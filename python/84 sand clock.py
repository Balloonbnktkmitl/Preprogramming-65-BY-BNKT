"""Prepro"""
def main():
    """84 sand clock"""
    num = int(input())
    column = (2*num)+1
    print("*"*column)
    for row in range(column):
        for col in range(column):
            if col == row or col == column-row-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("*"*column)
main()
