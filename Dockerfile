FROM python:3.8

RUN apt -y update && \
    apt install -y gcc python3-dev libpq-dev python3-dev postgresql-client

RUN pip install tox==3.27.1 uwsgi

WORKDIR /deals

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["./scripts/docker-entrypoint.sh"]