"""Prepro"""
def main():
    """48."""
    word = input().lower()
    tex = input().lower()
    numtex = len(tex)
    num = word.count(tex)
    if num >= 1:
        if numtex == 1:
            print("Character : %d" %num)
        else:
            print("Word : %d" %num)
    else:
        print("No word and character.")
main()

