import re

from utils.routes import routes


def parse_request(req):
    parsed_req = re.search(r'^([A-Z]{3,6})\s(/[a-zA-Z0-9]+/?)', req)
    if parsed_req and parsed_req.groups()[1] != '/favicon':
        try:
            req_obj = Request(
                path=parsed_req.groups()[1],
                method=parsed_req.groups()[0]
            )

        except KeyError:
            return None  # TODO: Raise 400 bad request

        return req_obj
    return None


class Request(object):

    def __init__(self, path, method, host=None, **kwargs):
        self.path = path
        self.method = method
        self.host = host
        for k, v in kwargs:
            self.k = v

    def get_matched_route_controller(self):
        for pattern in list(routes.keys()):
            if re.search(pattern, self.path):
                controller = routes[pattern]
                return controller
        return None
