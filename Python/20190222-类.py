class Car:
    price=150000 #公有类属性
    __factPrice=120000 #私有类属性 由两个下划线定义
    def __init__(self,brand,serial):
        self.brand=brand #公有对象属性
        self.__serial=serial #私有对象属性 由两个下划线定义
    def publicFunc(self):
        print('公有方法')
    def __privateFunc(self):
        print('私有方法')

c1=Car('丰田','卡罗拉')
c1.publicFunc()
Car.publicFunc(c1) #通过类名调用需要传入一个方法
c1._Car__privateFunc()
Car._Car__privateFunc(c1) #通过类名调用需要传入一个方法
print(Car.price)
print(Car._Car__factPrice)
print(c1.brand)
print(c1._Car__serial)
#公有方法与私有方法定义调用类似
