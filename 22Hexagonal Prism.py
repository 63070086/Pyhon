"""Describe"""
def sumsum():
    """ input"""
    rong = float(input())
    height = float(input())
    square = (rong*height)*6
    sum1 = (((((3**0.5)/4)*rong**2)*6)*2)
    sum2 = ((square+sum1)/10000)
    print("%0.02f squaremetre"%sum2)
sumsum()
