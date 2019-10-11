pipeline {
    agent {label 'agent01'}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip3 install -r requirements.txt'
		sh 'chmod 700 app/server.py'
            }
        }
	stage('testing') {
	   steps {
		sh 'python3 app/test_server.py'
	   }
	}
    }
}
