pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                // Ensure pip3 is installed on your EC2 instance
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                // This restarts the systemd service we configured
                sh 'sudo systemctl restart flask_app_service'
            }
        }
    }
    post {
        success {
            mail to: 'vijayaraj.innovate@gmail.com', 
                 subject: "SUCCESS: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}", 
                 body: "The deployment was successful!"
        }
        failure {
            mail to: 'vijayaraj.innovate@gmail.com', 
                 subject: "FAILURE: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}", 
                 body: "The build failed. Please check the Jenkins console output."
        }
    }
}
