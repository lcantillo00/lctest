from flask import Flask, flash, jsonify, render_template, request
from box import Box
import requests

import urllib.request
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

tasks=[]
dinfo={}
imag=[]

@app.route('/', methods=['POST', 'GET'])

def my_search():
    if request.method == 'POST':
        task = request.form['task']
        url="https://www.googleapis.com/books/v1/volumes?q="
        max_result="maxResults=5"
        final_url=url+task+'&'+max_result
        json_obj=urllib.request.urlopen(final_url)
        data=json.load(json_obj)
        # for item in data['items']:
        #    mydata=item['kind']
        #    tasks.append(mydata)
        for  v in data['items']:
            if isinstance(v, dict):
                for y in v['volumeInfo']['authors']:
                    # info.append(y)
                    for x in v['volumeInfo']['imageLinks'].values():
                        dinfo[y]=x
                        print(dinfo)
           
    
        return render_template('index.html',title="Get It Done!", tasks=tasks, dinfo=dinfo,imag=imag) 
        
    
app.run()