from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "DELETE"])
def handle_request():
    if request.method == "POST":
        return "Received a POST request"
    elif request.method == "GET":
        return "Received a GET request"
    elif request.method == "DELETE":
        return "Received a DELETE request"

if __name__ == "__main__":
    app.run()