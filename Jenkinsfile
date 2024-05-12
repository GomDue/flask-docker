pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
                git branch: 'main', 
                credentialsId: 'jenkins-github-cred',
                url: 'https://github.com/GomDue/flask-docker.git/'
            }
        }
        stage('build') {
            steps {
                echo 'building the application...'
            }
        }
        stage('test') {
            steps {
                echo 'testing the application...'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the application...'
            }
        }
    }
}
