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
                echo 'Copying updated files to production directory...'
                // CRITICAL STEP: Copy the updated index.html to your app directory
                sh 'cp index.html /home/ubuntu/app/index.html'
                
                // Restarting the service to apply changes
                echo 'Restarting Flask service...'
                sh 'sudo systemctl restart flask_app_service'
            }
        }
    }
    post {
        success {
            mail to: 'vijayaraj.innovate@gmail.com', 
                 subject: "SUCCESS: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}", 
                 body: "The deployment was successful! The new dashboard is now live."
        }
        failure {
            mail to: 'vijayaraj.innovate@gmail.com', 
                 subject: "FAILURE: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}", 
                 body: "The build failed. Please check the Jenkins console output."
        }
    }
}
