// Define a variable to hold the built image, so it can be shared between stages
def appImage

pipeline {
    agent none

    stages {
        stage('Checkout') {
            agent any
            steps {
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
            agent {
                docker { image 'python:3.12-slim' }
            }
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    // Build the image and assign it to the 'appImage' variable
                    appImage = docker.build("souravmdileep/sci-calc:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Push Docker Image') {
            agent any
            steps {
                script {
                    // Use the stored credentials to log in to Docker Hub and push the image
                    docker.withRegistry('', 'dockerhub-credentials') {
                        appImage.push()
                    }
                }
            }
        }
    }
}