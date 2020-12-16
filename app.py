from flask import Flask, request, render_template
import pandas as pd
import multiprocessing
import re
from os import path
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer
import difflib
import numpy as np
import time
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
from prometheus_client import Histogram

REQUESTS = Counter('page_access', 'Acces for main page')
REQUESTS_RES = Counter('res_page', 'Results for page acces')
EXCEPTIONS = Counter('code_exceptions','how many times raise an exception')
INPROGRESS = Gauge('page_access_in_progress', 'Visits in progress')
LAST = Gauge('page_accesses_last_time_seconds', 'The last time a res_page was served')
LATENCY = Summary('latency_in_seconds', 'time needed for a request')
#LANTENCY_HIS = Histogram('latency_in_seconds','time needed for a request')

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
        i = 1
        for tweet_id, confidence in model.docvecs.most_similar([vector], topn=20):
            tweet = data.iloc[tweet_id]['text']
            result.append("Top " + str(i) + " : " + tweet)
            i = i + 1
    except Exception:
        return result

    return result


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        REQUESTS.inc()
        INPROGRESS.inc()
        REQUESTS_RES.inc()
        #with EXCEPTIONS.count_exceptions():
            #if random.random()<0.2:
                #raise Exception        
        details = request.form
        if details['form_type'] == 'analysis_sentence':
            content = details['sentence']
            tweets = get_similar_tweets(details['sentence'])
            return render_template('index.html', content=content, tweets=tweets)
        LAST.set(time.time())
        INPROGRESS.dec()
        LATENCY.observe(time.time() - start)
    return render_template('index.html', content='', tweets=-1)


if __name__ == '__main__':
    start_http_server(9090)
    app.run(host='0.0.0.0')
