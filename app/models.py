from app import db
from werkzeug.security import generate password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    username db.Column(db.String(50))
    email   db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
    return '<User {}: {}>'.format(self.name, self.username)

    def set_password(self, password):
    self.password_hash = generate_password_hash(password)

    def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))
