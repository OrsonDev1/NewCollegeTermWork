import random
import time
import pickle as pkl
import json

# setting most values to zero, that need to be reset
p1score = 0
p2score = 0
p1pass = 0
p2pass = 0
p1authPass = 0
p2authPass = 0
# pycharm complains so im just going define them here
dice1 = 0
dice2 = 0
dice3 = 0
extraDice = False
maxRounds = 5
roundsPassed = 0
winningScore = 0
scores = []

# reads the authentication names and keys off of the .pkl file, saves it in the array
with open('authentication.pkl', 'rb') as f:
    playersKeys = pkl.load(f)

# rolling two dice, easier to do through a subroutine, so you can call it again.
def rollDosDice():
    global dice1
    global dice2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

def singleDice():
    global dice3
    dice3 = random.randint(1, 6)

def authenticationCheck():
    # if the player one name is anywhere in playersKeys, get where it is in the array
    if any(p1name in sublist for sublist in playersKeys):
        number = playersKeys[0].index(p1name)
        # the auth key will always be in the same column in the other array, so we check if the key matches up for that name
        if p1authKey == playersKeys[1][number]:
            # if it matches, we pass the auth check and p1 pass is true
            global p1authPass
            p1authPass = 1
            print("Player 1 passed auth check")
            # if not, we exit out of the program
        else:
            print("Player 1 failed auth check, please try again")
            exit(1)
    else:
        # if the name is not in the database, we quit
        print("Player 1 failed name check")
        exit(1)
    # do the same for player 2
    if any(p2name in sublist for sublist in playersKeys):
        number2 = playersKeys[0].index(p2name)
        if p2authKey == playersKeys[1][number2]:
            global p2authPass
            p2authPass = 1
            print("Player 2 Passed auth check")
        else:
            print("Player 2 failed auth check, please try again")
            exit(1)
    else:
        print("Player 2 failed name check")
        exit(1)

def scoreboardSystem():
    # Load the old scoreboard
    with open('scoreboard.json', 'r') as scoreFile:
        scores = json.load(scoreFile)

    # Add the new winning score
    scores.append({"name": winningName, "score": winningScore})
    scores.sort(key=lambda x: x["score"], reverse=True)

    # Keep only the top 5 scores
    top_scores = scores[:5]

    # Write the updated scores back to the file
    with open('scoreboard.json', 'w') as scoreFile:
        json.dump(top_scores, scoreFile, indent=4)

    print("Current top scores:")
    for score in scores:
        print(f"{score['name']}: {score['score']}")
    return top_scores


# inputting the player data, chose to use authentication keys to authenticate the players
p1name = input("Player One Name: ")
p1name = p1name.title()
p1authKey = input("Player One Authentication Key")
p2name = input("Player Two Name: ")
p2name = p2name.title()
p2authKey = input("Player Two Authentication Key ")
authenticationCheck()

# double-checking there are no unauthenticated players
if p1authPass == 0 or p2authPass == 0:
    print("Either player has failed authentication check, please try again")
    exit(1)
print("-----------------------------------------")
time.sleep(1)
# will run many times till 5 rounds have passed
while roundsPassed < maxRounds:
    # rolling the two dice
    print("Round: ", roundsPassed+1)
    print("--------")
    rollDosDice()
    total = dice1 + dice2
    p1score = total + p1score
    print("Player 1 roll")
    # working out the extra scores
    if dice1 == dice2:
        # if double, roll a third dice
        singleDice()
        p1score = p1score + dice3
        extraDice = True
    # if even, + 10
    if total % 2 == 0:
        p1score = p1score + 10
        print("Even Total! Your score was increased by 10!")
    # if odd, -5
    elif total % 2 != 0:
        p1score = p1score - 5
        print("Odd Total, Your score was decreased by 5 :(")
    # just incase
    else:
        print("Unexpected error, please try again")
        exit(1)
    # print out scores and dice rolls
    if extraDice:
        print("Player 1 rolled", dice1, ",", dice2, "and", dice3, "and has a total score of", p1score)
        extraDice = False
    else:
        print("Player 1 rolled", dice1, "and", dice2, "and has a total score of", p1score)
    # make it seem more human, and easier to read
    print("-----------")
    time.sleep(2)

    # do it all again for player 2
    rollDosDice()
    total = dice1 + dice2
    p2score = total + p2score
    print("Player 2 Roll")
    # working out the extra scores
    if dice1 == dice2:
        # if double, roll a third dice
        singleDice()
        p2score = p2score + dice3
        extraDice = True
    # if even, + 10
    if total % 2 == 0:
        p2score = p2score + 10
        print("Even Total! Your score was increase by 10!")
    # if odd, -5
    elif total % 2 != 0:
        p2score = p2score - 5
        print("Odd Total, Your score was decrease by 5 :(")
    # just incase
    else:
        print("Unexpected error, please try again")
        exit(1)
    # print out scores and dice rolls
    if extraDice:
        print("Player 2 rolled", dice1, ",", dice2, "and", dice3, "and has a total score of", p2score)
        extraDice = False
    else:
        print("Player 2 rolled", dice1, "and", dice2, "and has a total score of", p2score)
    # make it seem more human, and easier to read

    # checking the score isn't too low
    if p1score <= -1:
        print("P1 score has gone under 0, you lose")
        exit(1)
    elif p2score <= -1:
        print("P2 score has gone under 0, you lose")
        exit(1)
    print("-----------")
    time.sleep(2)
    # increased the amount of rounds passed, so we don't go forever
    roundsPassed = roundsPassed + 1

# if it is a draw,
while p1score == p2score:
    print("Draw!")
    singleDice()
    p1score = p1score + dice3
    singleDice()
    p2score = p2score + dice3
    print("-----------")
    time.sleep(2)

print("Final Score for Player 1: ", p1score)
print("Final Score for Player 2: ", p2score)

if p1score > p2score:
    print("Player 1 has won with a score of", p1score)
    winningScore = p1score
    winningName = p1name
elif p2score > p1score:
    print("Player 2 has won with a score of", p2score)
    winningScore = p2score
    winningName = p2name
else:
    print("An unexpected error has occurred")
    exit(1)

scoreboardSystem()
