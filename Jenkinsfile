pipeline {
    agent any
    stages {
        stage('Build Docker Images') {
            steps {
                sh 'docker build -t booking-service ./services/booking'
                sh 'docker build -t payment-service ./services/payment'
                sh 'docker build -t user-service ./services/user'
            }
        }
        stage('Push to ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds']]) {
                    sh './scripts/push_to_ecr.sh'
                }
            }
        }
        stage('Deploy with Terraform') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }
    }
}
