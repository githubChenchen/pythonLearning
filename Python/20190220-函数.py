def jiecheng(num):
    s=1
    for i in range(1,num+1):
        s=s*i
    return s
def jiecheng_sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=jiecheng(i)
    return sum
print(jiecheng_sum(4))
