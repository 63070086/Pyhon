""" BMI """
def main():
    """code calcu BMI"""
    num_kg = float(input())
    num_cm = int(input())
    num_m = num_cm/100
    num_bm = num_kg / (num_m**2)
    num_bm = float("%0.01f"%(num_bm))
    if num_bm >= 30:
        print("you're too fat, lose weight now!")
    if num_bm >= 25 and num_bm < 30:
        print("you're almost fat, prepare the losing weight course!")
    if num_bm >= 18.6 and num_bm < 25:
        print("pass, welcome Technaldooooo!")
    if num_bm < 18.6:
        print("you're so weak, eat more!")
main()
