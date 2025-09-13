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
                bat 'docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% ./calculator_app'
            }
        }

  stage('Push to Docker Hub') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            bat """
                echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                docker push hemis15/calculator-app:5
            """
        }
    }
}


        stage('Deploy Container') {
            steps {
                bat '''
                docker stop calculator-app || exit 0
                docker rm calculator-app || exit 0
                docker run -d --name calculator-app -p 5000:5000 %DOCKER_IMAGE%:%BUILD_NUMBER%
                '''
            }
        }
    }
}

