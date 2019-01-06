#!/usr/bin/env bash

# Builds Development environment need to run service, no source files are present.
docker build -f dockerfiles/dev.Dockerfile -t cbaxter1988/service_confparser:dev .


# Builds Test environment for service, Source files are copied to the container and executed.
docker build -f dockerfiles/build.Dockerfile -t cbaxter1988/service_confparser:test .


# Runs the docker service
 docker run --rm -p 50052:50052 cbaxter1988/service_confparser:test