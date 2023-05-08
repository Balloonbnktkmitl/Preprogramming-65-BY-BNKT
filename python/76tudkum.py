"""Prepro"""
def main():
    """76tudkum"""
    word = input()
    while True:
        reword = input().lower()
        if word.find(reword) == -1:
            break
        while reword in word:
            word = word.replace(reword, "")
    print(word)
main()
