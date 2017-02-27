__author__ = 'alex'

# This program says hello and ask for my name.

print('Hello, world!')
print('What is your name?')  # asks for the name
myName = input()
print('It\'s good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # asks for the age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
