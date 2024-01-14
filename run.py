from app import create_app, db
from app.models import Fruit

app = create_app('default')

def initialize_database():
    with app.app_context():
        db.create_all()
        # Check if the fruits table is empty
        if Fruit.query.count() == 0:
            # Add some default fruits
            default_fruits = [
                Fruit(name="Apple", color="Red"),
                Fruit(name="Banana", color="Yellow"),
                Fruit(name="Orange", color="Orange")
            ]
            db.session.bulk_save_objects(default_fruits)
            db.session.commit()

if __name__ == "__main__":
    if not app.config.get('TESTING'):
        initialize_database()
    app.run(host='0.0.0.0', port=5000, debug=True)

