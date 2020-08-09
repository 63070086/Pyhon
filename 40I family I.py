"""string"""
def main():
    """input tye lower"""
    name = input()
    name2 = name.isalpha()
    print("Alpha: %r"%(name2))
    name3 = name.isdecimal()
    print("Decimal: %r"%(name3))
    name4 = name.isnumeric()
    print("Numeric: %r"%(name4))
    name5 = name.isdigit()
    print("Digit: %r"%(name5))
main()
