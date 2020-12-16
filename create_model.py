import multiprocessing
import pandas as pd
from os import path
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer
from webapp import normalize

nlp = English()
tokenizer = Tokenizer(nlp.vocab)
current_dir = path.abspath('.')
MODEL_FILE_NAME = path.join(path.abspath('.'), 'model_file')


data = pd.read_csv(path.join(current_dir, 'tweets.csv'), index_col=0)
data = data.drop_duplicates(subset=['id'])


def process(text, *, remove_stopwords=True, remove_punct=False):
    norm = normalize(text, remove_stopwords)
    tokens = list(tokenizer(norm))
    if remove_punct:
        tokens = [t for t in tokens if not t.is_punct or t.is_space]
    return [str(token) for token in tokens]


data.loc[:, 'tokens'] = data.text.apply(process)
sentences = []
for ind in data.index:
    tweet_tokens = data['tokens'][ind]
    sentences.append(TaggedDocument(tweet_tokens, [ind]))

size = 300
context_window = 50
min_count = 1
max_iter = 200

model = Doc2Vec(
    documents=sentences,
    min_count=min_count,  # ignore words with freq less than min_count
    max_vocab_size=None,
    window=context_window,  # the number of words before and after to be used as context
    size=size,  # is the dimensionality of the feature vector
    workers=multiprocessing.cpu_count(),
    iter=max_iter  # number of iterations (epochs) over the corpus)
)

model.save(MODEL_FILE_NAME)
