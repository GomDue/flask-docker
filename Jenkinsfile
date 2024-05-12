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
                sh 'docker build --tag ${IMAGE_NAME}:${BUILD_ID} .'
            }
        }
        stage('test') {
            steps {
                echo 'test...'
            }
        }
        stage('login Docker Hub') {
            steps {
                sh 'echo ${env.DOCKERHUB_ID} | docker login -u ${env.DOCKERHUB_PASSWORD} --password-stdin'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker push ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
        stage('remove docker image') {
            steps {
                sh 'docker rmi ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
    }
}
