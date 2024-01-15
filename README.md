# Fruits API Service

## Overview
The Fruits API Service is a simple Flask-based web application that provides an API for managing a list of fruits. It allows users to add, retrieve, and delete fruit entries. Each fruit has an associated ID, name, and color.

## Features
- **List All Fruits:** Retrieve a list of all fruit entries in the database.
- **Get Specific Fruit:** Fetch details of a specific fruit by ID.
- **Add New Fruit:** Add a new fruit entry to the database.
- **Delete Fruit:** Remove a fruit entry from the database.

## Technology Stack
- **Language:** Python 3.11
- **Framework:** Flask
- **Database:** SQLite
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## Local Setup
1. **Clone the Repository:**
git clone https://github.com/vdribadan/castor.git
cd castor

2. **Set Up a Virtual Environment (Optional):**
python -m venv venv
source venv/bin/activate 

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the Application:**
python run.py

## Using the API
You can interact with the API using a tool like `curl`.

- **List All Fruits:**
curl http://localhost:5000/fruits

- **Get Specific Fruit:**
curl http://localhost:5000/fruits/{id}

- **Add New Fruit:**
curl -X POST http://localhost:5000/fruits -H "Content-Type: application/json" -d '{"name": "Cherry", "color": "Red"}'

- **Delete Fruit:**
curl -X DELETE http://localhost:5000/fruits/{id}

## Running with Docker
To run the application in a Docker container, follow these steps:

1. **Build the Docker Image:**
docker build -t fruits-api .

2. **Run the Container:**
docker run -d -p 5000:5000 fruits-api

## Testing
To run the automated tests:

python -m unittest discover tests


## Continuous Integration and Deployment
This project is configured with GitHub Actions for continuous integration and deployment. Upon each push or pull request to the `main` branch, the CI workflow runs automated tests, builds the Docker image, and pushes it to the GitHub Container Registry.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by Maksims Koskins



