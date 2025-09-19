from flask import Blueprint
from app.extensions import db
from app.models.product_model import Product

init_bp = Blueprint('init_bp', __name__)

@init_bp.route('/init_db')
def init_db():
    db.create_all()

    Product.query.delete()

    products = [
        Product(name='蘋果', price=30.0, stock=100, image_url='https://via.placeholder.com/150?text=Apple'),
        Product(name='香蕉', price=20.0, stock=80, image_url='https://via.placeholder.com/150?text=Banana'),
        Product(name='鳳梨', price=50.0, stock=50, image_url='https://via.placeholder.com/150?text=Pineapple')
    ]
    db.session.add_all(products)
    db.session.commit()

    return '✅ 資料表已建立並插入測試商品！'