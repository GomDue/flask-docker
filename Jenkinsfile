pipeline {
    agent any

    enviroment {
        IMAGE_NAME = 'test'
        BUILD_ID = 'latest'
        DOCKERHUB_CREDENTIALS = credentials('sue-dockerhub')
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
                sh 'echo ${DOCKERHUB_CREDENTIALS_PSW } | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin'
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
