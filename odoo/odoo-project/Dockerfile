# Select a base image (adjust based on Odoo version)
FROM odoo:16.0

# Switch to root user to install dependencies
USER root

# Install additional dependencies if needed (example)
RUN apt-get update && apt-get install -y python3-pip
# If there are no specific pip packages to install, comment out or remove the next line
# RUN pip3 install some-dependency

# Copy your custom modules
COPY custom_modules/ /mnt/extra-addons/

# Switch back to the odoo user
USER odoo
