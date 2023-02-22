#this should be completed and turned in BEFORE class starts on Monday.  be kind to yourself and get it done in class.
#Matthew Boylan
#Casino.py
#Feb 21 2023
#tells you how long it takes to run out of money playing slot machines.

#import libraries  
import random

#get starting  # of quarters
print("
                              .-------.
                              |Jackpot|
                  ____________|_______|____________
                 |  __    __    ___  _____   __    |  
                 | / _\  / /   /___\/__   \ / _\ []| 
                 | \ \  / /   //  //  / /\ \\ \  []|  
                 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
                 | \__/\____/\___/   \/     \__/ []|
                 |===_______===_______===_______===|
                 ||*|  _    |*| _____ |*|  _    |*||
                 ||*| | \   |*||     ||*| | \   |*||
                 ||*| |_(_) |*||*BAR*||*| |_(_) |*||
                 ||*| (_)   |*||_____||*| (_)   |*|| __
                 ||*|_______|*|_______|*|_______|*||(__)
                 |===_______===_______===_______===| ||
                 ||*| _____ |*|  _    |*|  ___  |*|| ||
                 ||*||     ||*| | \   |*| |_  | |*|| ||
                 ||*||*BAR*||*| |_(_) |*|  / /  |*|| ||
                 ||*||_____||*| (_)   |*| /_/   |*|| ||
                 ||*|_______|*|_______|*|_______|*||
                 |===___________________________===|
                 |  /___________________________\  |
                 |   |                         |   |
                _|    \_______________________/    |_
               (_____________________________________)
")
quarters = int(input("How many quarters did you bring the casino, my dude?: "))



#generate variables, generate a random number to act as luck (to win), and track plays
plays = 0
gameAplays = random.randint(0,34)
gameBplays = random.randint(0,99)
gameCplays = random.randint(0,9)
maxquarters = quaters

#start the game loop
while quarters > 0:
    plays += 1

    #check machine A to see if it pays out
    if gameAplays == 34:
        quarters += 30
        gameAplays = 0
        print(f"Nice, you just won 30 quarters on machine A! you now have {quarters} quarters left! ")
        if quarters > maxquarters:
        quarters = maxquarters
    #lets check machine B, lets see if its you're in luck
    if gameBplays == 99:
        quarters += 60
        gameBplays = 0
        print(f"Damn, you just hit jackpot on machine B and just won 60 more quarters, you now have {quarters} quarters left! ")
        if quarters > maxquarters:
        quarters = maxquarters
    #Lets check machine C, are you excited?
    if gameCplays == 9:
        quarters += 10
        gameCplays = 0
        print(f"Oh snap, you just won 9 quarters on machine C! You now have {quarters} quarters left!")
    if quarters > maxquarters:
        quarters = maxquarters

    #pay a quarter for each play, and also slowly add plays to the machines until they hit their payout.
    quarters -= 1
    gameAplays += 1
    gameBplays += 1
    gameCplays += 1

#print the net results, may the odds be in your favour next time my friend
print(f"Ahhh, you finnally ran out of quarters my friend? Dont worry - the house always wins, am I right? But hey, you peaked with {maxquarters} quarters, so thats pretty good. ")
print("Until next time, keep hustling, and stay cool!")