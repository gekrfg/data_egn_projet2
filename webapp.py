from flask import Flask, request, render_template
import pandas as pd
import multiprocessing
import re
from os import path
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer

nlp = English()
# Create a blank Tokenizer with just the English vocab
tokenizer = Tokenizer(nlp.vocab)

data = pd.read_csv(path.join(path.abspath('.'), 'tweets.csv'), index_col=0)
data = data.drop_duplicates(subset=['id'])

current_dir = path.abspath('.')

def normalize(text, remove_stopwords):
    text = text.lower()
    regex = r'pic\.twitter\.com.*'
    text = re.sub(regex, '', text, 0, re.MULTILINE)

    text = nlp(text)
    lemmatized = list()

    for word in text:
        lemma = word.lemma_.strip()
        if lemma:
            if not remove_stopwords or lemma not in STOP_WORDS:
                lemmatized.append(lemma)

    return " ".join(lemmatized)


def remove_punctuation(tokens):
    return [t for t in tokens if not t.is_punct or t.is_space]


def process(text, *, remove_stopwords=True, remove_punct=False):
    norm = normalize(text, remove_stopwords)
    tokens = list(tokenizer(norm))
    if remove_punct:
        tokens = remove_punctuation(tokens)
    return [str(token) for token in tokens]


model = Doc2Vec.load(path.join(path.abspath('.'), 'model_file'))


def get_similar_tweets(sentence):
    tokens = process(sentence)
    vector = model.infer_vector(tokens)

    result = []
    try:
        for tweet_id, confidence in model.docvecs.most_similar([vector], topn=20):
            tweet = data.iloc[tweet_id]
            result.append(tweet)
    except Exception:
        try:
            for tweet_id, confidence in model.docvecs.most_similar([vector], topn=5):
                tweet = data.iloc[tweet_id]
                result.append(tweet)
        except Exception:
            try:
                for tweet_id, confidence in model.docvecs.most_similar([vector], topn=3):
                    tweet = data.iloc[tweet_id]
                    result.append(tweet)
            except Exception:
                for tweet_id, confidence in model.docvecs.most_similar([vector], topn=1):
                    tweet = data.iloc[tweet_id]
                    result.append(tweet)

    return result


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        if details['form_type'] == 'analysis_sentence':
            content = details['sentence']
            tweets = get_similar_tweets(details['sentence'])
            return render_template('index.html', content=content, tweets=tweets)

    return render_template('index.html', content='', tweets=-1)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
