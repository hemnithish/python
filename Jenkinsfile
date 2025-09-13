pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hemis15/calculator-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hemnithish/python.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% ./calculator_app'
            }
        }

  stage('Push to Docker Hub') {
    steps {
         withCredentials([string(credentialsId: 'docker-token', variable: 'DOCKER_TOKEN')]) {
                    bat """
                        docker logout
                        docker login -u hemis15 -p %DOCKER_TOKEN%
                docker push %DOCKER_IMAGE%:%IMAGE_TAG%
            """
        }
    }
}


        stage('Deploy Container') {
            steps {
                bat '''
                docker run -d --name calculator-app -p 5000:5000 %DOCKER_IMAGE%:%%IMAGE_TAG%
                '''
            }
        }
    }
}

