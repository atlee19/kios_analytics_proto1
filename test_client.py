import socket 

host = "0.0.0.0"
port = 8000

#creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client 
client.connect((host, port))

#send some data 
client.send(b"GET / HTTP/1.1\r\nHost: hello\r\n\r\n")
#what is the post??

response = client.recv(4096)

print("REPLY:".format(response))