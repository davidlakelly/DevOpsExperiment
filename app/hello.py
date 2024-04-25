from flask import Flask
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/sample')
def render_html():
    users = ["David", "John", "Paul", "George"]
    return render_template('sample.html', name="David",users=users )

# This is the route fo the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/')
    return render_template('loginpage.html', error=error)

if __name__ == '__main__':
    app.run()

