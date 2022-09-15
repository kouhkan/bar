FROM python:3.10-slim-stretch

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

COPY ./requirements /requirements

RUN pip install --no-cache-dir -r requirements/local.txt

COPY . .

ENTRYPOINT ["/entrypoint.sh"]