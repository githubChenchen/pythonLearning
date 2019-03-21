class Circle:
    def __init__(self,metre):
        self.metre=metre
    def square(self):
        print(3.14*self.metre*self.metre)
class Table:
    def __init__(self,height,color):
        self.height=height
        self.color=color
    def display(self):
        print(self.height,self.color)
class Roundtable(Circle,Table):
    def __init__(self,metre,height,color):
        Circle.__init__(self,metre)
        Table.__init__(self,height,color)
    def displayRound(self):
        super(Roundtable,self).square()
        super(Roundtable,self).display()
rt=Roundtable(1,1,'yellow')
rt.displayRound()
