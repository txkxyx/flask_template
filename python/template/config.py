# coding: utf-8

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@flask_template:3306/flask_template?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CSRF対策
    SECRET_KEY = 'template'
    # JWTトークン
    JWT_SECRET_KEY = 'template-secret'