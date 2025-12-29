#USING SOCKET to create a cliente to do a request to this server:
# GET /pub/WWW/TheProject.html HTTP/1.1
#Host: www.w3.org
import socket

host = "www.w3.org"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,80));

    # Req
    req = "GET /pub/WWW/TheProject.html HTTP/1.1\r\n"
    req += "Host: www.w3.org\r\n"
    req += "Connection: close\r\n"
    req += "\r\n"
    s.send(req.encode())
    #Response
    response = b""
    while True:
        recv = s.recv(1024)
        if not recv: break
        response += recv
    print(response.decode("utf-8"))
    