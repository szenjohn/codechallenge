# Use a base image with Python installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire repository contents to the container
COPY . .

# Set environment variables if needed
# ENV VARIABLE_NAME=value

# Expose the port your app runs on
EXPOSE 5000

# Specify the command to run your application
CMD ["python", "robot.py"]
