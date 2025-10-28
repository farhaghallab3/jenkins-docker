pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farhaghallab3/jenkins-docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t farha-app .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Remove old container if exists
                    sh 'docker rm -f farha-container || true'
                    // Run new container
                    sh 'docker run -d --name farha-container -p 8080:80 farha-app'
                }
            }
        }
    }
}
