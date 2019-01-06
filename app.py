import logging
import os
import time
from concurrent import futures

import grpc

from configparser import Parser
from configparser.protobufs import confparse_pb2_grpc

parser = Parser()
format = "MSG: %(message)s == LEVEL: %(levelname)s == TIME: %(asctime)s == Logger: %(name)s"

logging.basicConfig(level=logging.DEBUG, format=format)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    confparse_pb2_grpc.add_ParserServicer_to_server(parser, server)
    app_port = os.getenv("APP_PORT", "50052")

    logging.info(f'Starting server. Listening on port {app_port}')
    server.add_insecure_port(f'[::]:{app_port}')
    server.start()
    try:
        while True:
            time.sleep(float(os.getenv("APP_TIMEOUT", "86400")))

    except KeyboardInterrupt:
        logging.info(f'Stopping server on port {app_port}')
        server.stop(0)


serve()
