#Using socket to create a client that does a request
# GET /aied/pages/login.php HTTP/1.1
# host = 'www.aied.com.br'
import socket

host = "www.aied.com.br"


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,80));

    # Req
    req = "GET /aied/pages/login.php HTTP/1.1\r\n"
    req += "Host: www.aied.com.br\r\n"
    req += "Accept-Encoding: gzip, deflate\r\n"
    req += "Connection: close\r\n"
    req += "\r\n"
    s.send(req.encode())
    
    response = b""
    while True:
        recv = s.recv(1024)
        if not recv: break
        response += recv
    print(response.decode("utf-8"))
    