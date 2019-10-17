from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.UserModels import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Username is required'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password is required'
                        )

    def post(self):

        try:
            response_data = Users.parser.parse_args()

            if UserModel.getUser_By_Username(response_data['username']):
                return {'message': 'User with the same Username already exist'}, 400  # Bad Request

            user = UserModel(None, **response_data)
            user.insertUser()
            return {'message': 'Record created successfully'}, 201  # Created

        except:
            return {'message': 'Connection Error, Please try again'}, 500  # Server Error


class Users(Resource):
    @jwt_required()
    def get(self, username):
        try:
            user = UserModel.getUser_By_Username(username)
            if user:
                return user.to_Json(), 200
            return {'message': 'Record not found'}, 400
        except:
            return {'message': 'Server Error, Do try again'}, 500


class UserList(Resource):
    @jwt_required()
    def get(self):
        try:
            users = UserModel.getAllUsers()
            users = [user.to_Json() for user in users]
            return users
        except:
            return {'message': 'Connection Error, Please try again'}, 500  # Server Error
