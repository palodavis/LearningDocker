FROM ubuntu:18.04

WORKDIR /copy

COPY host-file .

WORKDIR /add

ADD add-files.tar.gz .
ADD https://www.docker.com/wp-content/uploads/2022/03/horizontal-logo-monochromatic-white.png .

RUN apt-get update && apt-get install -y \
    net-tools \
    curl \
    nginx \
    && rm -rf /var/lib/apt/lists/*
