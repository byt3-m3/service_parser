import grpc

from configparser import confparse_pb2_grpc, confparse_pb2


class ParserClient:

    def __init__(self, host='localhost', port='50052'):
        # Model Data
        self._line_spec = ""
        self._parent_spec = ""
        self._child_spec = ""
        self._delim = ""
        self._config = ""
        self._caller = __name__

        self._host = host
        self._port = port
        self._status = False
        self._stub = None

    def connect(self):
        chan = grpc.insecure_channel(f'{self._host}:{self._port}')
        try:
            self._stub = confparse_pb2_grpc.ParserStub(chan)
            self._status = True

        except Exception:
            raise

    def find_lines(self, line_spec="", delim="!", config=""):
        if not self._status:
            self.connect()
        # print(config)
        # print()
        Request = confparse_pb2.SingleLineSpec(line_spec=line_spec,
                                               delim=delim,
                                               config=config)

        result = self._stub.find_line(Request)
        return result


if __name__ == "__main__":
    c = ParserClient(host="localhost", port="50052")

    with open("files/config.conf", "rb") as f:
        config_str = f.read(999999).decode("utf-8")

        if isinstance(config_str, str):
            results = c.find_lines(line_spec="interface", config=config_str)

        print(results)

    if results.status == 200:
        print("Successful")
    elif results.status == 417:
        print("Error with database write")
