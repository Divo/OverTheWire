#!/usr/bin/python
import socket
import struct

HOST = 'vortex.labs.overthewire.org'
PORT = 5842

#Because this is old school type C networking we need to convert all the datums

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#Calc size to read in, never ever ever hardcode this. Ever
len_uint = struct.calcsize('I')
#Clever trick to fill array
data = [s.recv(len_uint) for i in range(4)]
# (< little endian, Which is native order for x86_64), (4 byte) (Unsigned int)
result = sum(struct.unpack('<4I',''.join(data)))

#Pack the response
s.send(struct.pack('<Q', result))

print s.recv(1024)

s.close()



