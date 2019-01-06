import logging

from configparser import confparse_pb2_grpc, confparse_pb2
from configparser.controllers.parser_controller import ParserController
from .tools import make_response, prep_config


class Parser(confparse_pb2_grpc.ParserServicer):
    """
    Server implementation of the Parser rpc model.

    """

    def find_line(self, request, context):
        """
        This method is the equivalent of a simple configuration grep (Case-sensitive).


        :param request:
        :param context:
        :return:
        """

        # TODO Extracts data from request.
        line_spec = request.line_spec
        delim = request.delim
        config = prep_config(request.config)

        if not config:
            return make_response(status=417, msg="Config Not Provided")

        pc = ParserController.new(config=config, delim=delim, line_spec=line_spec)

        results = pc.find_lines()

        return self._proc_result(results, self.find_line.__name__)

    def find_blocks(self, request, context):
        """
        Find all siblings matching the linespec, then find all parents of those siblings. Return a list of config lines
        sorted by line number, lowest first. Note: any children of the siblings should NOT be returned.

        :param request:
        :param context:
        :return:
        """
        # TODO Extracts data from request.
        line_spec = request.line_spec
        delim = request.delim
        config = prep_config(request.config)

        if not config:
            return make_response(status=417, msg="Config Not Provided")

        pc = ParserController.new(config=config, delim=delim, line_spec=line_spec)

        results = pc.find_lines()

        return self._proc_result(results, self.find_blocks.__name__)

    def find_parents_w_child(self, request, context):
        """
        Parse through all children matching childspec, and return a list of parents that matched the parentspec.
         Only the parent lines will be returned.

        :param request:
        :param context:
        :return:
        """
        # TODO Extracts data from request.
        parent_spec = request.parent_spec
        child_spec = request.child_spec
        delim = request.delim
        config = prep_config(request.config)

        if not config:
            return make_response(status=417, msg="Config Not Provided")

        pc = ParserController.new(config=config, delim=delim, parent_spec=parent_spec, child_spec=child_spec)

        results = pc.find_parents_w_child()

        return self._proc_result(results, self.find_parents_w_child.__name__)

    def find_parents_wo_child(self, request, context):
        """
        Parse through all parents matching parentspec, and return a list of parents that did NOT have children match the
         childspec. For simplicity, this method only finds oldest_ancestors without immediate children that match.

        :param request:
        :param context:
        :return:
        """
        # TODO Extracts data from request.
        parent_spec = request.parent_spec
        child_spec = request.child_spec
        delim = request.delim
        config = prep_config(request.config)
        if not config:
            logging.error("Config Not Provided")
            return make_response(status=417, msg="Config Not Provided")

        pc = ParserController.new(config=config, delim=delim, parent_spec=parent_spec, child_spec=child_spec)

        results = pc.find_parents_wo_child()

        return self._proc_result(results, self.find_parents_wo_child.__name__)

    @staticmethod
    def _proc_result(results, func):
        if results:
            logging.info(f"{func} -- Successful")
            return make_response(data=str(results), msg="Successful", status=200)

        logging.error(f"{func} -- Fatal Error Encountered")
        return make_response(data=None, msg="Fatal Error Encountered", status=400)
