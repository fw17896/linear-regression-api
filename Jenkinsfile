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

        stage('Deploy Linear Regression API') {
            steps {
                sh '''
                    set -e
                    cd "$WORKSPACE"

                    echo "Pulling Docker image..."
                    docker compose pull

                    echo "Starting API..."
                    docker compose up -d

                    echo "Waiting for API..."
                    sleep 5

                    echo "Testing prediction endpoint..."
                    curl --fail --silent --show-error \
                      "http://localhost:5000/predict?x1=2&x2=3&x3=1"
                '''
            }
        }
    }
}
