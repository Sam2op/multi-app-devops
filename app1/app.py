
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "✅ Hello from App after CI/CD 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
