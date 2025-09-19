
from flask import Flask
from app.extensions import db
from app.routes.cart_routes import cart_bp  # 引入購物車 Blueprint
from app.routes.test import test_bp  # 引入測試 Blueprint**
from app.routes.product import product_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')  # 確保你有 config.py 設定資料庫
db.init_app(app)

app.register_blueprint(cart_bp)  # 註冊購物車路由
app.register_blueprint(test_bp)      # ✅ 註冊測試路由

@app.route('/')
def home():
    return 'Hello, Jasper! Flask is running 🎉'

if __name__ == '__main__':
    app.run(debug=True)








