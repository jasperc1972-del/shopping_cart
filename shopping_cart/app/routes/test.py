from flask import Blueprint
from app.models.product_model import Product

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/test_db')
def test_db():
    products = Product.query.all()
    output = '<h2>📦 商品清單</h2><ul>'
    for p in products:
        output += f'<li>{p.name} - ${p.price}</li>'
    output += '</ul>'
    return output