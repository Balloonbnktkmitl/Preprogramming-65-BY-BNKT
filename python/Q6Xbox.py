"""Quiz"""
def pattern(num):
    for i in range(0, num):
        for j in range(0, num):
            if (i == 0 or i == num - 1
                or j == 0 or j == num - 1
                or i == j or i == num - 1 - j):        
                print( "*", end=" ")
            else:
                print( " ",end=" ")
        print("")
def main():
    """Q6Xbox"""
    num = int(input())
    pattern(num)
main()
