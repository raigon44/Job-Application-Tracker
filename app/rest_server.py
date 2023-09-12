from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from flask_restful import Api, Resource
from user_dao import insert_user
from database_util import get_mysql_connection
from flask_bcrypt import Bcrypt
from forms import LoginForm

app = Flask(__name__)
CORS(app)
api = Api(app)

bcrypt = Bcrypt(app)

form = LoginForm()


@app.route('/')
def hello():
    # return send_file('ui/home.html')
    return render_template('home.html',
                           form=form)


@app.route('/getjobs')
def get_jobs():
    return 'This returns'


@app.route('/dashboard')
def show_dashboard():
    return 'This is the dashboard page'


class createaccount(Resource):
    def post(self):

        user_data = request.json
        db_connection = get_mysql_connection()
        insert_user(db_connection, bcrypt, user_data)

        db_connection.close()
        return 'user account created'


class login(Resource):
    def get(self):
        """
        This method does the following things:
        1. Retrieves the password of the user from the database
        2. If no password is available then returns a message saying the email ID entered is not present in our system
        3. If password is available, then checks it with the password received to the API
        :return:
        """
        login_form = LoginForm(request.GET)
        print(login_form.email)
        return


api.add_resource(createaccount, '/createaccount', methods=['POST'])
api.add_resource(login, '/login', methods=['GET'])

if __name__ == '__main__':
    print("Starting the Python Flask Server for Job Application Tracking System")
    app.run(port=5000)