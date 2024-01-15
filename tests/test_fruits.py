import unittest
import json
from app import create_app, db
from app.models import Fruit

class FruitTestCase(unittest.TestCase):

    # Set up test application context and test client
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    # Clean up database after each test
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # Helper method to add a fruit to the database
    def add_fruit(self, name='Apple', color='Red'):
        with self.app.app_context():
            fruit = Fruit(name=name, color=color)
            db.session.add(fruit)
            db.session.commit()
            return fruit.id

    # Test retrieving all fruits
    def test_get_all_fruits(self):
        self.add_fruit()
        response = self.client.get('/fruits')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    # Test retrieving a single fruit by ID
    def test_get_single_fruit(self):
        fruit_id = self.add_fruit()
        response = self.client.get(f'/fruits/{fruit_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Apple')
        self.assertEqual(data['color'], 'Red')

    # Test adding a new fruit
    def test_add_fruit(self):
        response = self.client.post('/fruits', json={'name': 'Banana', 'color': 'Yellow'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Banana')
        self.assertEqual(data['color'], 'Yellow')

    # Test adding a fruit with invalid payload
    def test_add_fruit_invalid_payload(self):
        response = self.client.post('/fruits', json={'name': 'Grape'})
        self.assertEqual(response.status_code, 400)

    # Test deleting a fruit
    def test_delete_fruit(self):
        fruit_id = self.add_fruit()
        response = self.client.delete(f'/fruits/{fruit_id}')
        self.assertEqual(response.status_code, 200)

    # Test deleting a nonexistent fruit
    def test_delete_nonexistent_fruit(self):
        response = self.client.delete('/fruits/999')
        self.assertEqual(response.status_code, 404)
    
    # Test updating a fruit
    def test_update_fruit(self):
        fruit_id = self.add_fruit()
        response = self.client.put(f'/fruits/{fruit_id}', json={'name': 'Updated Apple', 'color': 'Green'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Updated Apple')
        self.assertEqual(data['color'], 'Green')
        # Verify that the update is reflected in the database
        with self.app.app_context():
            updated_fruit = Fruit.query.get(fruit_id)
            self.assertEqual(updated_fruit.name, 'Updated Apple')
            self.assertEqual(updated_fruit.color, 'Green')

if __name__ == '__main__':
    unittest.main()
