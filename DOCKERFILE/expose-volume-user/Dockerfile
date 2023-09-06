FROM nginx:1.23.3-alpine

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN addgroup -g 1000 -S paulo \
    && adduser -S -D -H -u 1000 -h /var/cache/nginx -s /sbin/nologin -G paulo -g paulo paulo \
    && chown -R paulo:paulo /var/cache/nginx \
    && chown -R paulo:paulo /var/log/nginx \
    && chown -R paulo:paulo /etc/nginx/conf  .d \
    && touch /var/run/nginx.pid \
    && chown -R paulo:paulo /var/run/nginx.pid

USER paulo

EXPOSE 8010

VOLUME /usr/share/nginx/html