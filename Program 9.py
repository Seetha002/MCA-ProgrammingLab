#!/usr/bin/env python
# coding: utf-8

# In[2]:


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if self.area()==other.area():
            print("Two rectangles have same area")
        else:
            print("Does not have same area")
rect1=rectangle(5,10)
rect2=rectangle(8,6)
print("Area of rectangle 1 is:",rect1.area())
print("Perimeter of rectangle 1 is:",rect1.perimeter())
print("Area of rectangle 2 is:",rect2.area())
print("Perimeter of rectangle 2 is:",rect2.perimeter())
rect1.compare(rect2)


# In[4]:


class bank:
    def __init__(self,acct_no,acct_name,acct_type,bal):
        self.acct_no=acct_no
        self.acct_name=acct_name
        self.acct_type=acct_type
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("The amount ",amt," is deposited")
        print("Current balance:",self.bal)
    def withdraw(self,amt):
        self.bal=self.bal-amt
        print("The amount ",amt," is withdrawn")
        print("Current balance:",self.bal)
account=bank(1234,"seetha","savings",1000)
account.deposit(500)
account.withdraw(200)


# In[11]:


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


# In[26]:


class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __str__(self):
        return "%.2d:%.2d:%.2d".self.hour,self.minute,self.second
    def __add__(self,other):
        self.hour=self.hour+other.hour
        self.minute=self.minute+other.minute
        self.second=self.second+other.second
        if self.second>=60:
            self.second-=60
            self.minute+=1
        if self.minute>=60:
            self.minute-=60
            self.hour+=1
        return "hour:"+str(self.hour)+"minute:"+str(self.minute)+"second:"+str(self.second)
time1=time(9,45,20)
time2=time(1,35,20)
print(time1+time2)


# In[ ]:




