#!/usr/bin/env python
# coding=utf-8

# 3

def SimpleAdding(num):
    newNum = 0

    # code goes here
    for i in range(int(num) + 1):
        newNum = newNum + i

    return newNum

# keep this function call here
print SimpleAdding(raw_input())


exit()



#  2

def LetterChanges(valami):
    newValami=""
    newChar=""

    # code goes here
    # print ord("v")

    for char in (valami):
        if char.isalpha():
            if char.lower() == "z":
                newChar = 'a'
            else:
                newChar = chr(ord(char) + 1)
        else:
            newChar = char

        if newChar in "aeiou":
            newChar = newChar.upper()

        newValami = newValami + newChar

    return newValami

# keep this function call here
print LetterChanges(raw_input())

exit()

# 1
def FirstReverse(valami):
    # code goes here
    string = valami[::-1]
    return str(string)

# keep this function call here
print FirstReverse(raw_input())

exit()

