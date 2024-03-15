__author__ = 'alex'

# with open('test.txt', 'r') as test_file_r:
#     print(test_file_r.read())

test_file_w = open('test.txt', 'a')

''' Opening a file:
Character   Meaning 
'r'         open for reading (default)
'w'         open for writing, truncating the file first
'x'         open for exclusive creation, failing if the file already exists
'a'         open for writing, appending to the end of file if it exists
'b'         binary mode
't'         text mode (default)
'+'         open for updating (reading and writing)
'''

test_file_w.write("newer content: \n")
test_file_w.write('This line is added by Python twice\n')
test_file_w.write('another line thrice\n')
test_file_w.close()

# test_file.write(content)