pipeline {
    agent any

    stages {
        // Stage 1: Install Python and dependencies
        stage('Setup') {
            steps {
                // Jenkins runs as the 'root' user in the container, so no 'sudo' is needed
                sh 'apt-get update -y'
                sh 'apt-get install -y python3 python3-pip'
            }
        }

        // Stage 2: Get the code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 3: Run the tests
        stage('Test') {
            steps {
                // Use 'python3 -m pip' to be specific
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -q'
            }
        }
    }
}