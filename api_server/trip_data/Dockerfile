FROM python:3.5-alpine

ENV API_SVC_URL "http://api-svc:8001/"

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /uploads
COPY *.py /

ENTRYPOINT ["python", "app.py"]