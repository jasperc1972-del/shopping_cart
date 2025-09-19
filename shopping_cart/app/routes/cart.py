from flask import Blueprint, request, render_template, redirect, url_for
from app.extensions import db
from app.models.cart_item import CartItem
from app.models.product import Product

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/view_cart')
def view_cart():
    user_id = 1  # 假設固定使用者
    cart_items = db.session.query(CartItem, Product)\
        .join(Product, CartItem.product_id == Product.id)\
        .filter(CartItem.user_id == user_id).all()

    cart_data = [{
        'id': item.id,
        'name': product.name,
        'price': product.price,
        'quantity': item.quantity,
        'subtotal': product.price * item.quantity
    } for item, product in cart_items]

    total = sum(item['subtotal'] for item in cart_data)
    return render_template('view_cart.html', cart_items=cart_data, total=total)

@cart_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    user_id = 1
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

@cart_bp.route('/update_cart/<int:item_id>', methods=['POST'])
def update_cart(item_id):
    new_quantity = int(request.form['quantity'])
    item = CartItem.query.get(item_id)
    if item:
        item.quantity = new_quantity
        db.session.commit()
    return redirect(url_for('cart_bp.view_cart'))

@cart_bp.route('/remove_item/<int:item_id>', methods=['POST'])
def remove_item(item_id):
    item = CartItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('cart_bp.view_cart'))