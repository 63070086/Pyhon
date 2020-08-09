"""subcode"""
import math
def main():
    """main code"""
    xnum = float(input())
    ynum = float(input())
    znum = int(input())
    znumradian = -math.radians(znum)
    xcos = xnum*(math.cos(znumradian))
    xsin = xnum*(math.sin(znumradian))
    ycos = ynum*(math.cos(znumradian))
    ysin = ynum*(math.sin(znumradian))
    typex = xcos - ysin
    typey = xsin + ycos
    print("%0.03f %0.03f"%(typex, typey))
main()
