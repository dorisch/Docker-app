FROM python:3.7-slim

FROM python
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "-u", "app.py"]