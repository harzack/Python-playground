import re

# function returning the positions of each spaces in a string, and last position is length of string:
def PositionsOfLetterInString(dName, dLetter):
    sPos = []
    for i in range(len(dName)):
        if (dName[i] == dLetter):
            sPos.append(i)
    sPos.append(len(dName)+1)
    return (sPos)

#Convert DOCS filename to document number using enhanced filing scheme
def DOCSEnh2Num(FileName):
    docNum = 0
    numbersRegex = re.compile(r'\d')
    lettersRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')

    # Remove file extension and last 3 digits (version info and filing scheme)
    extPos = PositionsOfLetterInString(FileName,".")
    print('The document ' + FileName + ' has: ' + str(len(FileName)) + ' letters and the . is at position:  ' + str(extPos))
    FileName = FileName[0:(extPos[0])-2]

  # Calculate doc number from characters
    for j in range(1,len(FileName)):
        docNum = docNum * 36
        c = FileName[j-1:j].upper()
        if numbersRegex.search(c) != None:
            docNum = docNum + int(c)
        elif lettersRegex.search(c) !=None:
            docNum = docNum + ord(c) - 55
        elif c == "@":
            docNum = docNum + 10
        elif c == "#":
            docNum = docNum + 14
        elif c == "$":
            docNum = docNum + 18
        elif c == "_":
            docNum = docNum + 24
        elif c == "%":
            docNum = docNum + 30
        else:
            docNum = 0
    return(str(docNum))

# Convert DOCS filename to document number using unix filing scheme
def DOCSUnix2Num(FileName):
    docNum = 0
    numbersRegex = re.compile(r'\d')
    lettersRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUV]')

    # Remove file extension and last 3 digits (version info and filing scheme)
    extPos = PositionsOfLetterInString(FileName,".")
    print('The document ' + FileName + ' has: ' + str(len(FileName)) + ' letters and the . is at position:  ' + str(extPos))
    FileName = FileName[0:(extPos[0])-2]

  # Calculate doc number from characters
    for j in range(1,len(FileName)):
        docNum = docNum * 32
        c = FileName[j-1:j].upper()
        if numbersRegex.search(c) != None:
            docNum = docNum + int(c)
        elif lettersRegex.search(c) !=None:
            docNum = docNum + ord(c) - 55
        elif c == "W":
            docNum = docNum + 10
        elif c == "X":
            docNum = docNum + 14
        elif c == "Y":
            docNum = docNum + 18
        elif c == "Z":
            docNum = docNum + 24
        elif c == "_":
            docNum = docNum + 30
        else:
            docNum = 0
    return(str(docNum))