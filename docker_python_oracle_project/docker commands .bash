# Step 1: Pull the Python Docker image (using Python 3.10 as an example)
# This will serve as the base image for running the Python application.
docker pull python:3.10

# Step 2: Pull the Oracle XE Docker image (21c slim version for lightweight development)
# This image provides a free Oracle database for testing and development.
docker pull gvenzl/oracle-xe:21-slim

# Step 3: Run the Oracle XE container
# - `--name oracle_db`: Assign a container name for easy identification.
# - `-e ORACLE_PASSWORD=hr`: Set the Oracle password.
# - `-e ORACLE_DATABASE=orclpdb`: Specify the database name.
# - `-p 1521:1521`: Map Oracle's default port (1521) to the host machine.
docker run -d --name oracle_db -e ORACLE_PASSWORD=hr -e ORACLE_DATABASE=orclpdb -p 1521:1521 gvenzl/oracle-xe:21-slim


# Step 4: Check logs of the Oracle container to ensure it's running correctly
# Useful for debugging database startup issues.
docker logs oracle_db

# Step 5: Build the Docker image for the Python application
# - `-t python_oracle_app`: Tag the image as `python_oracle_app` for easy reference.
# - The Dockerfile must be in the current directory when this command is executed.
docker build -t python_oracle_app .

# Step 6: Run the Python application container
# - `--name python_app`: Assign a container name.
# - `--link oracle_db`: Connect the Python container to the Oracle database container.
# - `-v $(pwd):/app`: Mount the current directory to `/app` in the container for code access.
# - `-w /app`: Set `/app` as the working directory.
docker run -d --name python_app --link oracle_db -v C:\Users\Rumi\Desktop\docker_python_oracle_project\app:/app -w /app python_oracle_app


# Step 7: Check logs of the Python application container
# Useful to confirm the application is running and interacting with the database correctly.
docker logs python_app

# Step 8: Verify running containers
# Lists all active containers to ensure both Oracle and Python containers are running.
docker ps

# Step 9: Access the Oracle container interactively (optional)
# Useful for manually inspecting the database or debugging.
docker exec -it oracle_db bash

# Step 10: Access the Python container interactively (optional)
# Useful for running Python commands or debugging application issues.
docker exec -it python_app bash

# Step 11: Stop containers when finished
# Stops both the Oracle and Python containers.
docker stop python_app oracle_db

# Step 12: Remove containers to clean up the environment
# Deletes the stopped Oracle and Python containers.
docker rm python_app oracle_db

# Step 13: Remove the custom Python Docker image (optional)
# Deletes the `python_oracle_app` image if no longer needed.
docker rmi python_oracle_app

# Step 14: Remove unused Docker resources (optional)
# Cleans up unused images, containers, and volumes.
docker system prune -f

# Step 15: View Docker logs in real-time (optional)
# Attach to a running container's logs to monitor output in real-time.
docker logs -f oracle_db
docker logs -f python_app

# Step 16: Restart containers (if needed)
# Restarts previously stopped containers.
docker start python_app oracle_db

# Step 17: Verify container resource usage (optional)
# Check resource consumption for optimization purposes.
docker stats
