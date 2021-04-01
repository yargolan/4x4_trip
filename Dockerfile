FROM alpine:3.13.4

RUN apk add --no-cache sqlite python3 bash

WORKDIR /opt/4x4_trips

RUN mkdir -p db requests

COPY src/* .

ENTRYPOINT ["python3", "4x4_trips.py"]
