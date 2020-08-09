""" code odd /even"""
def main():
    """input 24h"""
    numh = float(input())
    if numh >= 0.00 and numh < 12.00:
        print("Good Morning!")
    elif numh >= 12.00 and numh < 17.00:
        print("Good Afternoon!")
    elif numh >= 17.00 and numh < 24.00:
        print("Good Evening!")
    elif numh == 24.00:
        print("Good Morning!")
main()
