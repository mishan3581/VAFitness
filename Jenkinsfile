pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mishan3581/VAFitness.git'
            }
        }
        stage('Build') {
            steps {
                sh './build.sh'
            }
        }
        stage('Test') {
            steps {
                sh './test.sh'
            }
        }
        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
