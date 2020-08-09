"""Hamburger"""
def main():
    """input side1 side2"""
    side1 = int(input())
    side2 = int(input())
    meat = (side1+side2)*2
    print(("|"*side1) + ("*" * meat)+("|"*side2))
main()
