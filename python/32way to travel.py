"""Prepro"""
def main():
    """32."""
    weather = input()
    sumkun = input()
    dis = float(input())
    if weather == "rainy" and sumkun == "not important":
        print("Not go")
    else:
        if dis >= 300:
            print("Private jet")
        elif dis < 300 and dis >= 20:
            print("Car")
        elif dis < 20 and dis >= 1:
            print("Motorcycle")
        elif dis < 1 and dis > -1:
            print("Walk")
        else:
            print("Error")
main()
