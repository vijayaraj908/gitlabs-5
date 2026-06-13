pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vijayaraj908/gitlabs-5.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo systemctl restart flask_app_service'
            }
        }
    }
    post {
        success {
            mail to: 'vijayaraj.innovate@gmail.com', subject: "Build Successful", body: "Deployment done."
        }
        failure {
            mail to: 'vijayaraj.innovate@gmail.com', subject: "Build Failed", body: "Check logs."
        }
    }
}
