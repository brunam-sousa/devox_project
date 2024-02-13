pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19'}}
    stages {
        stage('Test Code Coverage - Pylint') {
            steps {
                sh 'python -m pylint devox'
            }
        }
    }
}