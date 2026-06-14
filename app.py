from flask import Flask, jsonify, render_template
import psutil
import subprocess

app = Flask(__name__, template_folder='.')

def get_nginx_status():
    try:
        # Check if nginx is active
        status = subprocess.check_output(['systemctl', 'is-active', 'nginx']).decode().strip()
        return status
    except subprocess.CalledProcessError:
        return "inactive"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    nginx = get_nginx_status()  # New check
    return jsonify({"cpu": cpu, "memory": memory, "disk": disk, "nginx": nginx})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
