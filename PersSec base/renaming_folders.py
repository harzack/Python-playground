import os, myFunctions

# listing directories and stores it in an array:
dirList = os.listdir(os.getcwd())
 
# display the number of items in the directory:
dirSize = len(dirList)
print("Directory Size: %s"%dirSize)
nChanges = 0

# loop in directory names (folders) to rename them
for i in range(dirSize):

    # Count number of spaces in the current directory item:
    nbSpace = myFunctions.NumberOfLetterInString(dirList[i], " ")
    # Initializes new name for current directory item:
    subDirName = []

    # Performs changes only if there is 2 spaces in the name, ignore the other cases:
    if nbSpace == 2:
        # remove all commas in current folder name:
        oldName = dirList[i]
        dirList[i] = myFunctions.RemoveLetterInString(dirList[i],",")
        os.rename(oldName,dirList[i])
        # Increments number of changes made:
        nChanges = nChanges + 1
        # Initializes the starting space position cursor:
        sPosition = 0
        # Collects all spaces positions in the current directory item:
        endSpos = myFunctions.PositionsOfLetterInString(dirList[i], " ")
        # Cuts current directory name in words based on space positions:
        for j in range(nbSpace + 1):
            subDirName.append(dirList[i][sPosition:endSpos[j]])
            sPosition = endSpos[j] + 1
        # checks if first 2 parts of the name are uppercase or not:
        if (subDirName[0].isupper() and subDirName[1].isupper()):
            newName = subDirName[0] + ' ' + subDirName[1] + ', ' + subDirName[2]
            #print("Two LAST names then: %s"%newName)
            os.rename(dirList[i],newName)
        else:
            newName = subDirName[0] + ', ' + subDirName[1] + ' ' + subDirName[2]
            #print("One LAST name then: %s"%newName)
            os.rename(dirList[i],newName)
    elif nbSpace == 3:
        # remove all commas in current folder name:
        oldName = dirList[i]
        dirList[i] = myFunctions.RemoveLetterInString(dirList[i],",")
        os.rename(oldName,dirList[i])
        nChanges = nChanges + 1
        sPosition = 0
        endSpos = myFunctions.PositionsOfLetterInString(dirList[i], " ")
        #print("Space positions = %s"%endSpos)
        for j in range(nbSpace + 1):
            #print('Name ' + str(j + 1) + ' is: ' + dirList[i][sPosition:endSpos[j]])
            subDirName.append(dirList[i][sPosition:endSpos[j]])
            sPosition = endSpos[j] + 1
        # checks if first 2 parts of the name are uppercase or not:
        if (subDirName[0].isupper() and subDirName[1].isupper() and subDirName[2].isupper()):
            newName = subDirName[0] + ' ' + subDirName[1] + ' ' + subDirName[2] + ', ' + subDirName[3]
            # print("Three LAST names then: %s"%newName)
            os.rename(dirList[i],newName)
        elif (subDirName[0].isupper() and subDirName[1].isupper()):
            newName = subDirName[0] + ' ' + subDirName[1] + ', ' + subDirName[2] + ' ' + subDirName[3]
            # print("Two LAST names then: %s"%newName)
            os.rename(dirList[i],newName)
        else:
            newName = subDirName[0] + ', ' + subDirName[1] + ' ' + subDirName[2] + ' ' + subDirName[3]
            # print("One LAST name then: %s"%newName)
            os.rename(dirList[i],newName)
 
print("Number of names updated: %s"%nChanges)
