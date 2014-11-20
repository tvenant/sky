__author__ = 'john'

from flask import Flask,request,render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name = name)

@app.route('/greeting/<name2>')
def greeting(name2):
    return render_template('greetings.html',name = name2)

@app.route('/<int:value>')
def counter(value):
    values = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five'}
    return render_template('counter.html',value = values.get(value,'unkown'))
@app.route('/browser')
def which_browser():
    user_agent = request.headers.get('User-Agent')
    return render_template('browser.html',browser=user_agent)
@app.route('/test')
def testing():
    pass

bootstrap = Bootstrap(app)
if __name__ == '__main__':
    app.run(debug = True)