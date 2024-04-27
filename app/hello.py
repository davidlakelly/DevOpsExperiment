from flask import Flask
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
switchList = [
        {
        "name": "C9200",
        "serial": "ABCD00010",
        "ip": "192.168.1.1"     
    },
    {
        "name": "C9300",
        "serial": "ABCD00011",
        "ip": "172.168.44.2"  
    },
        {
        "name": "C9400",
        "serial": "ABCD00012",
        "ip": "172.33.44.2"    
    }
]
@app.route('/')
def hello():
    return 'login sucess'

@app.route('/sample')
def render_html():
    users = ["David", "John", "Paul", "George"]
    return render_template('sample.html', name="David",users=users )


@app.route('/datapage')
def render_data():
    return render_template('datapage.html', switches=switchList )



# This is the route fo the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/datapage')
    return render_template('loginpage.html', error=error)

if __name__ == '__main__':
    app.run()

