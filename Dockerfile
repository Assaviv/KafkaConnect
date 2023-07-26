# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Install the Python dependencies
RUN pip install --no-cache-dir confluent-kafka faker kafka-python

# Setting up connector
ADD utils /usr/local/bin
RUN chmod +x /usr/local/bin/cx
RUN chmod +x /usr/local/bin/status

RUN apt-get -y update
RUN apt-get install -y jq
RUN apt-get install -y curl
RUN apt-get install -y dos2unix

RUN dos2unix /usr/local/bin/*

# Copy the current directory contents into the container at /app
COPY . /app

# Setup Kafka Connect With Mongo
RUN cx simplesink.json
RUN status

# Set the command to run your Python script
CMD ["python", "main.py"]
