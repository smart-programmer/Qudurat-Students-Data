from Qudurat import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)




class StudenData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    academic_number = db.Column(db.String(9), nullable=False)
    ID_number = db.Column(db.String(20), nullable=False)
    number_of_try = db.Column(db.String(1), nullable=False)
    math_degree = db.Column(db.String(3), nullable=False)
    language_degree = db.Column(db.String(3), nullable=False)
    degrees_sum = db.Column(db.String(4), nullable=False)
    



class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10), nullable=False)

