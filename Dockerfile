# Select a base image (adjust based on Odoo version)
FROM odoo:16.0

# Install additional dependencies if needed (example)
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install some-dependency

# Copy your custom modules (replace 'custom_modules' with your directory)
COPY custom_modules/ ./
