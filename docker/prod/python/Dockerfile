FROM python:3.10
ENV PYTHONUNBUFFERD=1

WORKDIR /app

COPY requirements/ requirements/
RUN pip install -U pip
RUN pip install -r requirements/prod.txt

COPY . .

EXPOSE 8000


COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
