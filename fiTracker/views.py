from flask import render_template
from flask import request, redirect, url_for, session, flash, g
from fiTracker import app
from models.MongoAlchemy import User

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.get_name(request.form['username']).first()
        if user.password != request.form['password']: 
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        #Verify User hasnt already been created
        requested_username = request.form['username']
        user = User.query.get_name(requested_username)
        if user.first():
            error = 'Username already exists please select another'
        else:
            parsed = dict([(key, val) for key, val in request.form.items()])
            user = User(**parsed)
            user.save ()
            session['logged_in'] = True
            flash('%s, Welcome!' % requested_username)
            return redirect(url_for('index'))
        return render_template('signup.html', error=error)
    return render_template('signup.html', error=error)


