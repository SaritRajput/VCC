from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def health():
    return jsonify(
        service="VCC Backend Microservice",
        status="UP"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
