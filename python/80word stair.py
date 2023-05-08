"""Prepro"""
import string
def main():
    """80word stair"""
    word = input().upper()
    text = string.ascii_uppercase.find(word)
    posi = string.ascii_uppercase[:text+1]
    for i in posi:
        text1 = string.ascii_uppercase.find(i)
        posi1 = string.ascii_uppercase[:text1+1]
        for column in posi1:
            print(column, end=' ')
        print()
main()
