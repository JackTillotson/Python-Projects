# The game of NIM
# Jack Tillotson, 12/9/2013

#****************************
# MODULE :displayPlayer
# INPUT : player
# OUTPUT : none
# DEF : To display which players turn it is
#****************************
def displayPlayer(player):
    if player == 0:
        print("Your turn player 1!")
    else:
        print("Your turn player 2!")

#****************************
# MODULE : displayPiles
# INPUT : piles
# OUTPUT : none
# DEF : To display the piles each turn
#****************************
def displayPiles(piles):
    print("Pile 1 has:", piles[0])
    print("Pile 2 has:", piles[1])
    print("Pile 3 has:", piles[2])


#****************************
# MODULE : getPileChoice
# INPUT : piles
# OUTPUT : pileChoice
# DEF : To get from the user which pile to take from
#****************************
def getPileChoice(piles):
    pileChoice = -1
    while pileChoice == -1:
        try:
        
            while pileChoice < 1 or pileChoice > 3 or piles[pileChoice -1] == 0:
                pileChoice = int(input("Which pile do you want to take from(1, 2, or 3)? : "))
                if pileChoice > 3 or pileChoice < 1:
                    print("That is not a real pile.")

                elif piles[pileChoice -1] == 0:
                    print("That pile is empty, please choose another.")
        except ValueError:
            print("Please enter a number between 1 and 3.")
            pileChoice = -1
    return pileChoice -1


#****************************
# MODULE : getMoveAmount
# INPUT : piles, pileChoice
# OUTPUT : piles
# DEF : To get from the user how many stones to remove and return the new piles
#****************************
def getMoveAmount(piles ,pileChoice):
    moveAmount = -1
    maximum = int(piles[pileChoice] / 2)
    if maximum == 0:
        maximum = 1
    while moveAmount == -1:
        try:
            while moveAmount != 1 and (moveAmount > maximum or moveAmount < 1):
                moveAmount = int(input("How many stones would you like to take? : "))
                if moveAmount > maximum or moveAmount < 1:
                    print("You can't take out that number of stones.")
        except ValueError:
            print("Please enter a number.")
            moveAmount = -1
    piles[pileChoice] -= moveAmount
    return piles


#****************************
# MODULE : isWinner
# INPUT : piles, player
# OUTPUT : lose
# DEF : To determine the loser and display it
#****************************                    
def isLoser(piles, player):
    lose = False
    if piles == [0, 0, 0]:
        if player == 0:
            print("Player 1 Loses!")
            lose = True
        else:
            print("Player 2 Loses!")
            lose = True
    return lose


                
#****************************
# MODULE : setPlayer
# INPUT : player
# OUTPUT : player
# DEF : To switch between players each turn
#****************************
def setPlayer(player):
    if player == 0:
        player = 1
    elif player == 1:
        player = 0
    return player


#****************************
# MODULE : main
# DEF : To call the functions of the program
#****************************
def main():
    again = 'Y'
    while again == 'Y':
        piles = [3, 5, 7]
        lose = False
        player = 0
        while lose == False:
            
            displayPlayer(player)
            displayPiles(piles)
            pileChoice = getPileChoice(piles)
            getMoveAmount(piles, pileChoice)
            lose = isLoser(piles, player)
            player = setPlayer(player)
        
        again = input("Enter Y to play again: ")
    
    
main()
