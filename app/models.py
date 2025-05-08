from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    reports = db.relationship('Report', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    job_content = db.Column(db.Text)
    description = db.Column(db.Text)
    result_content = db.Column(db.Text)
    filename = db.Column(db.String(256))
    filepath = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def has_file(self):
        return self.filename is not None and self.filename != '' 

    def __repr__(self):
        return f'<Report {self.title}>'
    
    
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))