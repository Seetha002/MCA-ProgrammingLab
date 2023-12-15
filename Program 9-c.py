class rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length*self.__breadth
    def compare(self,other):
        return self.area()<other.area()
rect1=rectangle(2,3)
rect2=rectangle(5,10)
print("Area of rectangle 1:",rect1.area())
print("Area of rectangle 2:",rect2.area())
print("Areas of two rectangles are similar?",rect1.compare(rect2))
