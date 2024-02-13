pipeline {
    agent any
    stages {
        stage('Test Code Coverage - Pylint') {
            steps {
                sh 'python -m pylint devox'
            }
        }
    }
}