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
