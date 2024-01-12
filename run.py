from app import app, db

def initialize_database():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    if not app.config.get('TESTING'):
        initialize_database()
    app.run(debug=True)
