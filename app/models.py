from app import db

class Fruit(db.Model):
    # Fruit model with id, name, and color fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # String representation of the Fruit model
        return f'<Fruit {self.name}>'
