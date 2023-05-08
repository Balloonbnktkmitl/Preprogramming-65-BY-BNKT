"""Prepro"""
def main():
    """85diamond"""
    num = int(input())
    for i in range(0, num):
        if i <= num//2:
            print(" "*(num//2-i), end="")
            print("*"*((2*i)+1))
        else:
            print(" "*(i-(num//2)), end="")
            print("*"*(num-((2*i)-num)-1))
main()
