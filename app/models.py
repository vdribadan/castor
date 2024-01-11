from app import db

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Fruit {self.name}>'
