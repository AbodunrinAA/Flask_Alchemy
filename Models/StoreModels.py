from db import db


class StoreModel(db.Model):
    __tablename__ = 'Stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, _id, name):
        self.id = _id
        self.name = name

    def to_JsonNoItems(self):
        return {'id': self.id, 'name': self.name}

    def to_Json(self):
        return {'id': self.id, 'name': self.name, 'items': [item.to_Json() for item in self.items.all()]}

    @classmethod
    def get_Store_By_Name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()  # Replacing StoreModel with cls
        except:
            raise

    def insertStore(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            raise

    @classmethod
    def getAllStores(cls):
        try:
            return cls.query.all()
        except:
            raise

    def deleteStore(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            raise

    def updateStore(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise
