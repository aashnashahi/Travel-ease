# TravelEase: Cloud-Native Microservices Deployment

TravelEase is a travel-tech project that demonstrates how to deploy microservices using Docker, Jenkins CI/CD, Terraform, AWS ECS, and monitoring tools like Prometheus, Grafana, and CloudWatch.

## 📁 Project Structure
```
travel-ease/
├── services/            # Microservices: booking, payment, user
├── docker-compose.yml   # Docker Compose setup
├── Jenkinsfile          # Jenkins CI/CD pipeline
├── terraform/           # Terraform AWS infrastructure
├── scripts/             # Deployment helper scripts
└── monitoring/          # Prometheus + Grafana config
```

## 🚀 Features
- Monorepo with GitHub for collaboration
- Docker-based containerization
- CI/CD with Jenkins and AWS ECR
- AWS ECS/EC2 for service hosting
- Monitoring via Prometheus, Grafana, and CloudWatch

## 🛠 Tech Stack
- GitHub, Docker, Jenkins, AWS ECS/EC2, Terraform
- Prometheus, Grafana, AWS CloudWatch

## 📦 How to Run
```bash
docker-compose up --build
```

## 🧪 How to Test
Visit:
- Booking: http://localhost:5000
- Payment: http://localhost:5001
- User: http://localhost:5002

Grafana: http://localhost:3000  
Prometheus: http://localhost:9090

## 👤 Author
Aashna Shahi  
DevOps Specialization  
