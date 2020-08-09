"""Long Code"""
def hello():
    """code input"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    num9 = int(input())
    num10 = int(input())
    maxcode = max(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    print("max: %d"%(maxcode))
    mincode = min(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    print("min: %d"%(mincode))
    sum_num = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
    print("sum: %d"%(sum_num))
    sum_recib = num1*num2*num3*num4*num5*num6*num7*num8*num9*num10
    sumlen = str(sum_recib)
    print("digit: %s"%(len(sumlen)))
hello()
