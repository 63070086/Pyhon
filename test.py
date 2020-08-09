allprice = int(input())
pricein = int(input())
numset = [100, 20, 10, 5, 1]
check = 0
text = ""
if pricein >= allprice:
    excess = allprice - pricein
    if excess == 0:
        print("Bank %d"%(numset[0]))
        print("Bank %d"%(numset[1]))
        print("Coin %d"%(numset[2]))
        print("Coin %d"%(numset[3]))
        print("Coin %d"%(numset[4]))
    for _ in range(len(numset)):
        if excess % numset[check] == 0:
            check +=1
        elif excess % numset[check] !=0:
            if numset[check] >=20:
                text = "Bank"
            elif numset[check] < 20:
                text = "Coin"
            print("%s %d"%(text, numset[check]))
            check += 1
else:
    print("No! Noo! Nooo!")
    print("your cash is not enough.")
    print("need %d more."%(allprice - pricein))