from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .shopping_cart import cart_blueprint

db = SQLAlchemy()
def create_app(config=None):
    app = Flask(__name__)
    
    
    app.add_url_rule('/', view_func=index, methods=['GET'])
    
    if app.debug:
        app.config.from_object('config_debug')
    else:
        app.config.from_object('config_debug')
    regist_blueprint(app)
    return app


def regist_blueprint(app):
    with app.app_context():
        app.register_blueprint(cart_blueprint)


def init_db(app):
    with app.app_context():
        db.init_app(app)


def index():
    from flask import current_app
    print(current_app.url_map)
    return 'Index'