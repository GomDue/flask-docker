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
                script {
                    image = docker.build("${IMAGE_NAME}:${BUILD_ID}")
                }
            }
        }
        stage('test') {
            steps {
                echo 'test...'
            }
        }
        stage('login Docker Hub') {
            steps {
                sh "echo ${env.DOCKERHUB_ID} | docker login -u ${env.DOCKERHUB_PASSWORD} --password-stdin"
            }
        }
        stage('deploy') {
            steps {
                script {
                    image.push("${env.BUILD_NUMBER}")
                }
            }
        }
        stage('remove docker image') {
            steps {
                sh "docker rmi ${IMAGE_NAME}:${BUILD_ID}"
            }
        }
    }
}
