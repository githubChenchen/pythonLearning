try:
    f=open('test.txt','w') #open用于打开文件对象
    f.write('这是一个测试文件')
    f.write('\n')
    f.write('用于文件测试异常')
except IOError: #文件打开出错，会包ioerror异常
    print('Error:打开文件失败')
finally:
    print('内容写入成功')
    f.close()  #在finally中关闭文件
fi=open('test.txt','a+')
content=fi.read()#读取文件所有内容
#print('content:',content,end='')
fi.seek(0)#将文件指针移动到文件头部，如果没有这一句，那么后续读取的内容为空
f2=fi.read(8)#读取文件前8个字符
#print(f2)
fi.seek(0)
f3=fi.readline()#读取其中一行内容
f4=fi.readline()
f5=fi.readline()
#print(f3,end='')
#print(f5,end='')
fi.seek(0)
ff=fi.readlines()#读取当前指针之后的所有文件内容，返回由所有行内容组成的列表
#for one in ff:
 #   print(one)
w=['12345','67890']
fi.writelines(w)
fi.seek(0)
f4=fi.read()
print(f4)
print('sddhqihdi')
fi.close
    
