import http.client
#USING default lib to do a request
host = "www.google.com.br"
conn = http.client.HTTPConnection(host)
conn.request("GET", "/3/", headers={"Host": host})
response = conn.getresponse()
print(response.status, response.reason)