"""kmitl code"""
def main():
    """sub code input kmitl"""
    text = input()
    text = text.lower()
    find_text = text.count('k')
    find_text2 = text.count('m')
    find_text3 = text.count('i')
    find_text4 = text.count('t')
    find_text5 = text.count('l')
    num = 0
    if find_text >= 1:
        num = num + (find_text/find_text)
        if find_text2 >= 1:
            num = num + (find_text2/find_text)
            if find_text3 >= 1 and find_text3 >= 2:
                num = num + 2
                if find_text4 >= 1 and find_text4 >= 2:
                    num = num +2
                    if find_text5 >= 1:
                        num = num + (find_text5/find_text)
    else:
        pass
    if num >= 7:
        print('Yes')
    else:
        print('No')
main()
