import re
s='Do not trouble1 trouble till trouble troubles you.'
r='t[a-zA-Z]+\d+'
print(re.match(r,s))    #在s开头处匹配正则表达式
print(re.search(r,s))   #在s任意位置匹配正则表达式
print(re.findall(r,s))  #以列表形式返回s中所有正则表达式


r1=re.compile(r)      #complie方法将字符串转换为正则表达式对象
print(r1.findall(s))

s2='a234b132c'
r2=re.compile('\d+')
print(r2.split(s2))    #以正则表达式分隔字符串
print(r2.split(s2,1))   #分隔一次
