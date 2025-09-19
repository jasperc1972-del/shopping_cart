from flask import Blueprint, render_template, request, redirect, url_for
from app.models.product_model import Product  # ✅ 加上這行
from app.models.cart_item_model import CartItem
from app.extensions import db

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products')
def products():
    product_list = Product.query.all()
    return render_template('products.html', products=product_list)

@product_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    user_id = 1  # 假設固定使用者
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])

    item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        item.quantity += quantity
    else:
        item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
        db.session.add(item)

    db.session.commit()
    return redirect(url_for('cart_bp.view_cart'))