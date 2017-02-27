import os, myFunctions

function = input("Convert a file name (F) or number (N): ")

# file names to test:
# 2801!.docx = 80
# 5jp01!.wpd = 7189
# 7w201_.xls = 7490


if function == "F":
    fileName = input("Enter a file name: ")
    extPos = myFunctions.PositionsOfLetterInString(fileName, ".")

    if fileName[extPos[0]-1:extPos[0]] == "!":
        docNumber = myFunctions.DOCSEnh2Num(fileName)
        print("Enhanced: Document number is: %s" % docNumber)
    elif fileName[extPos[0]-1:extPos[0]] == "_":
        docNumber = myFunctions.DOCSUnix2Num(fileName)
        print("Unix: Document number is: %s" % docNumber)
    else:
        print("This is not a valid file name!")

elif function == "N":
    version = input("Enter a version number: ")
    extension = input("Enter the extension of the file name: ")
    if version.isnumeric():
        version = int(version)
        try:
            docNumber = int(input("Enter a doc number: "))
        except ValueError:
            print("the document number is not a number!")
        else:
            if version < 10:
                sVersion = str(version).rjust(2, '0')
            else:
                sVersion = str(version)
            filename = myFunctions.Num2DOCSEnh(docNumber).lower()
            print("The enhanced file name is: %s" % filename + sVersion + "!" + "." + extension)
            filename = myFunctions.Num2DOCSUnix(docNumber).lower()
            print("The unix file name is: %s" % filename + sVersion + "_" + "." + extension)
    else:
        print("Version should be a number...")
else:
    print("You didn't chose a valid option...")
