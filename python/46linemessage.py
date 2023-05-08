"""Prepro"""
def main():
    """46."""
    word1 = input().capitalize()
    word2 = input().capitalize()
    word3 = input().capitalize()
    word = (word1, word2, word3)
    cal = sorted(word, key=len)
    print(cal[0])
    print(cal[1])
    print(cal[2])
main()
