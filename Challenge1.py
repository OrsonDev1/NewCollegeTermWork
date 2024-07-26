# Arrays
acceptedSymbols = ['X', 'x','*', '+', '-','/',]

# subroutines

# checks, making sure stuff is correct so we quit nicely
def symbolcheck(symbol):
    if symbol not in acceptedSymbols:
        print("Not a valid Symbol, sorry")
        exit(1)


# i would love to have all this in one subroutine, however the time i have spent on that was becoming far to great when i can get it to work
def addition():
    print(symbol + '\t' + '\t'.join([str(x) for x in range(number)]) + '\n')
    for y in range(number):
        print(y, end='\t')
        for z in range(number):
            print(str(y+z), end="\t")
        print('\n')

def subtraction():
    print(symbol + '\t' + '\t'.join([str(x) for x in range(number)]) + '\n')
    for y in range(number):
        print(y, end='\t')
        for z in range(number):
            print(str(y - z), end="\t")
        print('\n')

def multiplication():
    print(symbol + '\t' + '\t'.join([str(x) for x in range(number)]) + '\n')
    for y in range(number):
        print(y, end='\t')
        for z in range(number):
            print(str(y * z), end="\t")
        print('\n')
def division():
    print(symbol + '\t' + '\t'.join([str(x) for x in range(number)]) + '\n')
    for y in range(number):
        print(y, end='\t')
        for z in range(number):
            print(str(y / z), end="\t")
        print('\n')


# Data Input
symbol = input("What is the symbol you want to use? ")
# making sure the symbol is valid and making it quit nicely if not
symbolcheck(symbol)
number = int(input("What number do you want to go to?"))
# it cuts off the last number and this is just an easy workaround
number += 1


if symbol == '+':
    addition()
elif symbol == '-':
    subtraction()
elif symbol == '*' or symbol == 'x' or symbol == 'X':
    multiplication()
elif symbol == '/':
    print("this will never work right because you cant divide by 0")
    division()

