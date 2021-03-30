#!/bin/bash

mkdir -p database
docker run --name mongodb -v database:/data -p 27017:27017 -dit mongo
