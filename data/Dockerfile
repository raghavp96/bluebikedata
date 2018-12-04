FROM python:3.5-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY uploads/* /uploads/
COPY *.py /

ENTRYPOINT ["python", "app.py"]