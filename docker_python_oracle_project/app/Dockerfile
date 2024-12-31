# Use the official Python image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir cx_Oracle pandas scikit-learn

# Run the Python application
CMD ["python", "main.py"]
