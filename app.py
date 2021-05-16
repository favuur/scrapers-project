from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/scrape')
def handle_scrape():
    target_url=request.args.get('target_url')
    return 'Handling scrape data for' + target_url