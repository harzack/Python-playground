import re


# function to count the number of specified letter found in a string:
def NumberOfLetterInString (dname, dletter):
    nletter = 0
    for i in range(len(dname)):
        if dname[i] == dletter:
            nletter += 1
    return nletter


# function returning the positions of each specified letter in a string, and last position is length of string:
def PositionsOfLetterInString(dname, dletter):
    sPos = []
    for i in range(len(dname)):
        if dname[i] == dletter:
            sPos.append(i)
    sPos.append(len(dname)+1)
    return sPos

# Function removing the specified letter in a string
def RemoveLetterInString(dname, dletter):
    nString = ""
    for i in range(len(dname)):
        if dname[i] != dletter:
            nString += dname[i]
    return nString


# The next 4 functions convert eDOCS file names to doc numbers and vice versa for both unix and enhanced filing scheme:

# Converts document number and version to DOCS filename using enhanced filing scheme:
def Num2DOCSEnh(docnum):
    filename = ""
    docnum = int(docnum)

    # Calculate file name from doc number
    while docnum >= 1:
        mod36 = docnum % 36
        # print("mod36 is: %d" % mod36)
        if mod36 < 10:
            filename += str(int(mod36))
        elif mod36 == 10:
            filename += "@"
        elif mod36 == 14:
            filename += "#"
        elif mod36 == 18:
            filename += "$"
        elif mod36 == 24:
            filename += "_"
        elif mod36 == 30:
            filename += "%"
        else:
            filename += chr(int(mod36) + 55)
        docnum = (docnum - mod36) / 36

    return filename.strip()[::-1]


# Converts document number and version to DOCS filename using UNIX filing scheme
def Num2DOCSUnix(docnum):
    filename = ""
    docnum = int(docnum)

    # Calculate file name from doc number
    while docnum >= 1:
        mod32 = docnum % 32
        if mod32 < 10:
            filename += str(int(mod32))
        elif mod32 == 10:
            filename += "W"
        elif mod32 == 14:
            filename += "X"
        elif mod32 == 18:
            filename += "Y"
        elif mod32 == 24:
            filename += "Z"
        elif mod32 == 30:
            filename += "_"
        else:
            filename += chr(int(mod32) + 55)
        docnum = (docnum - mod32) / 32

    return filename.strip()[::-1]


# Convert DOCS filename to document number using enhanced filing scheme
def DOCSEnh2Num(filename):
    docnum = 0
    numbersRegex = re.compile(r'\d')
    lettersRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')

    # Remove file extension and last 3 digits (version info and filing scheme)
    extPos = PositionsOfLetterInString(filename, ".")
    filename = filename[0:(extPos[0])-2]

    # Calculate doc number from characters
    for j in range(1, len(filename)):
        docnum *= 36
        c = filename[j-1:j].upper()
        if numbersRegex.search(c) is not None:
            docnum += int(c)
        elif lettersRegex.search(c) is not None:
            docnum = docnum + ord(c) - 55
        elif c == "@":
            docnum += 10
        elif c == "#":
            docnum += 14
        elif c == "$":
            docnum += 18
        elif c == "_":
            docnum += 24
        elif c == "%":
            docnum += 30
        else:
            docnum = 0
    return str(docnum)


# Convert DOCS filename to document number using unix filing scheme
def DOCSUnix2Num(filename):
    docnum = 0
    numbersRegex = re.compile(r'\d')
    lettersRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUV]')

    # Remove file extension and last 3 digits (version info and filing scheme)
    extPos = PositionsOfLetterInString(filename, ".")
    filename = filename[0:(extPos[0])-2]

    # Calculates doc number from characters
    for j in range(1, len(filename)):
        docnum *= 32
        c = filename[j-1:j].upper()
        if numbersRegex.search(c) is not None:
            docnum += int(c)
        elif lettersRegex.search(c) is not None:
            docnum = docnum + ord(c) - 55
        elif c == "W":
            docnum += 10
        elif c == "X":
            docnum += 14
        elif c == "Y":
            docnum += 18
        elif c == "Z":
            docnum += 24
        elif c == "_":
            docnum += 30
        else:
            docnum = 0
    return str(docnum)
