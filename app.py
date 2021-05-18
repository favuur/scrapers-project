from flask import Flask, request, render_template
import re
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)
app.run(use_reloader=True)

def performScrape(target_url):
    with urllib.request.urlopen(target_url) as response:
        html=response.read()
        soup=BeautifulSoup(html,"html.parser").b
        
        print(soup)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/scrape')
def handle_scrape():
    target_url=request.args.get('target_url')

    expression = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    isAUrl = re.match(expression, target_url)

    if (isAUrl) :
        performScrape(target_url)

    return "TARGET URL provided is not a URL Format E.g https://google.com"
    
    