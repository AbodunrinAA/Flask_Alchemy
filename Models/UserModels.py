from db import db


class UserModel(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def to_Json(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}

    def insertUser(self):
        print(self.password)
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise

    @classmethod
    def getUser_By_Username(cls, username):
        try:
            return cls.query.filter_by(username=username).first()  # Replacing ItemModel with cls
        except:
            raise

    @classmethod
    def getUser_By_Id(cls, _id):
        try:
            return cls.query.filter_by(id=_id).first()  # Replacing ItemModel with cls
        except:
            raise

    @classmethod
    def getAllUsers(cls):
        try:
            return cls.query.all()  # Replacing ItemModel with cls
        except:
            raise
