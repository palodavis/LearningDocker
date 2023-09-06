FROM nginx:1.23.3-alpine

HEALTHCHECK --interval=10s --timeout=5s --start-period=15s --retries=2 \
    CMD curl -f https://localhost/

STOPSIGNAL SIGKILL

