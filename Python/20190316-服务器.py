import socket
import sys
HOST='127.0.0.1'
PORT=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('创建成功')
s.bind((HOST,PORT))
print('绑定端口成功')
s.listen(5)
print('开始监听')
while True:
    conn,addr=s.accept()
    print('Connected with '+ addr[0] + ':'+ str(addr[1]))
    t=threading.Thread(tcplink,args=(sock,addr))
    t.start()

def tcplink(sock,addr):
    print('请输入新的连接 %s:%s...' %addr)
    sock.send(b'welcome')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
sock.send(('hello，%s!' %data.decode('utf-8')).encode('utf-8'))
sock.close()
print('Connection from %s:%s closed.' %addr)
