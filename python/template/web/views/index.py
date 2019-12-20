from .. import application, db
from ..models.users import Users
from flask import request, jsonify
from flask_jwt_extended import create_access_token,jwt_optional, get_jwt_identity

def get_user(mail,password):
    
    users = Users.query.filter_by(mail=mail).one()
    

@application.route('/')
def index():
    users = Users.query.all()
    return "Hello World"

@application.route('/login',methods=['POST'])
def login():
    mail = request.json.get('mail',None)
    passowrod = request.json.get('passowrd',None)
    access_token = create_access_token(identity=mail)
    print(mail)
    return jsonify(access_token=access_token),200

@application.route('/manager',methods=['GET'])
@jwt_optional
def manager():
    login_user = get_jwt_identity()
    return jsonify(login=login_user)