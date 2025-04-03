import os
from flask import Flask
from flask import render_template, json
import random
import requests
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu https://digbmc.github.io; script-src 'self'"
    return response

@app.route("/")
def request_data():
    options = cache.get('option_data')
    
    if options is None:
        sheet_gids = [1753778501, 62073537, 0, 1662803068,
        986138193, 1983999724, 1676654895, 522650580,
        79503554, 805567290, 391711747, 97925162,
        1366782536, 1477837928, 1669471132]
        sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ129TGBwN5BhU6FshY10G_yYJaVD6z5dGoHsgo0DWgoT6AIqB3g_QWgxRjG-P_UxNxPCUpTozj6VaA/pub?output=csv"
        options = []
        for gid in sheet_gids[1:]:
            response = requests.get(sheet_url+'&gid='+str(gid))
            data = response.content.decode('utf-8')
            choices = data.splitlines()
            options.append(choices)
        cache.set('option_data', options, timeout=300)
    
    pairs = []
    for val in options:
        r = random.randint(1,10)
        pairs.append((val[0], val[r]))

    return render_template("hello.html", entry=pairs)

@app.route("/options")
def request_options():
    options = cache.get('option_data')
    
    if options is None:
        sheet_gids = [1753778501, 62073537, 0, 1662803068,
        986138193, 1983999724, 1676654895, 522650580,
        79503554, 805567290, 391711747, 97925162,
        1366782536, 1477837928, 1669471132]
        sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ129TGBwN5BhU6FshY10G_yYJaVD6z5dGoHsgo0DWgoT6AIqB3g_QWgxRjG-P_UxNxPCUpTozj6VaA/pub?output=csv"
        options = []
        for gid in sheet_gids[1:]:
            response = requests.get(sheet_url+'&gid='+str(gid))
            data = response.content.decode('utf-8')
            choices = data.splitlines()
            options.append(choices)
        cache.set('option_data', options, timeout=300)
    
    pairs = []
    for val in options:
        r = random.randint(1,10)
        pairs.append((val[0], val[r]))

    return render_template("options.html", entry=pairs)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)