"""Prepro"""
def main():
    """38."""
    weight = float(input())
    height = float(input())
    age = int(input())
    bmi = weight/((height/100)**2)
    if age < 18:
        print("Please use BMI for Children and Teens.")
    else:
        if bmi < 16:
            print("Severe Thinness")
        elif bmi < 16.99:
            print("Moderate Thinness")
        elif bmi < 18.49:
            print("Mild Thinness")
        elif bmi < 24.99:
            print("Normal")
        elif bmi < 29.99:
            print("Overweight")
        elif bmi < 34.99:
            print("Obese Class I")
        elif bmi < 39.99:
            print("Obese Class II")
        else:
            print("Obese Class III")
main()
