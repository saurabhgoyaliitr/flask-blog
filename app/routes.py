from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Saurabh'}
	posts = [
	{
		'author': {'username':'john'},
		'body': 'Wow, what a great move'

	}, 
	{
		'author': {'username':'susan'},
		'body': 'avengers are cool'

	}]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title = 'Sign In', form= form)


	




