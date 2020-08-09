"""moly"""
def main():
    """int str"""
    skill = int(input())
    skilltest = skill
    cover = input().upper()
    speed = int(input())
    zoom = input().upper()
    check = 0
    if zoom == "Y":
        skill += 2
    if skill >= 1 and skill <= 7:
        if skill >= 4:
            if cover == 'Y':
                print("Normal Moly!!!")
            elif cover == "N":
                if speed <= 2:
                    print("Normal Moly!!!")
                    check = 1
                else:
                    print("try again")
                    check = 1
        if skill >= 6:
            if cover == 'Y':
                print("Rare Moly!! How cute!!!")
            elif cover == 'N':
                if speed <= 1:
                    print("Rare Moly!! How cute!!!")
                elif check != 1:
                    print("try again")
        if skill < 4:
            print("try again")
        if skilltest < 1:
            pass
main()
