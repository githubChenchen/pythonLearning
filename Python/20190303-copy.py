def copy(s1,s2):
    f1=open(s1)
    txt1=f1.read()
    f1.close()
    f2=open(s2,'w+')
    f2.write(txt1)
    f2.close()
copy('myfile.txt','myfile2.txt')
