import grpc

from configparser import confparse_pb2_grpc, confparse_pb2


class ParserClient:

    def __init__(self, host='localhost', port='50052'):
        # Model Data
        self._line_spec = ""
        self._parent_spec = ""
        self._child_spec = ""
        self._delim = ""
        self._config = None
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

    def find_lines(self, line_spec="", delim="!"):
        if not self._status:
            self.connect()

        self._validate_config()

        request = confparse_pb2.SingleLineSpec(line_spec=line_spec,
                                               delim=delim,
                                               config=self._config)

        result = self._stub.find_line(request)
        return result

    def find_blocks(self, line_spec="", delim="!"):
        if not self._status:
            self.connect()

        self._validate_config()

        request = confparse_pb2.SingleLineSpec(line_spec=line_spec,
                                               delim=delim,
                                               config=self._config)

        result = self._stub.find_blocks(request)
        return result

    def find_parents_w_child(self, parent_spec="", child_spec="", delim="!"):
        if not self._status:
            self.connect()

        self._validate_config()

        request = confparse_pb2.MultiLineSpec(parent_spec=parent_spec,
                                              child_spec=child_spec,
                                              delim=delim,
                                              config=self._config)

        result = self._stub.find_parents_w_child(request)
        return result

    def find_parents_wo_child(self, parent_spec="", child_spec="", delim="!"):
        if not self._status:
            self.connect()

        self._validate_config()

        request = confparse_pb2.MultiLineSpec(parent_spec=parent_spec,
                                              child_spec=child_spec,
                                              delim=delim,
                                              config=self._config)

        result = self._stub.find_parents_wo_child(request)
        return result

    def load_config(self, config_file):
        with open(config_file, "rb") as f:
            _config_str = f.read(999999).decode("utf-8")
            if isinstance(_config_str, str):
                self._config = _config_str
                return _config_str

    def _validate_config(self):
        if self._config is None:
            raise Exception(
                "No Configuration loaded, Use ParseClient.load_config(config_file) to load config from Disk")

        return True


