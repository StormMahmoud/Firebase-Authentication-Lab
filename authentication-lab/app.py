from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyAHi89SznT5b_FgOoW4T8BCK1nULEP8uhM",
  "authDomain": "mahmoud-80a43.firebaseapp.com",
  "projectId": "mahmoud-80a43",
  "storageBucket": "mahmoud-80a43.appspot.com",
  "messagingSenderId": "780139978483",
  "appId": "1:780139978483:web:94cfe6528fa449957ee186",
  "measurementId": "G-GW2TRJ0672",
  "databaseURL" :"" }
  

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


#ry:
            

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        print("heyy")
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        #except:
         #   return render_template('signin.html')
    else:
        return render_template('signin.html')

    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    erorr = ""
    if request.method == 'POST':
        email = request.form['email']
        password =  request.form['password']
        #try:
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
        return redirect(url_for('signin'))
        #except:
         #   return render_template("signup.html")
    return render_template("signup.html")        


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)