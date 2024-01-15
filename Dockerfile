# Use a smaller base image
FROM python:3.11-alpine

# Add a label for pushing to ghcr
LABEL org.opencontainers.image.source=https://github.com/vdribadan/castor

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Install dependencies required for building certain Python packages
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

# Create a new user and group for running the application
RUN addgroup -S castor && adduser -S castor -G castor

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clean up unnecessary files and dependencies
RUN apk del .build-deps

# Change the ownership of files to the non-root user
RUN chown -R castor:castor /usr/src/app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application as the non-root user
USER castor

# Define the command to run the app
CMD ["python", "run.py"]
