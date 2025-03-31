import os
from flask import Flask
from flask import render_template, json
import random

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu;"
    return response

# def add_header(response):
#     response.cache_control.max_age = 300
#     return response

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/data")
def get_json():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    filename = os.path.join(data_dir, 'bmc.json')
    with open(filename) as test_file:
        data = json.load(test_file)
        pairs = []
        for entry in data['sheets']:
            r = random.randint(1,10)
            for key in entry.keys():
                p = (entry[key][0], entry[key][r])
                pairs.append(p)
        return render_template("hello.html", entry=pairs)

        # return ' '.join(data['sheets'][0]['62073537'])


"""
        entry = data['sheets'][0]
        pairs = []
        for key in entry.keys():
            pair = (entry[key][0], entry[key][1])
            pairs.append(pair)
    pairs = []
    for item in data['sheets'][0]:
        category = item[0]
        value = item[1]
        pairs.append((category, value))
    return render_template("hello.html", entry=pairs)
"""    
    # return data['sheets'][0]['62073537'][0]

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)