#!/usr/bin/env python
# coding: utf-8

# In[8]:


import socket
server=socket.socket()
ip="192.168.1.75"
port = 2222
server.connect((ip,port))
c=(server.recv(100))
print(c.decode())
while(True):
    a=input()
    b=str.encode(a)
    server.send(b)


# In[ ]:




