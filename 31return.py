""" sub code """
def sub(fting):
    """return fting """
    return fting**2

def main():
    """main code"""
    fting = float(input())
    fting = sub(fting)
    print("%.02f"%(fting))
main()
