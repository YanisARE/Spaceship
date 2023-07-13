# Use an official Python runtime as a parent image
FROM python:3.10.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Add wait-for-it script
ADD wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

CMD ["/wait-for-it.sh", "db:5432", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
