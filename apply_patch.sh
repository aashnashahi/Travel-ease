#!/bin/bash

echo "🛠️ Applying TravelEase Prometheus Metrics Patch..."

# Update app.py files
for service in user payment booking; do
cat > $service/app.py <<EOF
from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('${service}_requests_total', 'Total requests to ${service} service')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "${service^} service is running!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
EOF
echo "✅ $service/app.py updated."
done

# Ensure prometheus_client and flask are in Dockerfiles
for service in user payment booking; do
    if ! grep -q "prometheus_client" "$service/Dockerfile"; then
        echo "📦 Adding Flask + Prometheus dependencies to $service/Dockerfile"
        sed -i '/pip install/ s/$/ flask prometheus_client/' "$service/Dockerfile"
    else
        echo "✅ Dependencies already present in $service/Dockerfile"
    fi
done

# Update Prometheus config
mkdir -p prometheus
cat > prometheus/prometheus.yml <<EOF
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'user-service'
    static_configs:
      - targets: ['user:5000']

  - job_name: 'payment-service'
    static_configs:
      - targets: ['payment:5000']

  - job_name: 'booking-service'
    static_configs:
      - targets: ['booking:5000']
EOF

echo "✅ Prometheus config updated."

# Show success message
echo -e "\n🎉 Patch applied! Now rebuild with:"
echo "docker-compose down && docker-compose up --build"
