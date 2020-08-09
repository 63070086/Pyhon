"""Pro Grade"""
def main():
    """intput name-input numGrade"""
    name = str(input()).capitalize()
    grade = input()
    grade = float(grade)
    if grade >= 90 and grade <= 100:
        print("%s Grade: A"%(name))
    elif grade >= 85 and grade < 90:
        print("%s Grade: B+"%(name))
    elif grade >= 80 and grade < 85:
        print("%s Grade: B"%(name))
    elif grade >= 75 and grade < 80:
        print("%s Grade: C+"%(name))
    elif grade >= 70 and grade < 75:
        print("%s Grade: C"%(name))
    elif grade >= 65 and grade < 70:
        print("%s Grade: D+"%(name))
    elif grade >= 55 and grade < 65:
        print("%s Grade: D"%(name))
    else:
        print("See you next semester, %s"%(name))
main()
