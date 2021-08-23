#!/usr/bin/env bash
TAG=${TAG:-latest}
DEFAULT_IMAGE=$"rtree-bench":$TAG
IMAGE=${IMAGE:-$DEFAULT_IMAGE}

# --net=host is required to reach the prediction-api
docker run -ti $IMAGE "$@"