pipeline {
    agent { 
        docker { image 'python:3.10-alpine3.18'}
    }
    stages {
        stage('Test Code Coverage - Pylint') {
            steps {
                sh 'python -m pylint devox'
            }
        }
    }
}