""" code odd /even"""
def main():
    """input N"""
    numn = int(input())
    if numn % 2 != 0:
        print("Weird")
    elif numn % 2 == 0 and numn >= 2 and numn <= 5:
        print("Not Weird")
    elif numn % 2 == 0 and numn >= 6 and numn <= 20:
        print("Weird")
    elif numn % 2 == 0 and numn > 20:
        print("Not Weird")
main()
