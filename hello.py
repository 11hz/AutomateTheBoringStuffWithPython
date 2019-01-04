# This program says hello and asks for my name

print('Hello World!')

print('What is your name?') #ask for their name
myName = input ()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #ask for their age
myAge = input ()
print (myName + ', you will be ' + str(int(myAge) + 1) + ' in a year.')

# Pound signs are comments; Blank lines are ignored

# input() function waits for interactive user input

#Recap:
# - Type programs into an editor
# - The execution starts at the top and moves down
# - # Comments are ignored by Python
# - Functions are mini-programs in your program
# - print() displays the value passed to it
# - input() lets user type in a value
# - len() takes a string value and returns an interger value of the string's length
# - int(), str(), and float() convert values' data type
