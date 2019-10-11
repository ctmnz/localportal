pipeline {
    agent {label 'agent01'}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip3 install -r requirements.txt'
		sh 'chmod 700 app/server.py'
		sh 'export FLASK_APP=app/server.py'
		sh './app/server.py'
            }
        }
    }
}
