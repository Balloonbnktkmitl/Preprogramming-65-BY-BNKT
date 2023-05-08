"""Prepro"""
def main():
    """83X"""
    num = int(input())
    for row in range(num):
        for column in range(num):
            if column == row:
                print("* ", end="")
            elif column + row == num-1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
main()
