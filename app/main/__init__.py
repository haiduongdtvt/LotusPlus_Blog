from flask import Blueprint

# Create the Blueprint instance
bp = Blueprint('main', __name__)

# Import routes at the bottom to avoid circular imports
from app.main import routes