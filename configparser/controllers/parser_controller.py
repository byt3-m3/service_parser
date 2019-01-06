from ciscoconfparse import CiscoConfParse


class ParserController:

    def __init__(self, data: dict):
        """
        Controller will be used to preform any Actions received from the API.

        :param data: The keys needed for the model
        """
        self._data = data


    @staticmethod
    def new(config=None, delim=None, line_spec=None, parent_spec=None, child_spec=None):
        """
        Factory to generate new ParserController.

        :param config: Configuration of the node
        :param delim: Comment delimiter
        :param line_spec: Spec used for single line searches
        :param parent_spec: Spec used fro parent/child search
        :param child_spec:S pec used fro parent/child search
        :return ParserController: instance of a ParserController
        """
        if line_spec and parent_spec or line_spec and child_spec:
            raise Exception("Must be either  line_spec or parent_spec/child_spec, not all 3 options")

        if line_spec:
            data = {
                "line_spec": line_spec,
                "delim": delim,
                "config": config
            }
            return ParserController(data)

        if parent_spec or child_spec:
            data = {
                "parent_spec": parent_spec,
                "child_spec": child_spec,
                "delim": delim,
                "config": config
            }
            return ParserController(data)

        return

    @staticmethod
    def _make_parse_obj(config=None, delim=None):
        if isinstance(config, list):
            return CiscoConfParse(config=config, comment=delim)

    def find_lines(self):
        line_spec = self._data.get("line_spec")
        delim = self._data.get("delim")
        config = self._data.get("config")

        parse_obj = self._make_parse_obj(config=config, delim=delim)
        if not parse_obj:
            return

        return parse_obj.find_lines(line_spec)

    def find_blocks(self):
        line_spec = self._data.get("line_spec")
        delim = self._data.get("delim")
        config = self._data.get("config")

        parse_obj = self._make_parse_obj(config=config, delim=delim)
        if not parse_obj:
            return

        return parse_obj.find_blocks(line_spec)

    def find_parents_w_child(self):
        parent_spec = self._data.get("parent_spec")
        child_spec = self._data.get("child_spec")
        delim = self._data.get("delim")
        config = self._data.get("config")

        parse_obj = self._make_parse_obj(config=config, delim=delim)
        if not parse_obj:
            return

        return parse_obj.find_parents_w_child(parent_spec, child_spec)

    def find_parents_wo_child(self):
        parent_spec = self._data.get("parent_spec")
        child_spec = self._data.get("child_spec")
        delim = self._data.get("delim")
        config = self._data.get("config")

        parse_obj = self._make_parse_obj(config=config, delim=delim)
        if not parse_obj:
            return

        return parse_obj.find_parents_wo_child(parent_spec, child_spec)
