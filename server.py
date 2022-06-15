import socket

server_ip = '127.0.0.1'
port = 9999

server = socket.socket()

server.bind((server_ip, port))
server.listen(1)
print('Listening...')

client, adder = server.accept()
print('---Client has connected---')

msg = client.recv(1024)
print('---Received a message---')
print(msg)

client.send(b'Hi I\'m server, welcome: ' + msg)
print('---Sent a message---')

client.close()
server.close()