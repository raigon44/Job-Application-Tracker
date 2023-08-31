from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_restful import Api, Resource
from user_dao import insert_user
from database_util import get_mysql_connection

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def hello():
    return send_file('ui/home.html')


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
        insert_user(db_connection, user_data)

        db_connection.close()
        return 'user account created'


api.add_resource(createaccount, '/createaccount', methods=['POST'])

if __name__ == '__main__':
    print("Starting the Python Flask Server for Job Application Tracking System")
    app.run(port=5000)