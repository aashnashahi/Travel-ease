from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('payment_http_requests_total', 'Total HTTP requests to Payment service')

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Payment Service'})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
