# The Casting of Lots
# Jack Tillotson, Program 9, 10/30/2013


# Import the function random
import random

#**************************
# MODULE : rules
# DEF : To display the rules when the progam first starts.
#**************************
def rules():
    print("The rules of the game are simple!")
    print("There are two types of bets to be made! Pass or Field bet.")
    print()
    print("A field bet is won when a player rolls 2, 3, 4, 9, 10, 11, 12.")
    print("2 and 12 win double while anything else is a loss.")
    print()
    print("A pass bet is lost with a 7 or an 11, and won with a 2 or a 12")
    print("If any other number is rolled then that number becomes 'Point.'")
    print("You win if you reroll the Point or lose with a 7 or an 11.")
    print()
    print("Well now that you know how to play, lets get started!")

#***************************
# MODULE : openTalents
# INPUTS : none
# OUTPUTS : talents
# DEF : To open the file to get the talents
#***************************
def openTalents():
    talentsFile = open('talents.txt', 'r')
    talents = int(talentsFile.readline())
    talentsFile.close()
    return talents

#***************************
# MODULE : saveTalents
# INPUTS : talents
# OUTPUTS : none
# DEF : Saves the talents for when game is next played
#***************************
def saveTalents(talents):
    talentsFile = open('talents.txt', 'w')
    talentsFile.write(str(talents) + '\n')
    talentsFile.close()

#***************************
# MODULE : startOver
# INPUTS : none
# OUTPUTS : talents
# DEF : To reset talents when the player runs out
#***************************
def startOver():
    print("Sorry you have no more money left, maybe you shouldn't gamble...")
    
    talentsFile = open('talents.txt', 'w')
    talentsFile.write(str(100) + '\n')
    talentsFile.close()

    print("But you seem like an alright chap.")
    print("Maybe I'll let you try again starting from the bottom!")

    talentsFile = open('talents.txt', 'r')
    talents = int(talentsFile.readline())
    talentsFile.close()

    return talents

#***************************
# MODULE : menu
# INPUTS : talents
# OUTPUTS : choice
# DEF : To get the choice of bet or to quit from the user
#***************************
def menu(talents):
    
    print("Welcome to the casting of lots!")
    print("Here are the talents you have to play with: ", talents)
    print("1 - Field Bet\n2 - Pass Bet\n3 - Quit")
    
    choice = int(input("Choice --------------------------- "))
    
    while choice not in [1, 2, 3]:
        
        print("\nPlease choose either choice 1, 2, or 3.\n")
        print("Welcome to the casting of lots!")
        print("Here are the talents you have to play with: ", talents)
        print("1 - Field Bet\n2 - Pass Bet\n3 - Quit")
        
        choice = int(input("Choice --------------------------- "))
    
    return choice

#***************************
# MODULE : talentsBank
# INPUTS : talents, winLose
# OUTPUTS : talents
# DEF : This function holds the variable talents
#       and the user's winnings and losings are sent in.
#***************************
def talentsBank(talents, winLose):
    talents += winLose
    return talents

#***************************
# MODULE : talentsBet
# INPUTS : talents
# OUTPUTS : wager
# DEF : To determine how many talents the user would like to bet.
#***************************
def talentsBet(talents):
    wager = int(input("How much do you wish to wager? "))
    
    while wager < 0 or wager > talents:
        
        if wager < 0:
            print("You can't wager less than 0 you goofball, try again.")
            wager = int(input("How much do you wish to wager? "))
            
        elif wager > talents:
            print("You can't wager money you don't have!")
            wager = int(input("How much do you wish to wager? "))
            
    return wager


#***************************
# MODULE : fieldBet
# INPUTS : wager
# OUTPUTS : winLose
# DEF : Preforms the rolls for the choice of field bet
#       and returns whats is lost or won.
#***************************
def fieldBet(wager):
    
    lot = random.randint(1, 6) + random.randint(1, 6)
    
    if lot in [2, 12]:
        winLose = wager * 2
        
    elif lot in [3, 4, 9, 10, 11]:
        winLose = wager
        
    else:
        winLose = wager * (-1)
        
    print("You rolled", lot)
    
    return winLose


#***************************
# MODULE : passBet
# INPUTS : wager
# OUTPUTS : winLose
# DEF : Preforms the rolls for the choice of pass bet
#       and returns what is lost or won.
#***************************
def passBet(wager):
    
    lot = random.randint(1, 6) + random.randint(1, 6)
    
    if lot in [7, 11]:
        winLose = wager * (-1)
        print("You rolled", lot)
        
    elif lot in [2, 12]:
        winLose = wager
        print("You rolled", lot)
        
    else:
        point = lot
        print("You rolled a POINT!  The point is", point)
        input("Press enter to roll again. ")
        rollPoint = random.randint(1, 6) + random.randint(1, 6)
        
        if rollPoint in [7, 11]:
                winLose = wager * (-1)
                
        elif rollPoint == point:
                winLose = wager
        print("You rolled", rollPoint)
        
        while rollPoint != 7 and rollPoint != 11 and rollPoint != point:
            input("Press enter to roll again. ")
            rollPoint = random.randint(1, 6) + random.randint(1, 6)
            print("You rolled", rollPoint)
            
            if rollPoint in [7, 11]:
                winLose = wager * (-1)
                
            elif rollPoint == point:
                winLose = wager
                
    return winLose


#***************************
# MODULE : showOutputs
# INPUTS : winLose, talents
# OUTPUTS : none
# DEF : Show the winnings or losses and new total of talents.
#***************************
def showOutputs(winLose, talents):
    
    if winLose > 0:
        print("You won ", winLose, "!", sep = '')
        print("Now you have", talents)
        
    else:
        print("You lost ", winLose * (-1), "!", sep = '')
        print("Now you have", talents)
        
#***************************
# MODULE : main
# DEF : Calls functions of the program.
def main():

    # Display Rules
    rules()
    
    # Open the file holding the talents
    talents = openTalents()

    # Declaring variables
    choice = 0
    wager = 0
    winLose = 0
    
    while choice != 3:

        if talents < 1:
            talents = startOver()
        
        choice = menu(talents)
        
        if choice == 1:
            wager = talentsBet(talents)
            winLose = fieldBet(wager)
            talents = talentsBank(talents, winLose)
            showOutputs(winLose, talents)
            
        if choice == 2:
            wager = talentsBet(talents)
            winLose = passBet(wager)
            talents = talentsBank(talents, winLose)
            showOutputs(winLose, talents)
            
        if choice == 3:
            saveTalents(talents)
            
        
            
main()
