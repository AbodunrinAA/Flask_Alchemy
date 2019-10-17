from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.ItemModels import ItemModel as ItemModels


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Item Name is required'
                        )
    parser.add_argument('price',
                        type=int,
                        required=True,
                        help='Item Price is required'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Store_id is required'
                        )

    @jwt_required()
    def post(self):
        """
        :param:
        :return:
        """
        response_data = Item.parser.parse_args()
        try:
            if ItemModels.get_Item_By_Name(response_data['name']):
                return {'message': 'An item with name {0} already exist'.format(response_data['name'])},\
                       400  # Bad request

            new_resource = ItemModels(None, response_data['name'], response_data['price'],
                                      response_data['store_id']).insertItem()
            if new_resource:
                return {'message': 'Record created successfully'}, 201  # Created
            return {'message': 'Record not created successfully'}, 500  # Server Error
        except:
            return {'message': 'Server Error, Do try again'}, 500  # Server Error

    @jwt_required()
    def put(self):
        try:
            response_data = Item.parser.parse_args()

            item = ItemModels.get_Item_By_Name(response_data['name'])
            if item:
                item.price = response_data['price']
                item.store_id = response_data['store_id']
                item.updateItem()
                return {'message': 'Record updated successfully'}, 200
            ItemModels(_id=None, name=response_data['name'], price=response_data['price'],
                       store_id=response_data['store_id']).insertItem()
            return {'message': 'Record created successfully'}, 201
        except:
            return {'message': 'Server Error, Do try again'}


class Items(Resource):
    @jwt_required()
    def get(self, name):
        """
        :param name:
        :return:
        """

        item = ItemModels.get_Item_By_Name(name)
        if item:
            return item.to_Json(), 200
        return {'message': 'Record not found'}, 404  # 200 Ok, 404 Not Found

    @jwt_required()
    def delete(self, name):
        try:
            item = ItemModels.get_Item_By_Name(name)
            if item:
                item.deleteItem()
                return {'message': 'Record removed successfully'}, 200
            return {'message': 'Record not found'}, 400
        except:
            return {'message': 'Server Error, Do try again'}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):
        """
        :return:
        """
        items = ItemModels.getAllItems()
        result_Json = [item.to_Json() for item in
                       items]
        return result_Json
