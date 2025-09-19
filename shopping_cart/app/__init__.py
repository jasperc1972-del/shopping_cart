from flask import Flask
from app.extensions import db
from app.routes.cart import cart_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    app.register_blueprint(cart_bp)
    return app



