import os
from os.path import abspath, dirname
import uuid
from dotenv import load_dotenv

# Get the root directory of the project
ROOT_DIR = abspath(dirname(__file__))
# Generate a random secret key for the application
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or str(uuid.uuid4())
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(ROOT_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(ROOT_DIR, 'app/uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xlsx', 'xls', 'doc', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for file uploads
    DEBUG = True
    
