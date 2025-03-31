import os
from flask import Flask
from flask import render_template, json
import random
import requests

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu;"
    return response

@app.route("/")
# def get_data_from_json():
#     data_dir = os.path.join(os.path.dirname(__file__), 'data')
#     filename = os.path.join(data_dir, 'bmc.json')
#     with open(filename) as test_file:
#         data = json.load(test_file)
#         pairs = []
#         for entry in data['sheets']:
#             r = random.randint(1,10)
#             for key in entry.keys():
#                 p = (entry[key][0], entry[key][r])
#                 pairs.append(p)
#         return render_template("hello.html", entry=pairs)
def request_data():
    sheet_gids = [1753778501, 62073537, 0, 1662803068,
    986138193, 1983999724, 1676654895, 522650580,
    79503554, 805567290, 391711747, 97925162,
    1366782536, 1477837928, 1669471132]

    sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ129TGBwN5BhU6FshY10G_yYJaVD6z5dGoHsgo0DWgoT6AIqB3g_QWgxRjG-P_UxNxPCUpTozj6VaA/pub?output=csv"
    pairs = []
    for gid in sheet_gids[1:]:
        response = requests.get(sheet_url+'&gid='+str(gid))
        data = response.content.decode('utf-8')
        choices = data.splitlines()
        r = random.randint(1,10)
        pairs.append((choices[0], choices[r]))
    return render_template("hello.html", entry=pairs)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)