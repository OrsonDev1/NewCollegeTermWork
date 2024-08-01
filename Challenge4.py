# importing the modules we need
import random
import time
import pickle as pkl
import json

# setting player values to zero
p1score = 0
p2score = 0
p1pass = 0
p2pass = 0
p1authPass = 0
p2authPass = 0
# pycharm complains if I don't define them, so im just going define them here
dice1 = 0
dice2 = 0
dice3 = 0
# we only want to have extraDice been true if we use it
extraDice = False
maxRounds = 5
roundsPassed = 0
winningScore = 0
endScoring = 0
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

# easier to make something we can call for when we need to roll a single dice
def singleDice():
    global dice3
    dice3 = random.randint(1, 6)

# the authentication program I made, it takes the name given, which is stored in one half of a 2D array, it then finds the position of this name, and looks at the key in the same position on the other array.
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

# this double checks to make sure that the authentication was actually passed, an attempt to prevent circumvention
def authenticationDoubleCheck():
    # double-checking there are no unauthenticated players
    global p1authPass
    global p2authPass
    if p1authPass == 0 or p2authPass == 0:
        print("Either player has failed authentication check, please try again")
        exit(1)

# this is my scoreboard system, where we can import the scoreboard, add the new winningName, add the winningScore, sort it so that we have the highest first, then we remove all the scores but the top 5, and save that to the json file.
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

    return top_scores

# the main game, we call to roll two dice, then get the total, and add the total to the 'endScore'
def maingame():
    global endScoring
    global extraDice
    endScoring = 0
    rollDosDice()
    total = dice1 + dice2
    endScoring = total
    # we see if we have rolled a double, if we have then we roll the third dice and add that dice roll to the total score
    if dice1 == dice2:
        singleDice()
        endScoring = endScoring + dice3
        extraDice = True
    # if even, + 10 to the score
    if total % 2 == 0:
        endScoring = endScoring + 10
        print("Even Total! Your score was increased by 10!")
    # if odd, -5 from the score
    elif total % 2 != 0:
        endScoring = endScoring - 5
        print("Odd Total, Your score was decreased by 5 :(")
    # just incase, we quit nicely (I doubt it will be used but defensive design)
    else:
        print("Unexpected error, please try again")
        exit(1)


# inputting the player name, and authentication key, making sure that the name given is titled, so the first letter is capital. Do this for both players
p1name = input("Player One Name: ")
p1name = p1name.title()
p1authKey = input("Player One Authentication Key")
p2name = input("Player Two Name: ")
p2name = p2name.title()
p2authKey = input("Player Two Authentication Key ")
# making sure people don't try face themselves
if p1name == p2name:
    print("You cant face yourself!")
    exit(1)
# we make sure the players auth key and name is correct, and then we check that it was successful passed (probably unnecessary but worth a check)
authenticationCheck()
authenticationDoubleCheck()
# makes it more readable
print("-----------------------------------------")
time.sleep(1)
# we run this for 5 times (maxRounds is 5, using a variable, so it can be easily changed if needed)
while roundsPassed < maxRounds:
    # telling the user how many rounds had passed.
    print("Round: ", roundsPassed+1)
    print("--------")
    print("Player 1 roll")
    # calling the main game, the making sure each users score is kept for each user
    maingame()
    p1score = p1score + endScoring
    # print out scores and dice rolls
    if extraDice:
        print("Player 1 rolled", dice1, ",", dice2, "and", dice3, "and has a total score of", p1score)
        extraDice = False
    else:
        print("Player 1 rolled", dice1, "and", dice2, "and has a total score of", p1score)
    # make it seem more human, and easier to read
    print("-----------")
    time.sleep(2)
    # same thing for player 2, I cant find an easy way to simplify this even though it is a bit dry
    print("Player 2 roll")
    maingame()
    p2score = p2score + endScoring
    if extraDice:
        print("Player 2 rolled", dice1, ",", dice2, "and", dice3, "and has a total score of", p2score)
        extraDice = False
    else:
        print("Player 2 rolled", dice1, "and", dice2, "and has a total score of", p2score)
    # make it seem more human, and easier to read

    # checking the score isn't too low, if it's below zero, then we quit
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

# if it is a draw, we roll another dice for each player until the scores are different
while p1score == p2score:
    print("Draw!")
    singleDice()
    p1score = p1score + dice3
    singleDice()
    p2score = p2score + dice3
    print("-----------")
    time.sleep(2)

# announcing the final scores
print("Final Score for Player 1: ", p1score)
print("Final Score for Player 2: ", p2score)
time.sleep(1)

# saying who won the game, and what score.
if p1score > p2score:
    print("Player 1", p1name, "has won with a score of", p1score)
    winningScore = p1score
    winningName = p1name
elif p2score > p1score:
    print("Player 2", p2name, "has won with a score of", p2score)
    winningScore = p2score
    winningName = p2name
else:
    print("An unexpected error has occurred")
    exit(1)
time.sleep(1)
# saving the scoreboard, then printing out what the scoreboard is
scoreboardSystem()
with open('scoreboard.json', 'r') as scoreFile:
    scores = json.load(scoreFile)
for score in scores:
    print(f"{score['name']}: {score['score']}")
