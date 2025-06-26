# Use Python 3.9 base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install dependencies
RUN pip install spyne lxml

# Expose the port (optional, for documentation)
EXPOSE 8000

# Run your SOAP server
CMD ["python", "soap_server.py"]