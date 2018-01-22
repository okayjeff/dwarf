status_reason_map = {
    200: 'OK',
    301: 'MOVED PERMANENTLY',
    302: 'FOUND',
    400: 'BAD REQUEST',
    401: 'UNAUTHORIZED',
    403: 'FORBIDDEN',
    405: 'METHOD NOT ALLOWED',
    500: 'INTERNAL SERVER ERROR',
}


class Response(object):
    def __init__(self, status, content, content_type):
        self.status_line = 'HTTP/1.1 {} {}\n'.format(status, status_reason_map[status])
        self.content_type = 'Content-Type: {}\n\n'.format(content_type)
        self.content = content
        self.response = self.status_line + self.content_type + self.content
