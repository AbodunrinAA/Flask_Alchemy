from db import db

connectionString = None


class ItemModel(db.Model):
    __tablename__ = "Items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    produce_date = db.Column(db.DateTime(), default=True)
    expire_date = db.Column(db.DateTime(), default=True)
    price = db.Column(db.Float(precision=5))
    store_id = db.Column(db.Integer, db.ForeignKey('Stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, _id, name, price, store_id):
        self.id = _id
        self.name = name
        self.price = price
        self.store_id = store_id

    def to_Json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'store': self.store.to_JsonNoItems()}

    @classmethod
    def get_Item_By_Name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()  # Replacing ItemModel with cls
        except:
            raise

    def insertItem(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            raise

    @classmethod
    def getAllItems(cls):
        try:
            return cls.query.all()
        except:
            raise

    def deleteItem(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            raise

    def updateItem(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise
