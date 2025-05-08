from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))