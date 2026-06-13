pipeline {
    agent any
    stage('Install Dependencies') {
    steps {
        sh '''
        # Create the virtual environment if it doesn't exist
        if [ ! -d "venv" ]; then
            python3 -m venv venv
        fi
        # Install dependencies inside the virtual environment
        ./venv/bin/pip install -r requirements.txt
        '''
    }
}
stage('Deploy') {
    steps {
        // IMPORTANT: Ensure your systemd service uses the venv's python path
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
