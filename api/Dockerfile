FROM python:3.5-alpine

RUN apk add -U --no-cache gcc build-base linux-headers ca-certificates \ 
                          python3 python3-dev libffi-dev libressl-dev

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY app.py /
COPY db.py /

RUN ls -la

ENTRYPOINT ["python", "app.py"]