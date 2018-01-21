import re
import socket

def foo_func(request):
    return 'HTTP/1.1 200 OK\n\nI am FOO!'

def bar_func(request):
    return 'HTTP/1.1 200 OK\n\nI am BAR!'

HOST, PORT = '', 8888

URLS = {
    '^/foo/?$': foo_func,
    '^/bar/?$': bar_func,
}

def parse_request(req):
    parsed_req = re.search('^([A-Z]{3,6})\s(/[a-zA-Z0-9]+/?)', req)
    if parsed_req:
        for pattern in list(URLS.keys()):
            if re.search(pattern, parsed_req.groups()[1]):
                controller = URLS[pattern]
                return controller(parsed_req)
        return None
    return None

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print('Serving HTTP on port {} ...'.format(PORT))

while True:
    conn, _ = listen_socket.accept()
    request = conn.recv(1024)
    print(request)
    
    res = parse_request(request)
    if not res:
        res = 'HTTP/1.1 404 NOT FOUND\n\nPage not found.'
    
    print(res)

    conn.sendall(res)
    conn.close()
