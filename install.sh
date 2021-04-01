#!/bin/bash


docker_name=4x4_trips


# Cleanup
docker rm -f ${docker_name}


# Set up
mkdir -p db requests/.handled


# Build it
docker build . -t ${docker_name}_image


# Run it.
docker run --name ${docker_name} \
   -v "$(pwd)/db:/opt/${docker_name}/db" \
   -v "$(pwd)/requests:/opt/${docker_name}/requests" \
   -dit ${docker_name}_image
