from flask import Flask, flash, jsonify, render_template, request
import requests

import urllib.request
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


dinfo={}

@app.route('/', methods=['POST', 'GET'])

def my_search():
    if request.method == 'POST':
        task = request.form['task']
        url="https://www.googleapis.com/books/v1/volumes?q="
        max_result="maxResults=20"
        final_url=url+task+'&'+max_result
        json_obj=urllib.request.urlopen(final_url)
        data=json.load(json_obj)
        for  v in data['items']:
                mylink = v['volumeInfo']['previewLink']
                if isinstance(v, dict):
                    for x in v['volumeInfo']['imageLinks'].values():
                            for y in v['volumeInfo']['authors']:
                                
                                dinfo[v['id']]=x,y,mylink
        # for k,v in dinfo.items():
        #     print(k, v)
        print(dinfo)    
    
        return render_template('index.html',title="Get It Done!", dinfo=dinfo) 
        
    
app.run()