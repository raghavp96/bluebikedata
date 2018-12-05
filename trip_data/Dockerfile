FROM python:3.5-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /uploads
COPY *.py /

ENTRYPOINT ["python", "app.py"]