FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /eventManagement

# Copy the requirements file and install dependencies
COPY requirements.txt /eventManagement/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /eventManagement/

# Copy the custom script into the container
COPY entrypoint.sh /eventManagement/entrypoint.sh

# Give execute permissions to the script
RUN chmod +x /code/entrypoint.sh

# Expose the port on which your Django app runs (e.g., 8000)
EXPOSE 8000

# Define the command to run your Django app using the custom script
CMD ["/eventManagement/entrypoint.sh"]

