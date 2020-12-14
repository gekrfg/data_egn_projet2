from flask import Flask, request, render_template

REQUESTS= Counter('flask_redis_app_total_requests','How many times the application has been accessed')
EXCEPTIONS = Counter('flask_redis_app_total_exceptions','How many times the application issued an exception')

INPROGRESS = Gauge('flask_redis_app_inprogress_gauge','How many requests to the app are currently in progress')
LAST = Gauge('flask_redis_app_latency_summary_seconds','time need for a request')

app = Flask(_name_)

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
