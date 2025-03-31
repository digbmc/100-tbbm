from flask import Flask

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu;"
    return response

@app.route("/")
def hello_world():
    return "<h1>One thousand billion Bryn Mawrs</h1><p>Hello, World!</p><p><a href='https://support.reclaimhosting.com/hc/en-us/articles/9220813439127'>More info</a></p>"
