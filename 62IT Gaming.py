"""IT Gaming"""
def main():
    """input 3"""
    game = input().capitalize()
    cate = input().lower()
    price = float(input())
    if cate == "action" or cate == "adventure":
        print("(Discount) %s Price: %0.02f Baht"%(game, price - (price*25)/100))
    elif cate == "creative" or cate == "survival" or cate == "sport" or cate == "racing"\
        or cate == "simulator":
        if len(game) % 4 == 0:
            print("Discount Season: Spring")
            print("(Discount) %s Price: %0.02f Baht"%(game, price - (price*35)/100))
        elif len(game) % 4 == 1:
            print("Discount Season: Summer")
            print("(Discount) %s Price: %0.02f Baht"%(game, price - (price*45)/100))
        elif len(game) % 4 == 2:
            print("Discount Season: Fall")
            print("(Discount) %s Price: %0.02f Baht"%(game, price - (price*40)/100))
        elif len(game) % 4 == 3:
            print("Discount Season: Winter")
            print("(Discount) %s Price: %0.02f Baht"%(game, price - (price*38)/100))
    else:
        print("404 error!")
main()
