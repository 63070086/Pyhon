""" tex """
def main():
    """if condition"""
    num = int(input())
    numh = num//60
    bath = 900.00
    numhe = num%60
    if numhe >= 20:
        numh = numh + 1
    if numh == 1:
        bath = bath * numh
        print("Total price is %0.02f baht"%(bath))
    if numh >= 2 and numh < 4:  
        bath = bath * numh
        numhper = (bath * 10)/100
        numbath = bath - numhper
        print("Total price is %0.02f baht"%(numbath))
    if numh >= 4 and numh < 5:
        bath = bath * numh
        numhper = (bath * 20)/100
        numbath = bath - numhper
        print("Total price is %0.02f baht"%(numbath))
    if numh >= 5:
        bath = bath * numh
        numhper = (bath * 30)/100
        numbath = bath - numhper
        print("Total price is %0.02f baht"%(numbath))
main()
