
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

COPY src/ app/

WORKDIR /app
# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install google-cloud-firestore
RUN pip install gunicorn

ENV PORT 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app