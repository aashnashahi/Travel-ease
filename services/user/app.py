from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus Counter metric
REQUEST_COUNT = Counter('user_http_requests_total', 'Total HTTP Requests for user Service')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return jsonify(message="Welcome to the user Service!")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

