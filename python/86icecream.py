"""Prepro"""
def main():
    """86icecream"""
    num = int(input())
    taste = input().lower()
    if taste == "m" or taste == "s" or taste == "c" or taste == "b" \
or taste == "r":
        for i in range(0, (2*num)-1):
            if i <= ((2*num)-1)//2:
                print(" "*((((2*num)-2)//2)-i), end="")
                print(taste*((2*i)+1))
            else:
                print(" "*((i-(num*2-1)//2)), end="")
                print("_"*(((2 * num) - 1) - ((2 * i) - ((2 * num) - 1)) - 1))
    else:
        print("Hey!,buy another shop.")
main()
