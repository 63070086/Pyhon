"""input"""
def main():
    """funtion"""
    text = input()
    textnum = len(text)
    print(" %s"%((textnum+2)*"-"))
    space = (textnum +2)*" "
    textlr = "|"+space+"|"
    textnum2 = (textnum)//2
    if textnum == 0:
        print("%s"%(textlr))
    else:
        print("%s"%((textlr+"\n")*textnum2), end="")
        print("| %s |"%(text))
        print("%s"%((textlr+"\n")*textnum2), end="")
    print(" %s"%((textnum+2)*"-"))
main()
