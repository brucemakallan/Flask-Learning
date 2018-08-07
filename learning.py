from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# set secret key for csrf and more
app.config['SECRET_KEY'] = 'b3e8ff1868b94ad6bd68bc9433766779'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# show flash message. Add provision in layout
		flash(f'Account created for {form.username.data}!', 'success')  # 2nd arg for HTML class
		return redirect(url_for('home'))  # go home
	return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)