"""def"""
def numsum():
    """docstring input"""
    numx1 = float(input())
    numy1 = float(input())
    numx2 = float(input())
    numy2 = float(input())
    sum1 = (numx2-numx1)**2
    sum2 = (numy2-numy1)**2
    sum3 = sum1+sum2
    sum4 = sum3**0.5
    print("Distance = %0.03f"%(sum4))
numsum()
