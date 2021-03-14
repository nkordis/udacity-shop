#!/bin/bash -eu

set -e

# TODO: Add the commands to generate the gRPC files
python -m grpc_tools.protoc -I../../pb --python_out=./ --grpc_python_out=./ demo.proto
python -m grpc_tools.protoc -I../../pb/grpc/health/v1 --python_out=./ --grpc_python_out=./ health.proto