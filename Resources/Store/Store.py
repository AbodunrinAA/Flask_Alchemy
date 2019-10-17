from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.StoreModels import StoreModel as StoreModels

# Note: Sparse id better than dense


class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Store Name is required'
                        )

    @jwt_required()
    def post(self):
        """
        :param:
        :return:
        """
        response_data = Store.parser.parse_args()

        if StoreModels.get_Store_By_Name(response_data['name']):
            return {'message': 'A store with name {0} already exist'.format(response_data['name'])}, 400  # Bad request

        new_resource = StoreModels(None, response_data['name']).insertStore()
        if new_resource:
            return {'message': 'Record created successfully'}, 201  # Created
        return {'message': 'Record not created successfully'}, 500  # Server Error

    @jwt_required()
    def put(self):
        try:
            response_data = Store.parser.parse_args()

            store = StoreModels.get_Store_By_Name(response_data['name'])
            if store:
                store.name = response_data['name']
                store.updateStore()
                return {'message': 'Record updated successfully'}, 200
            StoreModels(_id=None, name=response_data['name']).insertStore()
            return {'message': 'Record created successfully'}, 201
        except:
            return {'message': 'Server Error, Do try again'}


class Stores(Resource):

    @jwt_required()
    def get(self, name):
        """
        :param name:
        :return:
        """
        try:
            store = StoreModels.get_Store_By_Name(name)
            if store:
                return store.to_Json(), 200
            return {'message': 'Record not found'}, 404  # 200 Ok, 404 Not Found
        except:
            return {'message': 'Server Error, Do try again'}, 500

    @jwt_required()
    def delete(self, name):
        try:
            store = StoreModels.get_Store_By_Name(name)
            if store:
                store.deleteStore()
                return {'message': 'Record removed successfully'}, 200
            return {'message': 'Record not found'}, 400
        except:
            return {'message': 'Server Error, Do try again'}, 500


class StoreList(Resource):
    @jwt_required()
    def get(self):
        """
        :return:
        """
        stores = StoreModels.getAllStores()
        result_Json = [store.to_Json() for store in
                       stores]
        return result_Json
