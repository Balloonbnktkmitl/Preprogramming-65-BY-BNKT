"""Prepro"""
def main():
    """51."""
    word = input()
    if word.count("\"") == 0:
        print("No error")
    else:
        cal = word.index("\"")
        cal2 = word.rindex("\"")
        calas = chr(int(word[cal+1:cal2]))
        print(word.replace(word[cal:cal2+1], calas))
main()
