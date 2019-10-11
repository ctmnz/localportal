pipeline {
    agent {label 'agent01'}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
		sh 'pip3 install -r requirements.txt'
		sh 'chmod 700 app/server.py'
		sh 'export FLASK_APP=app/server.py'
		sh 'python3 ./app/server.py &'
		sh 'curl -i localhost:5000/'
		sh 'curl -i localhost:5000/news.html'
		sh 'curl -i localhost:5000/barca.html'
            }
        }
    }
}
