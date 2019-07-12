from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'niceonefrom@flask'

posts = [
    {
        'author':'otitoju john',
        'title':'Introduction to python flask',
        'content':'First flask post',
        'date':'July 13, 2019'
    },
    {
        'author':'john doe',
        'title':'Introduction to Node',
        'content':'First node post',
        'date':'July 12, 2019'
    },
    {
        'author':'Josephine',
        'title':'Introduction to physics',
        'content':'First physics post',
        'date':'July 10, 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)