"""pow round"""
def pow_round():
    """input"""
    num = float(input())
    num1 = round(num)
    min1 = pow(num1+num1**5, 9876543, 60)
    print("15:%.02d"%(min1))
pow_round()
