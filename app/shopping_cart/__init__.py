from flask import Blueprint

__all__ = ['cart_blueprint',]
cart_blueprint = Blueprint('cart', __name__, url_prefix='/shoping')

from . import routes
