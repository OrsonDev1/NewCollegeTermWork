import random

p1score = 0
p2score = 0
p1pass = 0
p2pass = 0
playerskeys = [["Steve", "Orson"], ["b098","a123"]]
def rolldosdice():
    global dice1
    global dice2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)

def scorecheck():
    print("will work on later")
def authenticationcheck():
    if any(p1name in sublist for sublist in playerskeys):
        number = playerskeys[0].index(p1name)
        print("num",number)
        if p1authkey == playerskeys[1][number]:
            global p1pass
            p1pass = 1
            print("Player 1 passed auth check")
        else:
            print("Player 1 failed auth check")
    else:
        print("Player 1 failed name check")
    if any(p2name in sublist for sublist in playerskeys):
        number2 = playerskeys[0].index(p1name)
        if p2authkey == playerskeys[1][number2]:
            print("Through key check")
            global p2pass
            p2pass = 1
        else:
            print("Player 2 failed auth check")
    else:
        print("Player 2 failed name check")




p1name = input("Player One Name: ")
p2name = input("Player Two Name: ")
p1authkey = input("Player One Authentication Key")
p2authkey = input("Player Two Authentication Key ")
authenticationcheck()
print("p1", p1pass)
print("p2", p2pass)