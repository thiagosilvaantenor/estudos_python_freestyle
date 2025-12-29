import socket;
# Trying to do a modular version of the exercises
# GET /pub/WWW/TheProject.html HTTP/1.1
#       Host: www.w3.org

# SET UP THE CLIENT SOCKET


BASE_HOST = "www.w3.org";

BLOCK = 1024

def handleReq(operation:str, resorce:str):
    url:str = operation.upper() + ' ' + resorce + ' HTTP/1.1\r\n'
    url += 'Host: www.w3.org\r\n'
    url += 'Connection: close\r\n'
    url += '\r\n'
    return url


def setUp(host):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,80))
        url = handleReq(operation='GET', resorce='/pub/WWW/TheProject.html')
        s.send(url.encode())
        response = b''
        while True:
            data = s.recv(BLOCK)
            response += data
            if not data: break
        print(response.decode('utf-8'))

def main():
    setUp(BASE_HOST)


main();