from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['service'])

SERVICE_NAME = 'user'  

@app.route('/')
def home():
    REQUEST_COUNT.labels(service=user).inc()
    return jsonify(message=f"Welcome to the {user.capitalize()} Service!")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
