from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

    # 關聯購物車項目
    cart_items = db.relationship('CartItem', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"