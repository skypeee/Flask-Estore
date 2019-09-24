from flask.blueprints import Blueprint

user = Blueprint('User', __name__)

from User import views