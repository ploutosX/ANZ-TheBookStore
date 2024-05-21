#!/bin/bash

# Retrieve app version, commit SHA, and timestamp
APP_VERSION=$(git describe --tags 2>/dev/null)
COMMIT_SHA=$(git rev-parse HEAD)
TIMESTAMP=$(date +"%Y-%m-%dT%H:%M:%S%z")

# Build Docker image
docker build . \
    -t the-book-store:${APP_VERSION:-latest} \
    -t the-book-store:${APP_VERSION:-latest} \
    --build-arg COMMIT_SHA=${COMMIT_SHA} \
    --build-arg TIMESTAMP=${TIMESTAMP}