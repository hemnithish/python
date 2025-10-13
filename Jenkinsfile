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
        stage('Scan Image for Vulnerabilities') {
            steps {
                script {
                    // Trivy scan using Docker
                    bat """
                    docker run --rm -v //./pipe/docker_engine://./pipe/docker_engine -v %cd%:/workdir aquasec/trivy image ^
                    --format json -o /workdir/trivy-report.json ^
                    --exit-code 1 --severity CRITICAL,HIGH %DOCKER_IMAGE%:%IMAGE_TAG%
                    """
                }
            }
            post {
                always {
                    // Save the report as Jenkins artifact
                    archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
                }
                failure {
                    error "❌ HIGH or CRITICAL vulnerabilities detected — build failed!"
                }
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
                docker run -d --name calculator-app -p 8081:8000 %DOCKER_IMAGE%:%IMAGE_TAG%
                '''
            }
        }
    }
}

