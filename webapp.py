from flask import Flask, request, render_template

app = Flask(__name__)


def get_similar_tweets(sentence):
    tweets_found = []
    tweet_found = ''
    for i in range(1, 21):
        tweets_found.append("Top " + str(i) + " :" + tweet_found)
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
