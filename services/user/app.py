from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

SERVICE_NAME = "user"
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['service'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(service=SERVICE_NAME).inc()
    return jsonify(message=f"Welcome to the {SERVICE_NAME.capitalize()} Service!")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
