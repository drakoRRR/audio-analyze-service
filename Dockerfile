FROM --platform=linux/amd64 python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    openssl-dev \
    make \
    py3-pip \
    python3-dev \
    libxml2-dev \
    libxslt-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader all

COPY . ./

EXPOSE 8080