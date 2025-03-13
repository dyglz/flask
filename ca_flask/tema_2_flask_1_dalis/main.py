from flask import Flask, render_template
from data import data # IMPORTUOJAME

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=data) # PERDUODAME Į ŠABLONĄ

@app.route('/about')
def about():
    return render_template('about.html')
  
@app.route('/services')
def services():
    return render_template('services.html')
  
@app.route('/contact')
def contact():
    return render_template('contact.html')
  
@app.route('/new_page')
def new_page():
    return render_template('new_page.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)