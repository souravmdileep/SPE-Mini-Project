pipeline {
    agent {
        docker { image 'python:3.12-slim' }
    }

    stages {
        stage('Checkout') {
            steps {
                // Use an explicit checkout with the stored credential
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
    }
}