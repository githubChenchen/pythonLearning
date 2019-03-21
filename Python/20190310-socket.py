import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5000)) #连接端口ip
s.send(b'GET/HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection:close\r\n\r\n')#发送数据
buf=[]
while True:
    d=s.recv(1024)#接收来自服务端的信息
    if d:
        buf.append(d)
    else:
        break
data=b''.join(buf)
s.close()
header,html=data.split((b'\r\n\r\n'),1)
print(header.decode('utf-8'))
with open('baidu.html','wb') as b:
    b.write(html)
