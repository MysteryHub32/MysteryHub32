import socket

server_ip = '127.0.0.1'
port = 9999

client = socket.socket()

client.connect((server_ip, port))
print('---Connected to server---')

print("type your name: ")
msg = input()

client.send(bytes(msg, 'utf-8'))
print('---Sent a message---')

msg = client.recv(1024)
print('---Got a message---')
print(msg)

client.close()
