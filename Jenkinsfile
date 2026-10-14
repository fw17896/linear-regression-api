pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy Prediction API') {
            steps {
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker compose ps'
                sh 'docker inspect -f "{{.State.Running}}" linear-regression-api'
            }
        }
    }
}
