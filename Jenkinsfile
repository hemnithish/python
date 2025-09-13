pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hemis15/calculator-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hemnithish/python.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER ./calculator_app'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop calculator-app || true
                docker rm calculator-app || true
                docker run -d --name calculator-app -p 5000:5000 $DOCKER_IMAGE:$BUILD_NUMBER
                '''
            }
        }
    }
}
