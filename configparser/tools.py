from configparser import confparse_pb2


def make_response(data=None, msg=None, status=None):
    """Used to generate Response objects for the API."""
    return confparse_pb2.Response(data=data, msg=msg, status=status)


def prep_config(config):
    """
    Used to normalize config data for operation.

    :param config:
    :return:
    """
    if config:
        return config.split("\r\n")

    return
