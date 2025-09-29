pipeline {
    // Define that the build should run inside a Docker container
    // This provides a clean environment with Python pre-installed
    agent {
        docker { image 'python:3.12-slim' }
    }

    stages {
        // We no longer need a 'Clean' or 'Setup' stage because the Docker agent
        // provides a fresh, clean environment for every single build.

        stage('Checkout') {
            steps {
                // This checks out the code into our temporary container
                checkout scm
            }
        }

        stage('Test') {
            steps {
                // Use the python that comes with the container to install dependencies and run tests
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest -q'
            }
        }
    }
}