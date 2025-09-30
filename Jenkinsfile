pipeline {
    agent {
        docker { image 'python:3.12-slim' }
    }

    stages {
        stage('Checkout') {
            steps {
                // The explicit checkout with the stored credential
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/souravmdileep/SPE-Mini-Project.git',
                        credentialsId: 'github-token'
                    ]]
                ])
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the image using your Dockerfile
                    // and tag it with your username and the build number
                    def appImage = docker.build("souravmdileep/sci-calc:${env.BUILD_NUMBER}")
                }
            }
        }
    }
}