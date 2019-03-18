# Python Web Dockerized Application

## 1. How to run

Build the image using the following command:

`docker build -t my_app:latest .`

Run the Docker container using the command below.

`docker run -p 5000:5000 my_app:latest`

### Running Tests

To run all tests, run:

`pytest tests.py`

## 2. API endpoints

### 2.1 Request to download text

Starts the task which is downloading text from requested URL.
Returns id of the created task.

`GET /api/download/text/<path:url>`

### 2.2 Request to download images

Starts the task which is downloading images from requested URL.
Returns id of the created task.

`GET /api/download/images/<path:url>`

### 2.3 Check task status

Returns the status of the task with the given id.

`GET /api/status/<id>`

### 2.4 Downloading resources

Downloading the requested resources with the given id.

`GET /api/result/<id>`
