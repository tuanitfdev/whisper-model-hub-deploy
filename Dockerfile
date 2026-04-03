FROM alpine:latest
COPY data/models /data/models
COPY data/cacheTorchHub /data/cacheTorchHub
COPY data/whl /data/whl
CMD ["tail", "-f", "/dev/null"]
