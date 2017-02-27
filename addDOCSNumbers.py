import re, myFunctions, datetime
# captures starting time
starTime = datetime.datetime.now()
# declares the file name to open:
inputFile = "documents_list.txt"
# declares the file name to write to:
exportFile = "documents_list_converted.txt"

# regex expressions to match:
# end of lines to split the file names:
linesRegex = re.compile(r'.+\n')
# underscores for enhanced filing scheme:
unixRegex = re.compile(r'_\.')
# exclamation mark for unix filing scheme:
enhRegex = re.compile(r'!\.')
# in case needed, the last name
#lastNameRegex = re.compile(r'.+$')

# opening the file to read and dump it in a list variable:
fileLetters = open(inputFile).read()
# opening the destination file in write mode:
convertedFile = open(exportFile,'w')
# using the regex to split all document names in chunks based on the end of line \n:
fileNames = linesRegex.findall(fileLetters)
# captures and displays the number of documents processed:
numberNames = len(fileNames)

# loop for each document in the file:
for i in range(0,numberNames):
    # removes the last 2 letters (the \n, new line character) and stores it in the current name:
    currentName = fileNames[i][0:len(fileNames[i])-2]
    # based on the filing scheme, call the proper function in myFunctions, and write in the destination file:
    if unixRegex.search(currentName) == None:
        docNumber = myFunctions.DOCSEnh2Num(currentName)
        convertedFile.write(currentName + '; ' + str(docNumber) + '\n')
    elif enhRegex.search(currentName) == None:
        docNumber = myFunctions.DOCSUnix2Num(currentName)
        convertedFile.write(currentName + '; ' + str(docNumber) + '\n')
    else:
        convertedFile.write(currentName + '; Not a valid name' + '\n')
# captures the end of processing time, and displays the elapsed time for completion:
endTime = datetime.datetime.now()
timeElapsed = endTime - starTime
print('Completed ' + str(numberNames) + ' document names in: ' + str(timeElapsed.seconds) + ':' + str(timeElapsed.microseconds) + ' seconds')