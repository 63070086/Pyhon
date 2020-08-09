"""float"""
def floating():
    """input int"""
    num1 = int(input())
    num0 = num1-1
    print("%0.1f%s"%(num1, '0'*num0))
floating()
