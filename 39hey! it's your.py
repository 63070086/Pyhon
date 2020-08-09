"""string"""
def main():
    """input tye function"""
    name = input()
    name2 = input()
    dela_text = name.strip(name2)
    delr_text = name.rstrip(name2)
    dell_text = name.lstrip(name2)
    print(dela_text)
    print(dell_text)
    print(delr_text)
main()
