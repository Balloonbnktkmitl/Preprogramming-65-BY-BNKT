"""Prpepro"""
def main():
    """89Basic Index"""
    wordlist = []
    while True:
        word = input()
        if word.upper() == "END":
            break
        else:
            wordlist.append(word)
    ind = int(input())
    if -(len(wordlist)) <= ind < len(wordlist):
        print("List[%d] = \"%s\"" %(ind, wordlist[ind]))
    else:
        print("Index Not Found")
main()
