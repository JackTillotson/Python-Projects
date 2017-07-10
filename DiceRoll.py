# D&D dice rolling program

#Dictionary for attributes
#While loop to make sure attributes are not == 0


#********************
# IMPORTING RANDOM
#********************
import random

#********************
# MODULE : character
# OUTPUTS : list2
# DEF : To generate the stat list
#********************

def character():
    
    list1 = range(1,7)
    characterRoll1 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll2 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll3 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll4 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll5 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll6 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll7 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll8 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll9 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll10 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll11 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    characterRoll12 = random.choice(list1) + random.choice(list1) + random.choice(list1)
    
    list1 = [characterRoll1, characterRoll2, characterRoll3, characterRoll4, characterRoll5, characterRoll6, characterRoll7, characterRoll8, characterRoll9, characterRoll10, characterRoll11, characterRoll12]
    print("Here are your rolls: ", list1)

    list2 = []
    
    list2.append(max(list1))
    list1.remove(max(list1))

    list2.append(max(list1))
    list1.remove(max(list1))

    list2.append(max(list1))
    list1.remove(max(list1))

    list2.append(max(list1))
    list1.remove(max(list1))

    list2.append(max(list1))
    list1.remove(max(list1))

    list2.append(max(list1))
    list1.remove(max(list1))

    list2.sort()
    list2.reverse()

    print("Here are your top 6 rolls: ", list2)
    return list2



#********************
# MODULE : assignStat1
# OUTPUTS : stat1
# DEF : To assign a number to the first stat
#********************
        
def assignStat1(list2, attributes):

    
    # repeat all indented code until rolls is empty
    while (len(list2) > 0):

        # Print all stat options (skipping the ones that are already assigned)
        print("Please choose which stat you would like your highest roll to go to from the options below")
        [print("{} ".format(option), end='') for option in attributes if attributes[option] == 0]
        print()

        # get user input
        choice = input(": ")
        
        # As long as the choice is invalid for some reason, make them choose again
        # repeat until the choice is valid
        while (choice not in attributes or attributes[choice] != 0):
            choice = input("Don't be a doofus and pick a real attribute.") # strength
        
        # Assign the value stored "behind" choice to the highest number
        attributes[choice] = max(list2)

        # Remove the highest number
        list2.remove(max(list2))

# main module
def main(list2):

    # define rolls and attributes
    
    attributes = {"str": 0, "dex": 0, "con": 0, "wis": 0, "cha": 0, "int": 0}

    # Call the function defined above
    assignStat1(list2, attributes)

    print(attributes)

    
    
def rollDice():
    again = "Y"
    while again == "Y":
    
        dice = int(input("Please input the dice that you would like to roll or enter '0' if you want to roll for you character : "))
        if dice != 0 and isinstance(dice, int):
            roll = random.randint(1,dice)
            print(roll)
        elif dice == (0):
            list2 = character()
            main(list2)
        else:
            rollDice()
        again = input("Enter Y to roll again: ")

    #dice = input("Please input the dice that you would like to roll or enter '0' if you want to roll for you character : ")
    #while dice != 0:
        #dice = int(input("Please input the dice that you would like to roll or enter '0' if you want to roll for you character : "))
        
rollDice()


