"""Prepro"""
def main():
    """78cat stair"""
    row = int(input())
    for i in range(row):
        for j in range(row):
            if j < i:
                print(' ', end=' ')
            else:
                print('* ', end='')
        print()
main()
