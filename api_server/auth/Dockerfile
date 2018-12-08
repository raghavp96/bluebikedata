FROM python:3.5-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY app.py /
COPY role-*.json /
RUN ls -la

ENTRYPOINT ["python", "app.py"]