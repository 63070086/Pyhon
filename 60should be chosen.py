"""funtion"""
def suba(num):
    """funtion"""
    if num >= 1 and num < 4:
        num2 = num * 725
        return num2
    elif num >= 4 and num % 4 == 0:
        num1 = num/4
        num1 = round(num1)
        num2 = (num1*(725*3))
        return num2
    elif num >= 4 and num % 4 != 0:
        num1 = num // 4
        excess = num - (num1*4)
        num1 = round(num1)
        num2 = (num1*(725*3))+(excess*725)
        return num2

def subb(num):
    """funtion"""
    num3 = num * 549
    return num3

def subc(num):
    """funtion"""
    num4 = num * 699
    if num4 >= 3000:
        numper = (num4*20)/100
        numper = round(numper)
        num4 = num4 - numper
        return num4
    else:
        return num4

def main():
    """input"""
    num = abs(int(input()))
    if subb(num) > suba(num) > subc(num):
        print("A")
    elif suba(num) > subb(num) > subc(num):
        print("B")
    elif suba(num) > subc(num) > subb(num):
        print("C")
    elif subc(num) > suba(num) > subb(num):
        print("A")
    elif subc(num) > subb(num) > suba(num):
        print("B")
    elif subb(num) > subc(num) > suba(num):
        print("C")
main()
