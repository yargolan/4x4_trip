FROM alpine:3.13.4

RUN apk add --no-cache sqlite python3 bash

WORKDIR /opt/4x4_trips

RUN mkdir -p db requests

COPY run_me.sh .

COPY src src

ENTRYPOINT ["/bin/bash", "-C", "./run_me.sh"]
# ENTRYPOINT ["/bin/bash"]
