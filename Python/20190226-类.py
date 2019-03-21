class Methods:
    @classmethod
    def publicMethod(cls): #类方法定义传入cls参数，调用是不用传参
        print('公有类方法')
    @classmethod
    def __privateMethod(cls): #私有类方法
        print('私有类方法')
    @staticmethod
    def staticMethods(): #公有静态方法 定义是无需传入cls或self参数
        print('公有静态方法')
    @staticmethod
    def __privateMethod(): #私有静态方法 访问方式同类方法
        print('私有静态方法')
    def publicM(self):
        print('普通公有方法')
    def __privateM(self):
        print('普通私有方法')
    PublicMethodtoClass=classmethod(publicM) #普通方法转化为类方法
    PrivateMethodtoClass=classmethod(__privateM) #普通方法转化为私有类方法
m=Methods()
m.publicMethod() #类方法可通过类名和实例名调用
Methods.publicMethod()
m._Methods__privateMethod()
Methods._Methods__privateMethod()
m.publicM()
m._Methods__privateM()


#派生类继承基类：class Student(Person):    Student为派生类，Person为基类
#super(Student,self).__init__(name,age,gender)  调用基类相关方法
#Python支持多继承
