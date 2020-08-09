"""function"""
def main():
    """input 3 """
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numb1 = numb*-1
    numb2 = (numb**2)-(4*(numa*numc))
    if numb2 >= 0:
        numb2 = numb2**0.5
        numb2test = numb2
    elif numb2 < 0:
        numb2 = (abs(numb2)**0.5)*-1
        numb2test = numb2
    numsum = ((numb1 + numb2) / (2*numa))
    numdel = ((numb1 - numb2) / (2*numa))
    if numb2test > 0:
        print("%0.02f"%(numsum))
        print("%0.02f"%(numdel))
    elif numb2test == 0:
        print("%0.02f"%(numsum))
    elif numb2test < 0:
        print("No Answer!")
main()
