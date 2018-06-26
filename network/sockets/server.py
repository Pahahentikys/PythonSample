import socket

from constants import *
from routing import *


def parse_request(request):
    parsed_request = request.split()
    request_method = parsed_request[0]
    request_url = parsed_request[1]
    request_tuple = (request_method, request_url)
    return request_tuple


def set_headers(request_method, request_url):
    if not request_method == "GET":
        return ("HTTP/1.1 405 Method not allowed\n\n", 405)

    if not request_url in REQUEST_URLS:
        return ("HTTP/1.1 404 Not found\n\n", 404)

    return ("HTTP/1.1 200 OK\n\n", 200)


def set_content(response_code, request_url):
    if response_code == 404:
        return "<h1>404 - not found</h1><h2>Page: {} not found!</h2>".format(request_url)
    if response_code == 405:
        return "<h1>405 - method not allowed</h1>"
    # return "<h1>{}</h1>".format(REQUEST_URLS[request_url])
    return REQUEST_URLS[request_url]()


def send_responce(request):
    request_method, request_url = parse_request(request)
    headers, response_code = set_headers(request_method, request_url)
    body = set_content(response_code, request_url)
    return (headers + body).encode()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(BUFFER_SIZE)
        # print(request.decode("utf-8"), "\n")
        print(request, "\n")
        print(client_address)

        response = send_responce(request.decode("utf-8"))

        # client_socket.sendall("It's work with sockets...".encode())
        client_socket.sendall(response)
        client_socket.close()
