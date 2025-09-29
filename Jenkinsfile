pipeline {
    agent any

    stages {
        // Stage 1: Clean the workspace before starting
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        // Stage 2: Install Python and dependencies
        stage('Setup') {
            steps {
                sh 'apt-get update -y'
                sh 'apt-get install -y python3 python3-pip'
            }
        }

        // Stage 3: Get the code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 4: Run the tests
        stage('Test') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -q'
            }
        }
    }
}