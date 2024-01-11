import unittest
import json
from app import app, db
from app.models import Fruit

class FruitTestCase(unittest.TestCase):

    # Initializes the test client and an in-memory SQLite database
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

            # Add a test fruit
            test_fruit = Fruit(name='Apple', color='Red')
            db.session.add(test_fruit)
            db.session.commit()
            
    # Cleans up the database after each test
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Checks if GET request to /fruits returns a list of fruits
    def test_get_all_fruits(self):
        response = self.app.get('/fruits')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    # Verifies that GET request to /fruits/1 returns the correct fruit
    def test_get_single_fruit(self):
        response = self.app.get('/fruits/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Apple')

    # Tests adding a new fruit using POST request and verifies the response
    def test_add_fruit(self):
        response = self.app.post('/fruits', json={'name': 'Banana', 'color': 'Yellow'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Banana')
        self.assertEqual(data['color'], 'Yellow')

    # Checks the API's handling of invalid POST data
    def test_add_fruit_invalid_payload(self):
        response = self.app.post('/fruits', json={'name': 'Grape'})
        self.assertEqual(response.status_code, 400)

    # Tests DELETE request to remove a fruit
    def test_delete_fruit(self):
        response = self.app.delete('/fruits/1')
        self.assertEqual(response.status_code, 200)

    # Ensures that attempting to delete a fruit that doesn't exist returns a 404 status code
    def test_delete_nonexistent_fruit(self):
        response = self.app.delete('/fruits/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
