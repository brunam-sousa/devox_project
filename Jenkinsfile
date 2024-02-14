pipeline {
    agent { 
        docker {
            image 'python:3.10-alpine3.18'
            label 'agent-docker'
        }
    }
    stages {
        stage('Test Code Coverage - Pylint') {
            steps {
                sh 'python -m pylint devox'
                archiveArtifacts(artifacts: 'target/*.jar', fingerprint: true)
            }
        }
    }
}