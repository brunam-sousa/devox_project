pipeline {
    agent { 
        label 'agent1'
        }

    stages {
        stage('Configuring environment') { // configuring necessary packages and modules
            steps {
                //sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt -t venv/lib/python3.11/site-packages'              
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
            script{
                //archiveArtifacts(artifacts: 'target/*.jar', fingerprint: true)
                msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
            }
        }
    }
}