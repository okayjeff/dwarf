import socket

from utils.request import parse_request


def start_server(host='', port=8888):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print('Serving HTTP on port {} ...'.format(port))
    return s


def run():
    server = start_server()

    while True:
        conn, _ = server.accept()
        request = conn.recv(1024)
        print(request)
        
        req = parse_request(request)
        if not req:
            resp = 'HTTP/1.1 404 NOT FOUND\n\nPage not found.'
            conn.sendall(resp)

        controller = req.get_matched_route_controller()
        resp = controller(request)

        print(resp)
        conn.sendall(resp)
        conn.close()


if __name__ == '__main__':
    run()
