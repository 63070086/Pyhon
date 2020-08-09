"""Code Python 4"""
def main():
    """input name """
    name = input()
    fill_name = name + 'i'
    cnum = fill_name.rfind('i')
    if cnum <= 5 and cnum > 0:
        print('True')
    else:
        print('False')
main()
