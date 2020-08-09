"""battery"""
def bat1():
    """Input BaterPer"""
    num_bat1 = int(input())
    num_floor1 = num_bat1//10
    num_foor2 = 10-num_floor1
    text_o = 'O'
    text__ = '_'
    print("(%s%s) %d%%"%(text_o*num_floor1, text__*num_foor2, num_bat1))
bat1()
