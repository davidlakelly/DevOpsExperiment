from flask import Flask, render_template, redirect, url_for, request, send_file
import api_call
import db_query
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
authflag = 1
#temp switch list pending methods

switchList = [
        {
        "indic_de": "C9200",
        "geo": "IRE",
        "TIME_PERIOD": "2001" ,    
         "OBS_VALUE": "1000",
        "OBS_FLAG": "A" 
    },
    {
        "indic_de": "C9200",
        "geo": "IRE",
        "TIME_PERIOD": "2002" ,    
         "OBS_VALUE": "1500",
        "OBS_FLAG": "A" 
    },
        {
        "indic_de": "C9200",
        "geo": "IRE",
        "TIME_PERIOD": "2003" ,    
         "OBS_VALUE": "1800",
        "OBS_FLAG": "A" 
    }
]

@app.route('/getapidata')
def get_data():
    logging.debug("Fetching data from API")
    data = api_call.get_data()
    logging.debug("Data fetched successfully")
    return data

@app.route('/getdbdata')
def get_db_data():
    logging.debug("Fetching data from database")
    data = db_query.readSqliteTable()
    logging.debug("Data fetched successfully")
    return data


@app.route('/')
def hello():
    logging.debug("Hello World")
    return redirect('/login')

@app.route('/sample')
def render_html():
    logging.debug("Rendering HTML")
    users = ["David", "John", "Paul", "George"]
    return render_template('sample.html', name="David",users=users)


# This is the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login(error = None):

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': #admin login fails
            error = 'Invalid Credentials. Please try again.'
            authflag = 0
            return render_template('loginpage.html', error=error)
        else:
            authflag = 1
            return redirect('/datapage') # login success
    else:
        return render_template('loginpage.html', error=error)


@app.route('/datapage') #This is the route for the data page
def render_data():
    if authflag == 1: #login success
        return render_template('datapage.html', switches=switchList )
    else: #attempting to access page berfore login
        return render_template('loginpage.html', error = 'Unauthroised Access Attempt')


@app.route('/graphpage')
def render_graph_demo():
    temp_labels = [x['TIME_PERIOD'] for x in switchList]
    temp_data = [y['OBS_VALUE'] for y in switchList]

    return render_template(
    template_name_or_list='graphpage.html',
    data=temp_data,
    labels=temp_labels)



@app.route('/download')
def downloadFile ():
    path = "static/test.csv"
    #print working directory
    print(os.getcwd(), file=sys.stdout)
    #list directory
    print(os.listdir(), file=sys.stdout)
    data = api_call.get_data()
    with open(path, "w+") as text_file:
        text_file.write(str(data))
    return send_file(path, as_attachment=True), 201

@app.route('/error')
def teapot_error():
    return render_template('418.html'), 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

