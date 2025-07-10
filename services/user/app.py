from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)


SERVICE_NAME = "user"  

REQUEST_COUNT = Counter(
    f"{SERVICE_NAME}_http_requests_total", f"Total HTTP requests for {SERVICE_NAME} service"
)

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return jsonify(message=f"Welcome to the {SERVICE_NAME.capitalize()} Service!")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
