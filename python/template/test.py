from web import db
from web.models.users import Users

def insertUsers():
    Users.query.delete()
    db.session.add(Users("test1","test@test.com","testpassword"))
    db.session.add(Users("test2","test@test.com","testpassword"))
    db.session.add(Users("test3","test@test.com","testpassword"))
    db.session.add(Users("test4","test@test.com","testpassword"))
    db.session.commit()
    
if __name__ == '__main__':
    insertUsers()