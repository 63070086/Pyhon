""" describtion"""
def basenum():
    """input numbase 10"""
    num_10 = int(input())
    num2 = bin(num_10)
    num8 = oct(num_10)
    num16 = hex(num_10)
    print(num2)
    print(num8)
    print(num16)
basenum()
