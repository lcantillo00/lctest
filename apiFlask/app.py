from flask import Flask, flash, jsonify, render_template, request
import requests

import urllib.request
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

tasks=[]
info=[]
@app.route('/', methods=['POST', 'GET'])

def my_search():
    if request.method == 'POST':
        task = request.form['task']
        url="https://www.googleapis.com/books/v1/volumes?q="
        max_result="maxResults=5"
        final_url=url+task+'&'+max_result
        json_obj=urllib.request.urlopen(final_url)
        data=json.load(json_obj)
        for item in data['items']:
           mydata=item['kind']
           tasks.append(mydata)
        for  v in data['items']:
            if isinstance(v, dict):
                for x in v['volumeInfo']:
                    info.append(x)
                # print(v['volumeInfo'])
            else:
                print("{0} : {1}".format(k, v))
        # for item in data['items']:
        #     for x in item['volumeInfo']:
        #         print(type(x))
        #     #    for z,y in x.items():
        #     #        print(type(y))
        return render_template('index.html',title="Get It Done!", tasks=tasks, info=info) 
        
    
app.run()