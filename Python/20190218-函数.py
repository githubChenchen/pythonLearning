def func():
    print("I love Python")
func()

def func1(x):
    s=1
    for i in range(x,0,-1):
        s=s*i
    return(s)
print(func1(10))


def square(*num):         #带*号的形参为可变参数，会将参数转化为元组
    print(type(num))
    print(num)
    sum=0
    for i in num:
        sum+=i*i
    return sum
print(square(1,2,3,4))
nums=[4,5,6,7]
#print(square(nums))  不能这样调用
print(square(*nums))    #加上*，将列表解包

def func2(x,y):
    s=x+y
    a=x*y
    b=x**y
    return s,a,b   #return语句可以返回多个值，组合为一个元组
tu=func2(3,4)
print(type(tu))
print(tu)


#Python函数可以嵌套定义

f=lambda x,y,z:x+y+z
x=f(1,2,3)
print(x)
import sys    #导入模块
print(sys.path)  #模块名.方法名（变量名）调用方法或变量

from math import *    #导入模块所有函数
from math import sin  #导入模块中某一个具体的函数
print(sin(30))    #调用时只写函数名，不能写模块名.函数名

import square      #可以导入自定义模块，自定义模块就是一个.py文件
from square import squ
s=squ(3,4)
print(s)
