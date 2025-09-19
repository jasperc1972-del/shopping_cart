from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))

    # 關聯購物車項目
    cart_items = db.relationship('CartItem', backref='product', lazy=True)

    def __repr__(self):
        return f"<Product {self.name} (${self.price})>"
