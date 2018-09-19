#!/usr/bin/env python
# coding=utf-8

def ChessboardTraveling(str):
    startX = 1
    startY = 1
    endX = 4
    endY = 3
    distX = endX - startX
    distY = endY - startY
    posX = 0
    posY = 0
    possibleMoveNum = distX + distY
    possibleMoves = ["R", "U"]
    results = []

    prevMoves = []

    for pm in range(endX * endY):
        currMoves = ""
        # for res in range(len(results)):

        print 'prevMoves: ', prevMoves

        for step in range(possibleMoveNum):
            # if prevMoves[0] == "R":
            #     pass

            if currMoves.count("R") < distX:

                currMove = "R"

                currMoves += currMove
            else:
                currMoves += "U"

        print 'currMoves: ', currMoves

        if len(results) == 0:
            results.append(currMoves)
            prevMoves = results[len(results) - 1]
        else:
            if currMoves not in results:
                results.append(currMoves)
                prevMoves = results[len(results) - 1]

    print results

# keep this function call here
# print ChessboardTraveling(raw_input())
ChessboardTraveling("1")

exit()


# 11
def ChessboardTraveling(str):
    startX = 1
    startY = 1
    endX = 3
    endY = 4
    distX = endX - startX
    distY = endY - startY
    posX = 0
    posY = 0

    # print "distX = ", distX, range(distX)
    # print "distY = ", distY, range(distY)

    prevMoves = []
    currMoves = []
    results = []
    finish = False
    hasPreviousResult = False
    possibleMoves = ["R", "U"]

    possibleMoveNum = distX + distY
    # for res in results:

    # for currRes in range(len(results) + 1):

    # if len(results) > 0:
    #     hasPreviousResult = True
    #     prevMoves = results[0]

    moveNum = 0

    # if hasPreviousResult == True:
    # for pm in range(endX * endY):
    for pm in range(4):
        finish = False
        posX = 0
        posY = 0

        if hasPreviousResult == True:
            # print pm, prevMoves
            while finish == False:
                # print 'moveNum: ', moveNum
                if moveNum < possibleMoveNum:
                    if prevMoves[moveNum] == "R":
                        if posY < distY:
                            posY = stepUp(posY)
                            currMoves.append("U")
                            moveNum += 1
                            printCurrMoves(currMoves, moveNum)
                        elif posX < distX:
                            posX = stepRight(posX)
                            currMoves.append("R")
                            moveNum += 1
                            printCurrMoves(currMoves, moveNum)
                        else:
                            finish = True
                    else:
                        if posX < distX:
                            posX = stepRight(posX)
                            currMoves.append("R")
                            moveNum += 1
                            printCurrMoves(currMoves, moveNum)
                        elif posY < distY:
                            posY = stepUp(posY)
                            currMoves.append("U")
                            moveNum += 1
                            printCurrMoves(currMoves, moveNum)
                        else:
                            finish = True
                else:
                    finish = True

                if finish == True:
                    results.append(currMoves)
                    moveNum = 0
                    print currMoves, len(currMoves)
                    currMoves = []
                    hasPreviousResult = True
                    prevMoves = results[len(results) - 1]
                    # prevMoves = results[0]

        else:
            # print pm
            while finish == False:
                if posX < distX:
                    posX = stepRight(posX)
                    currMoves.append("R")
                    moveNum += 1
                    printCurrMoves(currMoves, moveNum)
                elif posY < distY:
                    posY = stepUp(posY)
                    currMoves.append("U")
                    moveNum += 1
                    printCurrMoves(currMoves, moveNum)
                else:
                    finish = True

                if finish == True:
                    results.append(currMoves)
                    moveNum = 0
                    print currMoves, len(currMoves)
                    currMoves = []
                    hasPreviousResult = True
                    prevMoves = results[0]

            # print 'prevMoves: ', prevMoves


    # print results, len(results)



    for moveX in range(distX):
        for moveY in range(distY):
            pass

    # code goes here
    return str


def printCurrMoves(currMoves, moveNum):
    pass
    # print currMoves, moveNum

def stepRight(posX):
    posX += 1
    return posX

def stepUp(posY):
    posY += 1
    return posY

# keep this function call here
# print ChessboardTraveling(raw_input())
ChessboardTraveling("1")
exit()

# 10
#
# lista, amiben tárolom az utat pl:
# [j, j, f, f, f]
# [j, f, j, f, f]
# stepRight
#     stepUp



def KaprekarsConstant(num):
    multiNum = 0

    # code goes here
    while 1:
        newNumList = []

        for char in num:
            if char.isalnum():
                newNumList.append(char)

            newNumList.sort()

        newSmallNum = int("".join(newNumList))
        newBigNum = int("".join(newNumList)[::-1])
        resultNum = newBigNum - newSmallNum
        multiNum += 1

        if len(str(resultNum)) < 4:
            resultNum = resultNum * 10
        num = str(resultNum)

        # print newBigNum, '-', newSmallNum, '=', resultNum, num, 'multi =', multiNum
        if num == '6174':
            break

    return multiNum

# keep this function call here
print KaprekarsConstant(raw_input())
# KaprekarsConstant("2111")

exit()



# 9
def AlphabetSoup(str):
    newStrList = []

    # code goes here
    for char in str:
        if char.isalpha():
            newStrList.append(char)

    newStrList.sort()
    newStr = "".join(newStrList)

    return newStr

# keep this function call here
print AlphabetSoup(raw_input())

exit()



# 8
def TimeConvert(num):

    # code goes here
    minutes = int(num) % 60
    hours = (num - minutes) / 60
    return str(hours) + ':' + str(minutes)

# keep this function call here
print TimeConvert(raw_input())

exit()



# 7
def CheckNums(num1,num2):

    # code goes here
    if num1 == num2:
        return "-1"
    elif num1 > num2:
        return "False"
    else:
        return "True"

# keep this function call here
print CheckNums(raw_input())

exit()



# 6
def LetterCapitalize(sen):
    # code goes here
    words = sen.split()
    vv = []

    for word in words:
        newWord = word.capitalize()

        vv.append(newWord)

    sen = vv
    new = " ".join(vv)
    return new

# keep this function call here
print LetterCapitalize(raw_input())

exit()



# 5
def FirstFactorial(num):
    newNum = 1

    # code goes here
    for i in range(int(num)):
        newNum = newNum * (i + 1)

    return newNum

# keep this function call here
print FirstFactorial(raw_input())

exit()



# 4
def LongestWord(sen):
    longestWord = ""
    wordLength = 0

    # code goes here
    words = sen.split()

    for word in words:

        newWord = ""
        for char in word:
            if char.isalnum():
                newWord = newWord + char

        print newWord

        if len(newWord) > wordLength:
            longestWord = newWord
            wordLength = len(newWord)

    sen = longestWord
    return sen

# keep this function call here
# print LongestWord(raw_input())

# LongestWord("Argument goes here")

val="asdfhg!! ,. dsds???dfd"
tt=string.maketrans("!?.,", "X")
print val.translate(tt)

exit()



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

