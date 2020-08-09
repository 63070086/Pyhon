"""Arrow"""
def main():
    """input k and m"""
    numk = int(input())
    numn = int(input())
    lspace1 = numn//2
    lspace2 = numn//2
    if numn % 2 != 0:
        for _ in range(lspace1, 0, -1):
            print(lspace1*" " + numk*"*")
            lspace1 -= 1
        print(numk*"*")
        lspace1 += 1
        for _ in range(0, lspace2):
            print(lspace1*" " + numk*"*")
            lspace1 += 1
main()
