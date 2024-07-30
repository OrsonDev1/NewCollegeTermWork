# Entering the variables we need
gate = input("What logic gate you do want?")
var1 = int(input("What is your first input: "))
var2 = int(input("What is your second input: "))
# Making sure the gate input is in caps
gate = gate.upper()

# I feel most of this is self-explanatory but i will explain

if gate == "AND":
    # if the variable one and 2 both equal one, then the result is one
    if var1 == 1 and var2 == 1:
        result = 1
    else:
        # if not, then it is equal to zero
        result = 0
# if one of the variables is one, then the result is one,
elif gate == "OR":
    if var1 == 1 or var1 == 1:
        result = 1
    else:
        result = 0
# if either variables are equal to 1, then the result is 0, if not then it is 1
elif gate == "NOR":
    if var1 == 1 or var2 ==1:
        result = 0
    else:
        result = 1
# if both variables are equal to 1, then the result is zero, if either one or two, but not both(will be caught out by the first part of the if statement) then the result is zero, if not then the result is 0
elif gate == "XOR":
    if var1 == 1 and var2 == 1:
        result = 0
    elif var1 == 1 or var2 == 1:
        result = 1
    else:
        result = 0
# if both are 1, then the result if zero, if both are not 1 then the result is 1
elif gate == "NAND":
    if var1 == 1 and var2 ==1:
        result = 0
    else:
        result = 1
# making sure that it is not am invalid answer
else:
    print("Invalid gate, try again")
    exit(1)
# print the result
print("Answer is", result)
