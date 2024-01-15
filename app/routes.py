from flask import Blueprint, request, jsonify, abort
from app.models import Fruit
from app import db

# Create a Blueprint for API endpoints
api = Blueprint('api', __name__)

# List all fruits
@api.route('/fruits', methods=['GET'])
def get_fruits():
    fruits = Fruit.query.all()
    fruits_data = [{"id": fruit.id, "name": fruit.name, "color": fruit.color} for fruit in fruits]
    return jsonify(fruits_data)

# Get a specific fruit by ID
@api.route('/fruits/<int:id>', methods=['GET'])
def get_fruit(id):
    fruit = Fruit.query.get_or_404(id)
    return jsonify({"id": fruit.id, "name": fruit.name, "color": fruit.color})

# Add a new fruit
@api.route('/fruits', methods=['POST'])
def add_fruit():
    data = request.get_json()
    if not data or 'name' not in data or 'color' not in data:
        abort(400, description="Invalid data. Name and color are required.")
    new_fruit = Fruit(name=data['name'], color=data['color'])
    db.session.add(new_fruit)
    db.session.commit()
    return jsonify({"id": new_fruit.id, "name": new_fruit.name, "color": new_fruit.color}), 201

# Delete a fruit by ID
@api.route('/fruits/<int:id>', methods=['DELETE'])
def delete_fruit(id):
    fruit = Fruit.query.get_or_404(id)
    db.session.delete(fruit)
    db.session.commit()
    return jsonify({"message": "Fruit deleted successfully"}), 200

# Error Handlers
@api.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@api.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400
