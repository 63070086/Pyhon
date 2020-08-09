"""string"""
def main():
    """input tye lower"""
    name = int(input())
    name = abs(name)
    name = str(name)
    name2 = 'i'
    name3 = name + name2
    name4 = name3.find(name2)
    print("%d"%(name4))
main()
