# rfcomm_client.py
#send
# sudo rfcomm help
from bluetooth import *

#create client socket
client_socket=BluetoothSocket( RFCOMM )
addr = "B8:27:EB:DF:04:DF"
port = 1

client_socket.connect((addr,port))
data = ('100')
client_socket.send( data )

print("fin")

client_socket.close()


