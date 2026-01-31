from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def health():
    return jsonify(
        service="Welcome to Virtualization of VM World",
        status="UP"
    )
@app.route("/hello")
def hello():
    return jsonify(
        service="Welcome from VM1",
        status="UP"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
