from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body':'You cant see me'
        },
        {
            'author':{'username': 'Rick'},
            'body':"Wubba lubba dub dub"
        }
    ]
    return render_template('index.html', title='Home', user = user, posts = posts)