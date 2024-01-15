# Fruits API Service

## Overview
The Fruits API Service is a simple Flask-based web application that provides an API for managing a list of fruits. It allows users to create, retrieve, update and delete fruit entries. Each fruit has an associated ID, name, and color.

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

  ***Example:***
  This example retrieves the fruit with ID 1

  ```bash
   curl http://localhost:5000/fruits/1
  ```

- **Add New Fruit:**
curl -X POST http://localhost:5000/fruits -H "Content-Type: application/json" -d '{"name": "Cherry", "color": "Red"}'

- **Delete Fruit:**
curl -X DELETE http://localhost:5000/fruits/{id}

  ***Example:***
  This example deletes the fruit with ID 1

  ```bash
   curl -X DELETE http://localhost:5000/fruits/1
  ```

- **Update Fruit Name and/or Color:**
  curl -X PUT http://localhost:5000/fruits/{id} -H "Content-Type: application/json" -d '{"name": "New Fruit", "color": "New Color"}'

  ***Example:***
  This example updates the fruit with ID 1 to have the name "Grape" and the color "Green"

  ```bash
   curl -X PUT http://localhost:5000/fruits/1 \
   -H "Content-Type: application/json" \
   -d '{"name": "Grape", "color": "Green"}'
  ```


## Running with Docker
To run the application in a Docker container, follow these steps:

1. **Build the Docker Image:**
docker build -t fruits-api .

2. **Run the Container:**
docker run -d -p 5000:5000 fruits-api

## Testing
**To run the automated tests:**

python -m unittest discover tests


## Continuous Integration and Deployment (CI/CD)

### Overview
This project implements a CI/CD pipeline using GitHub Actions, which automates the testing, building, and deployment of the application. The pipeline is triggered on push events to the `main` branch and on the creation of pull requests against `main`.

### Workflow Details

1. **Automated Testing:**  
   Upon every push or pull request to `main`, the pipeline automatically runs the unit tests defined in the `tests` directory. These tests ensure that new changes do not break existing functionality. If any test fails, the pipeline stops, preventing the integration of failing code.

2. **Docker Image Building:**  
   If all tests pass, the pipeline proceeds to build a Docker image for the application. This image encapsulates the application and its environment, ensuring consistent behavior across different setups.

3. **Multi-Platform Support:**  
   The Docker image is built for multiple platforms, including `linux/amd64` and `linux/arm64`, ensuring compatibility with different types of infrastructure.

4. **Docker Image Publishing:**  
   After the image is built, it's automatically pushed to the GitHub Container Registry (GHCR). This makes the image readily available for deployment. The image is tagged with the `latest` tag for easy reference.

5. **Security and Best Practices:**  
   The pipeline uses `secrets.GITHUB_TOKEN` for authentication with GHCR, ensuring security and adherence to best practices.

### Local Testing and Deployment

Developers can test and deploy the application locally following the instructions in the [Local Setup](#local-setup) and [Running with Docker](#running-with-docker) sections. This includes steps for running the application and Docker commands for building and running the container.

### Notes

- The workflow configuration can be found in the `.github/workflows` directory of the repository.
- The Dockerfile used for building the image is located at the root of the repository.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by Maksims Koskins



