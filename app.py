from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/api/stats')
def get_stats():
    # Retrieve CPU and Memory usage [cite: 23, 24]
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return jsonify(cpu=cpu, memory=memory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
