__author__ = 'john'

from flask import Flask,request

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    user_agent = request.headers.get('User-Agent')
    return """<body bgcolor='orange'><h1> Hello %s. Im called The Dangerous!</h1><br/>
    <p>Your browser is: \"%s\"</p></body>"""%(name,user_agent)


if __name__ == '__main__':
    app.run(debug = True)