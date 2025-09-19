from flask import Flask
from app.extensions import db
from app.routes.cart_routes import cart_bp
from app.routes.product import product_bp
from app.routes.init_routes import init_bp  # 初始化資料表與測試資料

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')  # 請確認 config.py 路徑正確
    db.init_app(app)

    # 註冊所有 Blueprint
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(init_bp)

    return app





