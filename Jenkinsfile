pipeline {
    agent { 
        label 'agent1'
        }

    stages {
        stage('Configuring environment') { // configuring necessary packages and modules
            steps {
                sh 'python -m venv devox'
                sh 'pip install -r requirements.txt'              
            }
        }
        stage ('Test - Pylint') {// executing pylint to test the code
            steps{
                sh 'pylint devox'
            }
        }
    }
    post{
        failure{
             //archiveArtifacts(artifacts: 'target/*.jar', fingerprint: true)
             msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
        }
    }
}