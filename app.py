from flask import Flask
from flask_restful import Api

# Security
from flask_jwt import JWT

# User
from Resources.User.User import User, Users, UserList
from Security.Security import authenticate, identity

# Items
from Resources.Store.Store import Store, Stores, StoreList
from Resources.Item.Item import Item, Items, ItemList

# Sparse is better than dense
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Repository/ApplicationDb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # toggled off FlaskSQLAlchemy modification
# tracker and not that of SqlAlchemy itself

# Required for the security
app.secret_key = 'jose'

# Flask RESTful
api = Api(app)

# Create Db and Models tables
@app.before_first_request
def create_db():
    db.create_all()


# Security
jwt = JWT(app, authenticate, identity)

# Resources

# Item
api.add_resource(Item, '/item')
api.add_resource(Items, '/items/<string:name>')
api.add_resource(ItemList, '/items')

# Store
api.add_resource(Store, '/store')
api.add_resource(Stores, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# User
api.add_resource(User, '/user')
api.add_resource(Users, '/users/<string:username>')
api.add_resource(UserList, '/users')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
