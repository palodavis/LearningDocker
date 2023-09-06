FROM nginx:1.23.3-alpine

ONBUILD WORKDIR /usr/share/nginx/html
ONBUILD COPY index.html .
ONBUILD RUN date +"%T" >> index.html
