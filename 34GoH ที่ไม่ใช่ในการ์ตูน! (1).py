"""gho2"""
import math
def f_funch(numx):
    """sub code"""
    fx_code = 3*(2**numx)+(2*(numx**2))* (math.degrees(math.asin(0.5))+numx)
    return fx_code

def g_funch(numx):
    """sub code"""
    gx_code = 4*(numx+2)**2+(5*(numx-1))+h_funch(numx-1)
    return gx_code

def h_funch(numx):
    """sub code"""
    hx_code = (3*(numx+4))-(numx*(5-(3*numx)))
    return hx_code

def main_code():
    """main code"""
    numx = int(input())
    resualt = g_funch(f_funch(numx-2)/h_funch(numx+1))-numx
    print("Answer: %0.02f"%(resualt))
main_code()
