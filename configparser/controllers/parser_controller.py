from ciscoconfparse import CiscoConfParse


class ParserController:

    def __init__(self, data: dict):
        self._data = data
        pass

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

        return
