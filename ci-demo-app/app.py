from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from the CI/CD demo app!")


@app.route("/health")
def health():
    return jsonify(status="ok")


def add(a, b):
    """Simple function so we have something to unit test."""
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
