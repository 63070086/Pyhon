"""battery"""
def bat1():
    """Input BaterPer"""
    num_bat2 = int(input())
    num_wide = int(input())
    num_b = (num_bat2*num_wide)//100
    num_c = num_wide-num_b
    text_o = 'O'
    text__ = '_'
    print("(%s%s) %d%%"%(text_o*num_b, text__*num_c, num_bat2))
bat1()
