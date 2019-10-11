pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip3 install -r requirements.txt'
		sh 'export FLASK_APP=app/server.py'
		sh 'python -m flask run'
            }
        }
    }
}
