#Logic gates woo
gate = input("What logic gate you do want?")
var1 = int(input("What is your first input: "))
var2 = int(input("What is your second input: "))

gate = gate.upper()
if gate == "AND":
    if var1 == 1 and var2 == 1:
        result = 1
    else:
        result = 0
elif gate == "OR":
    if var1 == 1 or var1 == 1:
        result = 1
    else:
        result = 0
elif gate == "NOR":
    if var1 == 1 or var2 ==1:
        result = 0
    else:
        result = 1
elif gate == "XOR":
    if var1 == 1 and var2 == 1:
        result = 0
    elif var1 == 1 or var2 == 1:
        result = 1
    else:
        result = 0
elif gate == "NAND":
    if var1 == 1 and var2 ==1:
        result = 0
    else:
        result = 1
else:
    print("Invalid gate, try again")
    exit(1)

print("Answer is", result)
