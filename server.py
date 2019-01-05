import time
from concurrent import futures

import grpc

from configparser import Parser
from configparser import confparse_pb2_grpc

DAY = 60 * 60 * 24

parser = Parser()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    confparse_pb2_grpc.add_ParserServicer_to_server(parser, server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            print("Server Started on port 50052")
            time.sleep(DAY)
    except KeyboardInterrupt:
        server.stop(0)


serve()