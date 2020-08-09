"""Code Python 4"""
def main():
    """input 2 """
    text = input()
    num = text.count('9')
    if num >= 9:
        print("Hooray! This life must go on.")
    elif num >= 1 and num < 9:
        num2 = 9 - num
        print("My fortune is running out.\nI want %d more!"%(num2))
    else:
        print("Are you kidding me?!")
main()
