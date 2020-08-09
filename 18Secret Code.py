"""samakarn"""
def spyfall():
    """input """
    num = int(input())
    nump1 = (num%10)//1
    nump2 = (num%100)/10
    nump3 = (num%1000)//100
    nump4 = (num%10000)//1000
    nump5 = (num%100000)//10000
    print("%d%d%d%d%d"%(nump1, nump2, nump3, nump4, nump5))
spyfall()