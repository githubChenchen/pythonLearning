class Person:
    number=0                                #类属性
    def __init__(self,name,gender,age):     #初始化对象属性（实例属性），在构造函数中定义，以self作为前缀，只能通过对象名访问
        self.name=name
        self.gender=gender
        self.age=age
        Person.number+=1
    def displayPerson(self):
        print("Name:",self.name,"Gender:",self.gender,"Age:",self.age)
    def displayNumber(self):
        print("Total:",Person.number)


stu1=Person('xiaoming','M',18)
stu2=Person('xiaoli','F',19)
stu1.score=85   #增加属性
stu2.score=90
stu1.displayPerson()
stu2.displayPerson()
getattr(stu1,'score') #访问属性的值
hasattr(stu1,'score') #检测属性是否存在
setattr(stu1,'score',90) #设置属性值，如果没有该属性，则创建该属性
delattr(stu1,'score') #删除属性
print(stu1.score)
print(stu2.score)
stu1.age=21     #修改属性
del stu1.score   #删除属性
stu1.displayPerson()
print(stu1.score)
