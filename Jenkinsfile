pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Setup') {
            steps {
                sh 'apt-get update -y'
                sh 'apt-get install -y python3 python3-pip python3-venv' // Added python3-venv
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                // 1. Create a virtual environment named 'venv'
                sh 'python3 -m venv venv'

                // 2. Use the pip from the virtual environment to install packages
                sh 'venv/bin/python3 -m pip install -r requirements.txt'

                // 3. Use the pytest from the virtual environment to run tests
                sh 'venv/bin/python3 -m pytest -q'
            }
        }
    }
}