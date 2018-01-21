import re
import socket


# Controllers
def foo_func(request):
    return 'HTTP/1.1 200 OK\n\nI am FOO!'


def bar_func(request):
    return 'HTTP/1.1 200 OK\n\nI am BAR!'


# URL patterns
urls = {
    '^/foo/?$': foo_func,
    '^/bar/?$': bar_func,
}


# Request handling
def parse_request(req):
    parsed_req = re.search('^([A-Z]{3,6})\s(/[a-zA-Z0-9]+/?)', req)
    if parsed_req:
        for pattern in list(urls.keys()):
            if re.search(pattern, parsed_req.groups()[1]):
                controller = urls[pattern]
                return controller(parsed_req)
        return None
    return None


def start_server(host='', port=8888):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print('Serving HTTP on port {} ...'.format(port))
    return s


def run():
    server = start_server();

    while True:
        conn, _ = server.accept()
        request = conn.recv(1024)
        print(request)
        
        res = parse_request(request)
        if not res:
            res = 'HTTP/1.1 404 NOT FOUND\n\nPage not found.'
        
        print(res)
        conn.sendall(res)
        conn.close()


if __name__ == '__main__':
    run()
