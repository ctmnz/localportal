pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip install -r requirements.txt'
		sh 'export FLASK_APP=app/server.py'
		sh 'flask run'
            }
        }
    }
}
