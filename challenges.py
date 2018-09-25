#!/usr/bin/env python
# coding=utf-8


# aqrst
# ukaei
# ffooo


# abcd
# eikr
# oufj

def VowelSquare(strArr):
    vowels = "aeiouy"

    # strArr = list(strArr)

    rowNum = len(strArr)
    colNum = len(strArr[0])

    print strArr, type(strArr), rowNum, colNum

    rr = 0
    while rr < rowNum:
        currRow = strArr[rr]
        if rr < rowNum - 1:
            nextRow = strArr[rr + 1]
        else:
            nextRow = strArr[rr]

        for r in range(len(currRow)):
            # print currRow
            if r < len(currRow) - 1 and rr < rowNum - 1 and currRow[r] in vowels:
                if currRow[r + 1] in vowels and nextRow[r] in vowels and nextRow[r + 1] in vowels:
                    return str(rr) + "-" + str(r)
                    break

        rr += 1

    # code goes here
    return "not found"

# keep this function call here
# print VowelSquare(raw_input())
print VowelSquare(["abcd", "eikr", "oufj"])
# VowelSquare(["abcd", "eikr", "oufj"])
# print VowelSquare(["aqrst", "ukaei", "ffooo"])

exit()



def ScaleBalancing(strArr):
    x,y = eval(strArr[0])
    w = eval(strArr[1])

    for i in range(0, len(w)):
        if x + w[i] == y or y + w[i] == x:
            return w[i]
        for j in range(i + 1, len(w)):
            if x + w[i] == y + w[j] or x + w[j] == y + w[i] or x + w[i] + w[j] == y or x == y + w[i] + w[j]:
                return str(w[i]) + ',' + str(w[j])
    # code goes here
    return 'not possible'

# keep this function call here
# print ScaleBalancing(raw_input())
# print ScaleBalancing(["1, 8", "1, 2, 3, 6, 14"])
# print ScaleBalancing(["5, 9", "1, 2, 6, 7"])
print ScaleBalancing(["3, 10", "1, 1, 5, 10"])

exit()

def ScaleBalancing(strArr):

    chain = "(34 + 8)/3"
    res = eval(chain)
    print res, type(res)

    weights = strArr[0]
    weights.sort()

    diff = max(weights) - min(weights)
    # print diff


    addWeights = strArr[1]
    sumWeights = []
    # print addWeights[-1]

    sum = []
    for aw in addWeights:
        if sum:
            sum.append(sum[-1] + aw)
        else:
            sum.append(aw)
            print "üres a lista"


    print sum
    # sum = 0
    # for aw in addWeights:
    #     sum += aw
    #     print sum
    #     if sum == diff:
    #         print sum


    # print sum


    # code goes here
    # return strArr

# keep this function call here
# print ScaleBalancing(raw_input())
# ScaleBalancing([[3, 4], [1, 2, 7, 7]])
ScaleBalancing([[13, 4], [1, 2, 3, 6, 14]])

exit()

def ScaleBalancing(strArr):

    weights = strArr[0]
    weights.sort()
    # print weights

    addWeights = strArr[1]
    sumWeights = []

    for w in weights:
        sumWeight = [w]
        for aw in addWeights:
            sumWeight.append(w + aw)

        sumWeights.append(sumWeight)
    print sumWeights

    for sumWeight in sumWeights[0]:
        pass

    # while i < len(sumWeights[0]):
    for ww in sumWeights[0]:

        # print ww
        try:
            ss = sumWeights[1].index(ww)
            print ww, ss
            # print sumWeights[1][ss] - addWeights[ss]         #, ss, addWeights[ss]
            break
        #     found = 1
        #
        #     print sumWeight
        #     break

        except:
            print "nincs"


        # if sumWeight in sumWeights[1]:

    # code goes here
    return strArr

# keep this function call here
# print ScaleBalancing(raw_input())
ScaleBalancing([[3, 4], [1, 2, 7, 7]])

exit()



def duplicates(arr):

    # our hash table to store each element
    # in the list as we pass through it
    hashTable = {}

    # store duplicates
    dups = []

    # check each element in the array
    for i in range(0, len(arr)):

        # if element does not exist in hash table
        # then insert it
        if arr[i] not in hashTable:
            hashTable[arr[i]] = True

        # if element does exist in hash table
        # then we know it is a duplicate
        else:
            dups.append(arr[i])

    print hashTable
    return dups

print duplicates([1, 21, -4, 103, 21, 4, 1])

exit()
# 13

ff = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

print ff[1][3]
exit()

def PentagonalNumber(num):

    pNum = 1
    for tt in range(int(num)):
        n = tt + 1
        currPNum = (n - 1) * 5
        pNum += currPNum

    # code goes here
    return pNum

# keep this function call here
print PentagonalNumber(raw_input())

exit()

# 12

# 0111
# 1101
# 0111
#
# 0111
# 1111
# 1101
# 1101
#
# 11000
# 10111
# 11111
# 00111

def MaximalSquare(strArr):
    # inp = ["0111", "1111", "1111", "0011"]
    inp = ["10100", "10111", "11111", "00111"]
    rowNum = len(inp)
    colNum = len(inp[0])

    print 'rowNum: ', rowNum, 'colNum: ', colNum, "\n"

    ss = []
    firstBitLoc = 0
    bitNum = 0

    for number in inp:
        i = 1
        firstBitLoc = 0
        bitNum = 0
        isNull = False

        for char in number:
            if char == "1":
                if firstBitLoc == 0:
                    firstBitLoc = i
                    bitNum += 1
                else:
                    bitNum += 1
                # print i, char, bits
            else:
                isNull = True
                if firstBitLoc > 0:
                    if bitNum > 1:
                        pass
                    else:
                        pass
                    # firstBitLoc = 0
            i += 1
        ss.append([firstBitLoc, bitNum])

        print number,
        print 'First bit location: ', firstBitLoc, 'Number of bits: ', bitNum

        # print ss
    # code goes here
    return strArr

# keep this function call here
# print MaximalSquare(raw_input())
MaximalSquare(1)

exit()



# 11
def fac(num):
    result = 1
    for i in range(2,num+1):
        result *= i
    return result


def ChessboardTraveling(stri):
    # a = int(stri[6])-int(stri[1])
    # b = int(stri[8])-int(stri[3])

    a = 1
    b = 7

    # return fac(a+b)/fac(a)/fac(b)
    print fac(a+b)/fac(a)/fac(b)

# keep this function call here
# to see how to enter arguments in Python scroll down
# print ChessboardTraveling(raw_input())
ChessboardTraveling(1)

exit()

# 11
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

