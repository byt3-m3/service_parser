from ciscoconfparse import CiscoConfParse

from configparser import confparse_pb2_grpc, confparse_pb2
from configparser.controllers.parser_controller import ParserController


class Parser(confparse_pb2_grpc.ParserServicer):

    def find_line(self, request, context):
        line_spec = request.line_spec
        delim = request.delim
        config = request.config
        if config:
            config = request.config.split("\r\n")

        if len(config) == 0:
            return confparse_pb2.Response(status=417, msg="Config Not Provided")
        pc = ParserController({
            "line_spec": line_spec,
            "delim": delim,
            "config": config
        })

        results = pc.find_lines()
        if results:
            return confparse_pb2.Response(data=str(results),
                                          msg="Successful",
                                          status=200)

        return confparse_pb2.Response(status=400, msg="Fatal Error Encountered")

    def find_blocks(self, request, context):
        pass

    def find_parents_w_child(self, request, context):
        pass

    def find_parents_wo_child(self, request, context):
        pass
