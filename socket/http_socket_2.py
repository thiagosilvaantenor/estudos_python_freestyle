#Using socket to create a client that does a request
# GET / HTTP/1.1
# host: www.universidadegratuitaead.com.br
import socket
host = "www.universidadegratuitaead.com.br";



with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,80));

    # Req
    req = "GET / HTTP/1.1\r\n";
    req += "Host: www.universidadegratuitaead.com.br\r\n";
    req += "Connection: close\r\n";
    req += "\r\n";
    # Socket send the request 
    s.send(req.encode());
    #Response
    response = b"";
    while True:
        recv = s.recv(1024);
        if not recv: break;
        response += recv;
    print(response.decode("utf-8"));
    