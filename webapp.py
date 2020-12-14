from flask import Flask, request, render_template
import pandas as pd
import difflib
import numpy as np


df = pd.read_csv("tweets.csv",index_col=0)
df['score'] = np.NaN


app = Flask(__name__)

def string_similar(s1, s2):
    return round(difflib.SequenceMatcher(None, s1, s2).quick_ratio(), 3)


def get_similar_tweets(sentence):
    tweets_found = []

    dfn = df.copy(deep=True)
    for i in range(0, 17215):
        sim = string_similar(sentence, str(dfn['text'][i]))
        if sim >= 0.5:
            dfn['score'].at[i] = float(sim)

    dfn.dropna(axis=0, inplace=True)
    dfn.sort_values(by=['score'], ascending=False, inplace=True)
    dfn = dfn.reset_index()

    if dfn.shape[0] >= 20:
        for j in range(0, 20):
            tweets_found.append("Top " + str(j+1) + " : " + str(dfn['text'][j]))
    else:
        for j in range(0, dfn.shape[0]):
            tweets_found.append("Top " + str(j+1) + " : " + str(dfn['text'][j]))
    return tweets_found


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
