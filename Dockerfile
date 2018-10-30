# Use an official Python runtime as a parent image
FROM python:3-slim

RUN apt-get update && apt-get install -y libpq-dev

# create folder
RUN mkdir /application

# Set the working directory to /app
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY . /application

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "server_app/run.py"]
