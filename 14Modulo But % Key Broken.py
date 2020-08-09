""" NOT % """
def not_modulo():
    """Input Int"""
    num1 = int(input())
    num2 = int(input())
    num_floor = num1//num2
    num_x = num_floor*num2
    print(num1-num_x)
not_modulo()
