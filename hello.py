import os
from flask import Flask
from flask import render_template, json
import random
import requests
from flask_caching import Cache
import csv

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def get_permutations(gids, sheet_url):
    options = []
    for gid in gids:
        response = requests.get(sheet_url+'&gid='+str(gid))
        data = response.content.decode('utf-8')
        choices = []
        csv_reader = csv.reader(data.splitlines())
        for row in csv_reader:
            choices.append(row[1]) # different for test data
        options.append(choices)
    return options

def get_random(options):
    responses = []
    for val in options:
        try:
            r = random.randint(1, len(val))
            responses.append(val[r])
        except:
            responses.append('')
    return responses

questions = [
        'During their first year, students…',
        'Students develop and demonstrate their quantitative skills…',
        'Students develop language skills…',
        'Students achieve the breadth expected of a liberal arts education…',
        'Students develop a nuanced understanding of power, inequality, and justice in our society…',
        'Students further develop their mind-body connection…',
        'We assess and represent competencies…',
        'Our undergraduate credentialing includes…',
        'Students deepen their writing abilities beyond the first year by…',
        'Students practice interdisciplinary thinking…',
        'Students engage in experiential or community-engaged learning…',
        'Our graduate students interact with our undergraduates through…',
        'Seniors integrate their college experience and demonstrate their mastery of their academic program…',
        'Our curriculum supports students from historically-excluded populations…']

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; frame-ancestors 'self' https://digitalscholarship.brynmawr.edu https://digbmc.github.io; script-src 'self'"
    return response

@app.route("/")
def request_data():
    options = cache.get('main_data')
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
        cache.set('main_data', options, timeout=300)
    pairs = []
    for val in options:
        r = random.randint(1,10)
        pairs.append((val[0], val[r]))
    return render_template("hello.html", entry=pairs)

@app.route("/options")
# has values for main event
def request_options():
    options = cache.get('option_data')
    if options is None:
        sheet_gids = [1202051472, 1009788276, 1362786704, 2071309954, 865859103,
            60204872, 1356126397, 1552947615, 1430527252, 427379088, 299682830,
            1641709279, 1638835585, 1425001770]
        sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRIKHYbU9rAl4uAlZcy-L1OEAgbYMCyp_3mamMxQH-PyIcR6IkWWmy6GTN9MhNNSmcd9KPhWK6KumL-/pub?output=csv"
        options = []
        for gid in sheet_gids:
            response = requests.get(sheet_url+'&gid='+str(gid))
            data = response.content.decode('utf-8')
            choices = []
            csv_reader = csv.reader(data.splitlines())
            for row in csv_reader:
                choices.append(row[1]) 
            #choices = data.splitlines()
            options.append(choices)
        cache.set('option_data', options, timeout=100)
    
    responses = []
    for val in options:
        try:
            r = random.randint(1, len(val))
            responses.append(val[r])
        except:
            responses.append('')
    questions = [
        'During their first year, students…',
        'Students develop and demonstrate their quantitative skills…',
        'Students develop language skills…',
        'Students achieve the breadth expected of a liberal arts education…',
        'Students develop a nuanced understanding of power, inequality, and justice in our society…',
        'Students further develop their mind-body connection…',
        'We assess and represent competencies…',
        'Our undergraduate credentialing includes…',
        'Students deepen their writing abilities beyond the first year by…',
        'Students practice interdisciplinary thinking…',
        'Students engage in experiential or community-engaged learning…',
        'Our graduate students interact with our undergraduates through…',
        'Seniors integrate their college experience and demonstrate their mastery of their academic program…',
        'Our curriculum supports students from historically-excluded populations…']
    return render_template("options.html", entry=zip(questions, responses))

@app.route("/alumni")
def request_alumni():
    alumni = cache.get('alumni_data')
    if alumni is None:
        sheet_gids = [1202051472, 1009788276, 1362786704, 2071309954, 865859103,
            60204872, 1356126397, 1552947615, 1430527252, 427379088, 299682830,
            1641709279, 1638835585, 1425001770]
        sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRIKHYbU9rAl4uAlZcy-L1OEAgbYMCyp_3mamMxQH-PyIcR6IkWWmy6GTN9MhNNSmcd9KPhWK6KumL-/pub?output=csv"
        alumni = get_permutations(sheet_gids, sheet_url)
        cache.set('alumni_data', alumni, timeout=100)
    responses = get_random(alumni)
    return render_template("options.html", entry=zip(questions, responses))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)