pipeline {
    agent any
    environment  {
        IMAGE_NAME = 'test'
        BUILD_ID = 'latest'
    }
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
                bat 'docker build --tag ${IMAGE_NAME}:${BUILD_ID} .'
            }
        }
        stage('test') {
            steps {
                echo 'test...'
            }
        }
        stage('login Docker Hub') {
            steps {
                bat 'echo ${env.DOCKERHUB_ID} | docker login -u ${env.DOCKERHUB_PASSWORD} --password-stdin'
            }
        }
        stage('deploy') {
            steps {
                bat 'docker push ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
        stage('remove docker image') {
            steps {
                bat 'docker rmi ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
    }
}
