# rfcomm_server.py
#receive

from bluetooth import *

server_socket = BluetoothSocket( RFCOMM )

server_socket.bind(("",1))
server_socket.listen(1)

client_socket,address = server_socket.accept()

data = client_socket.recv(1024)
results = int(data)
print("received [%s]" % results)

client_socket.close()
server_socket.close()
