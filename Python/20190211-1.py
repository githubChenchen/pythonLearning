'''
x=eval(input("第一个数字："))
y=eval(input("第二个数字："))
if x>y:
    print("较大得是：",x)
elif x<y:
    print("较大得是：",y)
else:
    print("两个数字相等")
'''

'''
socer=eval(input("分数为："))
if socer>90:
    gpa=4
elif socer>=80:
    gpa=3
elif socer>=70:
    gpa=2
elif socer>=60:
    gpa=1
else:
    gpa=0
print("学分绩点为：",gpa)
'''

'''
s=0
for i in range(1,101,2):

    s=s+i
else:
    print("计算完毕！")
print("1到100的奇数和为：",s)

'''
'''
       # range函数产生某范围内整数，三种情况：
       #     1.range(5)表示0到5之间的整数，包括0不包括5，【0,4】
       #     2.range(3,7)------[3,6]
       #     3.range(5,12,2)第三个参数表示步长，【5,7,9,11】
'''
'''
from random import randint
n=randint(10,100)
print("价格已经产生，请输入数字")
x=eval(input("请输入价格："))
while x!=n:
    if x>n:
        print("猜错了，再小一点")
        x=eval(input("请输入价格："))
    elif x<n:
        print("猜错了，再大一点")
        x=eval(input("请输入价格："))
else:
    print("恭喜你，猜对了！")
#randint(m,n)函数产生【m,n】之间的随机整数
'''

'''
for x in range(21):
    for y in range(34):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print("公鸡：",x,"母鸡：",y,"小鸡：",z)
else:
    print("计算完毕！")
'''

'''
x=eval(input("第一个数字："))
y=eval(input("第二个数字："))
if x<y:
    x,y=y,x
for i in range(x,x*y+1):
    if i%x==0 and i%y==0:
        print("最小公倍数为：",i)
        break
else:
    print("计算完毕！")
'''

'''
s,n=0,0
for i in range(1,11):
    socer=eval(input("请输入分数："))
    if socer<60:
        continue
    else:
        s=s+socer
        n=n+1
else:
    print("输入完毕！")
print("及格人数为：",n)
print("平均分为：",round(s/n,2))
'''
'''
for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i,end=' ')
else:
    print("计算完毕！")
'''

'''
from time import sleep
n=eval(input("请输入一个奇数"))
if n%2!=1:
    print("您输入的不是奇数！")
else:
    a=n//2+1
    for i in range(1,n+1):
        if i<=a:
            print(' '*(a-i),end='')
            print('*'*(2*i-1),end='')
            print('')
        else:
            print(' '*(i-a),end='')
            print('*'*((n-i+1)*2-1),end='')
            print('')
        sleep(0.5)
'''


perC=13.47
perI=12.1
radioC=0.0048
radioI=0.012
y=2011
while perC>perI:
    perC=perC*(1+radioC)
    perI=perI*(1+radioI)
    y=y+1
else:
    print("印度人口将在",y,"年超过中国")
    print("中印人口分别为：",perC,perI)
                



































