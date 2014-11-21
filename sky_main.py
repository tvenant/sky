__author__ = 'john'

from flask import Flask,request,render_template, make_response,redirect, session, url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required




app = Flask(__name__)
app.config['SECRET_KEY'] = '-_=)+=@"<.>?/C54(*7`~``~N,3290<N..the_DANGROUS!|"$#%1Q__from__KIGALI!|!|!'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html',current_time = datetime.utcnow())

class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField()

@app.route('/user',methods=['GET','POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('user'))
    return render_template('user.html',form=form, name = session.get('name'))

@app.route('/greeting/<name2>')
def greeting(name2):
    return render_template('greetings.html',name = name2)

@app.route('/<int:value>')
def counter(value):
    values = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five'}
    return render_template('counter.html',value = values.get(value,'unkown'))

@app.route('/browser')
def which_browser():
    # import pdb;pdb.set_trace()
    user_agent = request.headers.get('User-Agent')
    response = render_template('browser.html',browser=user_agent)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/response')
def my_response():
    return make_response("<h1>Hello my sweet Response!</h1>")

@app.route('/facebook')
def redirect_to_facebook():
    return redirect('http://www.facebook.com')

@app.route('/test')
def testing():
    pass


if __name__ == '__main__':
    app.run(debug = True)
