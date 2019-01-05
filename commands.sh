#!/usr/bin/env bash
python -m grpc_tools.protoc -I=protos/ --python_out=configparser/ --grpc_python_out=configparser/ protos/configparser.proto
