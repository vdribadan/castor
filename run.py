from app import app
from db_init import initialize_database

if __name__ == "__main__":
    initialize_database()  # Ensure DB is set up
    app.run(debug=True)
