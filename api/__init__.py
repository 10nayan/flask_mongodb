from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import and register your API routes here
from . import endpoints