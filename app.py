from flask import Flask, render_template, request, redirect, url_for, redirect
import subprocess

app = Flask(__name__,template_folder='templates')

users={}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('streamlit_report'))
        elif username not in users:
            return render_template('loginsignup.html', login_error="User does not exist. Please signup")
        else:
            return render_template('loginsignup.html', login_error="Wrong password. Please try again.")
    return render_template('loginsignup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if username in users:
            return render_template('loginsignup.html', signup_error="User already exists")
        else:
            users[username] = password
            return redirect(url_for('login'))
    return render_template('loginsignup.html')

@app.route('/streamlit_report', methods=['GET', 'POST'])
def streamlit_report():
    if request.method == 'GET':
        return redirect('https://heartdiseasepredictor-jirffudm7capxkw7mtbm6g.streamlit.app/')

if __name__ == '__main__':
    app.run(debug=True)
