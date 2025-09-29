pipeline {
    // Use any available Jenkins agent to run the pipeline
    agent any

    // Define the stages of the pipeline
    stages {
        // Stage 1: Get the code from GitHub
        stage('Checkout') {
            steps {
                // This command checks out the code from the repository
                checkout scm
            }
        }

        // Stage 2: Run the tests
        stage('Test') {
            steps {
                // Run shell commands to install dependencies and run pytest
                sh 'pip install -r requirements.txt'
                sh 'pytest -q'
            }
        }
    }
}