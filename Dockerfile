# Instead of creating an image from scratch, we use this image which has python installed.
FROM python:3.10.6-buster

# COPY allows you to select the folders and files to include in your docker image
COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY models models

# RUN allows you to run terminal commands when your image gets created
# Here, we upgrade pip and install the libraries in our requirements.txt
RUN pip install --upgrade pip
RUN pip install -e .

# CMD controls the functionality of the container
# Here, we use uvicorn to control the web server ports

# local
CMD uvicorn package_folder.api_backend:api --host 0.0.0.0

# deploy to gcp
#CMD uvicorn package_folder.api_backend:api --host 0.0.0.0 --port $PORT
