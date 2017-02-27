import os, myFunctions

fileName = input("Enter a file name: ")

extPos = myFunctions.PositionsOfLetterInString(fileName,".")

if (fileName[extPos[0]-1:extPos[0]] == "!"):
    docNumber = myFunctions.DOCSEnh2Num(fileName)
    print("Enhanced: Document number is: %s"%docNumber)
elif (fileName[extPos[0]-1:extPos[0]] == "_"):
    docNumber = myFunctions.DOCSUnix2Num(fileName)
    print("Unix: Document number is: %s"%docNumber)
else:
    print("This is not a valid file name!")


# file name to test: 2801!.docx = 80 | 5jp01!.wpd = 7189 | 7w201_.xls = 7490