from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric for counting requests
REQUEST_COUNTER = Counter('payment_requests_total', 'Total HTTP Requests to Payment Service')

@app.route('/')
def home():
    REQUEST_COUNTER.inc()
    return "Welcome to the Payment Service!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
