#!/usr/bin/env python
# coding: utf-8

# In[11]:


import socket
server=socket.socket( socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.1.75"
port = 1234
server.connect((ip,port))
#print(server.recv(100))
while(True):
    a=input()
    b=str.encode(a)
    server.send(b)


# In[ ]:





# In[ ]:




