FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask prometheus_client requests \
    && apt-get update && apt-get install -y curl
EXPOSE 5000
CMD ["python", "app.py"]
