from .. import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    def __init__(self,name,mail,password):
        self.name = name
        self.mail = mail
        self.password = password