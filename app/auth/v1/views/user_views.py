from app.auth.v1.models.user_models import UserModel
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("email", type='str')

class User(Resource):
    required=True,
    help='Please input your email'
    '''
    User endpoints
    '''
    def post(self):
        '''
        Register a user endpoint
        '''
        args = parser.parse_args()
        args = request.get_json()
        email = args["email"]
        password = args["password"]
        confirm_password = args["confirm_password"]
        task = args["task"]
        tasktimer = args["tasktimer"]
        taskbreak = args["taskbreak"]

        newUser = UserModel(email, password, confirm_password,task,tasktimer,taskbreak)
        newUser.save_user()

        return{
            "message":"User register successfully",
            "user":newUser.__dict__,
        },201

