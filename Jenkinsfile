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

    stage('Deploy API') {
        steps {
            sh '''
                set -e
                docker compose pull
                docker rm -f linear-regression-api || true
                docker compose up -d
                sleep 5
                curl --fail --silent --show-error "http://localhost:5000/predict?x1=2&x2=3&x3=1"
            '''
        }
    }
}
```

}
