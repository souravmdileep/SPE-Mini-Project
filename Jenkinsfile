pipeline {
    // We define no global agent, so each stage can have its own.
    agent none

    stages {
        stage('Checkout') {
            // Run checkout on the main Jenkins node
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
            // Use the clean Python container just for testing
            agent {
                docker { image 'python:3.12-slim' }
            }
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            // Run the build on the main Jenkins node, which has Docker installed
            agent any
            steps {
                script {
                    def appImage = docker.build("souravmdileep/sci-calc:${env.BUILD_NUMBER}")
                }
            }
        }
    }
}