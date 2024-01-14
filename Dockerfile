# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Create a new user and group for running the application
RUN groupadd -r castor && useradd -r -g castor castor

# Copy the current directory contents into the container at /usr/src/app
# and change the ownership of these files to the non-root user
COPY --chown=castor:castor . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application as the non-root user
USER castor

# Define the command to run the app
CMD ["python", "run.py"]
