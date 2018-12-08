FROM python:3.5-alpine

ENV AUTH_SVC_URL "http://auth_svc:8080/"

RUN apk add -U --no-cache gcc build-base linux-headers ca-certificates \ 
                          python3 python3-dev libffi-dev libressl-dev

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY *.py /

RUN ls -la

ENTRYPOINT ["python", "app.py"]