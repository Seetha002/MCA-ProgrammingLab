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


# In[47]:


class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        total=time()
        total.__hour=self.__hour+other.__hour
        total.__minute=self.__minute+other.__minute
        total.__second=self.__second+other.__second
        if total.__second>=60:
            total.__second-=60
            total.__minute+=1
        if total.__minute>=60:
            total.__minute-=60
            total.__hour+=1
        return "Hour :"+str(total.__hour)+" Minute:"+str(total.__minute)+" second:"+str(total.__second)
time1=time(9,45)
time2=time(1,35,20)
print(time1+time2)


# In[ ]:





# In[ ]:




