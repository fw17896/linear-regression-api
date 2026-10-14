pipeline {
agent any

```
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

                echo "Pulling Docker image..."
                docker compose pull

                echo "Removing existing API container if present..."
                docker rm -f linear-regression-api || true

                echo "Starting API..."
                docker compose up -d

                echo "Waiting for API..."
                sleep 5

                echo "Testing prediction endpoint..."
                curl --fail --silent --show-error \
                  "http://localhost:5000/predict?x1=2&x2=3&x3=1"

                echo ""
                echo "API deployment successful!"
            '''
        }
    }
}
```

}
