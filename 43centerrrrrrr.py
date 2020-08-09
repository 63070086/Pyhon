"""string"""
def main():
    """input func"""
    wide = int(input())
    text = input()
    text1 = len(text)
    equal = wide*'='
    wide1 = (wide-text1)//2
    centera = wide1*'-'
    print("%s"%(equal))
    print("%s%s%s"%(centera, text, centera))
    print("%s"%(equal))
main()
