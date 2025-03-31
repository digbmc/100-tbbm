from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu;"
    return response

@app.route("/")
def hello_world():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
