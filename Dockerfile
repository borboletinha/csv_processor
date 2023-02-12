FROM python:3.8

RUN pip install tox==3.27.1 uwsgi

WORKDIR /deals

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["./scripts/docker-entrypoint.sh"]