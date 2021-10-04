FROM python:3.9.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install -r requirements.txt