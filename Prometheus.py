'''
from flask import Flask,request,render_template

from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
from prometheus_client import Histogram

REQUESTS= Counter('flask_redis_app_total_requests','How many times the application has been accessed')
EXCEPTIONS = Counter('flask_redis_app_total_exceptions','How many times the application issued an exception')

INPROGRESS = Gauge('flask_redis_app_inprogress_gauge','How many requests to the app are currently in progress')
LAST = Gauge('flask_redis_app_latency_summary_seconds','time need for a request')

LANTENCY = Summary('flask_redis_app_latency_summary_seconds','time needed for a request')
LANTENCY_HIS = Histogram('flask_redis_app_latency_summary_seconds','time needed for a request')
'''

app = Flask(_name_)

def get_similar_tweets(sentence):
    
'''
    INPROGRESS.dec()
    return status
'''

@app.route('/', methods=['GET', 'POST'])
def index():
'''
    REQUEST.inc()
    LAST.set(time.time())
    INPROGRESS.dec()
    start = time.time()
    time.sleep(random.random())
'''    
    if request.method == 'POST':
        details = request.form
        if details['form_type'] == 'analysis_sentence':
            content = details['sentence']
            tweets = get_similar_tweets(details['sentence'])
            return render_template('index.html', content=content, tweets=tweets)
'''
    INPROGRESS.dec()
    lat =time.time()
    LATENCY.observe(lat-start)
    LATENCY_HIS.observe()
'''    
    return render_template('index.html', content='', tweets=-1)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
