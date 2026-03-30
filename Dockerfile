FROM alpine:latest
COPY data/models /models
CMD ["tail", "-f", "/dev/null"]