#!/bin/bash


docker_name=4x4_trips


# Cleanup
docker rm -f ${docker_name}


# Set up
mkdir -p db requests/.handled

cat <<EOF > run_me.sh
#!/bin/sh
cd src
python3 4x4_trips.py
EOF


# Build it
docker build . -t ${docker_name}_image


# Run it.
docker run --name ${docker_name} \
   -v "$(pwd)/db:/opt/${docker_name}/db" \
   -v "$(pwd)/config:/opt/${docker_name}/config" \
   -v "$(pwd)/requests:/opt/${docker_name}/requests" \
   -dit ${docker_name}_image


# Clean-up
rm -f run_me.sh