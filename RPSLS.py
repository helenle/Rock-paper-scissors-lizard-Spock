# Rock-paper-scissors-lizard-Spock 
# Huyen Le

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
# get the number and convert it to name and return name.
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print "Invalid number!"
    
    return name

def name_to_number(name):
# get the name and convert it to a number and return number.
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        # assign a number so that it won't throw an error 
        # if user enters an invalid name at runtime.
        number = 5 
        print "Invalid name!"
    
    return number


def rpsls(name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    if (player_number < 5):
        # compute difference of player_number and comp_number modulo five
        difference = (comp_number - player_number) % 5 
        
        # use if/elif/else to determine winner
        if difference == 0:            
            winner = "Player and computer tie!"
        elif (difference >= 1) and (difference <= 2):
            winner = "Computer wins!"
        else: # assume (difference >= 3) and (difference <= 4)
            winner = "Player wins!"
             
        # convert comp_number to name using number_to_name        
        comp_name = number_to_name(comp_number)		

        # print results
        print "Player chooses", name
        print "Computer chooses", comp_name
        print winner, " \n"
    
    else:
        print ""
    

# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





