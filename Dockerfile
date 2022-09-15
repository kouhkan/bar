FROM python:3.10
ENV PYTHONUNBUFFERD=1
WORKDIR /django
COPY requirements/ requirements/
RUN pip install -U pip
RUN pip install -r requirements/prod.txt
COPY . .
