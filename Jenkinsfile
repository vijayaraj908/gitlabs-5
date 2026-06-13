pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                // Ensure venv is created and dependencies installed
                sh '''
                if [ ! -d "venv" ]; then
                    python3 -m venv venv
                fi
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                // Restarting the service
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
