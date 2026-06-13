from flask import Flask, jsonify, render_template
import psutil

# Point to current directory for HTML files
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return jsonify({"cpu": cpu, "memory": memory})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
