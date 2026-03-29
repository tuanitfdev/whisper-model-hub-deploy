FROM alpine:latest
COPY data/models /
CMD ["tail", "-f", "/dev/null"]