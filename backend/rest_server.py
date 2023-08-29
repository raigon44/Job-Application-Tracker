from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/index')
def hello():
    return 'This is the home page'

@app.route('/login')
def hello():
    return 'This is the login page'


@app.route('/createaccount')
def hello():
    return 'This is the create account page'

@app.route('/getjobs')
def hello():
    return 'This is the create account page'


if __name__ == '__main__':
    print("Starting the Python Flask Server for Job Application Tracking Systerm")
    app.run(port=5000)