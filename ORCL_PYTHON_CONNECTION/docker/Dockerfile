# Use official Python 3.13 image
FROM python:3.13

# Set working directory in the container
WORKDIR /app

# Install system dependencies and Oracle Instant Client
RUN apt-get update && apt-get install -y libaio1 wget unzip && wget https://download.oracle.com/otn_software/linux/instantclient/1925000/instantclient-basic-linux.x64-19.25.0.0.0dbru.zip && unzip instantclient-basic-linux.x64-19.25.0.0.0dbru.zip && mkdir -p /opt/oracle && mv instantclient_* /opt/oracle/instantclient && echo /opt/oracle/instantclient > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig && rm -rf /var/lib/apt/lists/* instantclient-basic-linux.x64-19.25.0.0.0dbru.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Set environment variables for Oracle Instant Client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV PATH="$PATH:/opt/oracle/instantclient"

# Default command to run the script
CMD ["/usr/local/bin/python3", "src/insert_dummy_data.py"]
