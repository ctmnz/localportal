pipeline {
    agent {label 'agent01'}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip3 install -r requirements.txt'
		sh 'export FLASK_APP=app/server.py'
		sh 'python3 -m flask run'
            }
        }
    }
}
