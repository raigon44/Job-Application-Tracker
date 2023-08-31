from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


@app.route('/')
def hello():
    return send_file('ui/home.html')


@app.route('/login')
def login():
    return 'This is the login page'


@app.route('/createaccount')
def create_user_account():
    return 'This is the create account page'


@app.route('/getjobs')
def get_jobs():
    return 'This returns'


@app.route('/dashboard')
def show_dashboard():
    return 'This is the dashboard page'


if __name__ == '__main__':
    print("Starting the Python Flask Server for Job Application Tracking System")
    app.run(port=5000)