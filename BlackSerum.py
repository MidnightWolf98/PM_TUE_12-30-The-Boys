#!/bin/python3
import random

# SCENE 2
print("One Year Later")  # Prints the statement
print("You are at work at EB-Hi-Fi\nbored out of your mind\nas usual...")  # Prints the statement in 3 lines
print("You get a phone call from a customer:\n'How may I help you today?'")  # Prints the statement in 2 lines
print("'My recently bought laptop keeps freezing, how can I fix it?'")  # Prints the statement

print("What do you say?")  # Prints the statement
print("1 - Have you updated your system to the latest version?")  # Prints the statement
print("2 - Did you try restarting your internet connection?")  # Prints the statement
print("3 - Have you tried restarting your system?")  # Prints the statement

def client_choice():  # Defines a function called client_choice
    try:  # Trys to run the code below
        client_problem_response = int(input("1, 2 or 3: "))  # Allows users to input an integer
        while client_problem_response != 3:  # While the input is not 3 run the code below
            while client_problem_response == 1 or client_problem_response == 2:  # While the input is 1 or 2 run the code below
                print("Yes I Have.")  # Prints Yes I Have
                break  # Exits the while loop
            client_problem_response = int(input("1, 2 or 3: "))  # Allows users to input an integer again
        if client_problem_response == 3:  # If input is 3 run the code below
            print("Let me try now...wow, it worked! Thank you, bye!")  # Prints the statement
    except:  # Runs the code below to avoid error in case of wrong input
        print("Choose 1, 2 or 3 only")  # Prints the statement
        client_choice()  # Runs the function client_choice

client_choice()  # Calls the client_choice function


print("The time is 5:00pm.")  # Prints the statement
print("It is time for you to go home.")  # Prints the statement
print("Like every other day, you day at work was long and exhausting.")  # Prints the statement

print("You finally reach home.")  # Prints the statement
print("You enter your home after opening the door with the code 6969.")  # Prints the statement
print("You start up your personal computer and decide to do a little gaming")  # Prints the statement
print("What game would you like to play?")  # Prints the statement
print("1 - Grand Theft Manual")  # Prints the statement
print("2 - Minebuild")  # Prints the statement
print("3 - Call of Moody")  # Prints the statement
print("4 - Fortday")  # Prints the statement

def game_choice():  # Defines the game_choice function
    try:  # Trys to run the code below
        game_input = int(input("Pick between 1 and 4: "))  # Allows user to input an integer
        if game_input == 1:  # If input is 1, run the code below
            print("Great choice! Grand Theft Manual is a fan favourite")  # Prints the statement
        elif game_input == 2:  # If input is 2, run the code below
            print("Ohhh Minebuild! A great classic!")  # Prints the statement
        elif game_input == 3:  # If input is 3, run the code below
            print("Time to join the war in Call of Moody!")  # Prints the statement
        elif game_input == 4:  # If input is 4, run the code below
            print("Time to enjoy some Fortday!")  # Prints the statement
        else:  # If the input is not 1, 2, 3 or 4, it runs the code below
            print("Try again")  # Prints the statement
            game_choice()  # Runs the game_choice function
    except:  # Runs the code below to avoid error in case of wrong input
        print("Please enter a number between 1 and 4 only")  # Prints the statement
        game_choice()  # Runs the game_choice function

game_choice()  # Calls the game_choice function

print("Just as the game starts up you start to hear a noise")  # Prints the statement
print("'It sounds like theres a massive fight outside' you say to yourself")  # Prints the statement
print("You decide to open the blinds in your apartment and see minions and the teletubbies casually brawling in the sky")  # Prints the statement
print("You then close your blinds and go back to gaming like nothings happening outside")  # Prints the statement
print("Just as you put your headset on, one of the minions falls out of the sky, through your roof, into your apartment")  # Prints the statement
print("'THAT HOLE IS GONNA COST ME A FORTUNE TO FIX, IM ALREADY BEHIND ON THE BILLS!!' you shout out loud")  # Prints the statement
print("The minion sees and decides to attack")  # Prints the statement
print("Without looking, you flick the minion away and it explodes into a million pieces")  # Prints the statement
print("'NOW I HAVE TO CLEAN THIS TOO!!!'")  # Prints the statement

# Scene 3
print("After fixing your roof, \ncleaning the apartment \nand getting rid of the remaining minions and teletubbies with your powers\nyou decide to go back to your normal and average life by continuing to hide your powers")  # Prints the statement
print("Suddenly your new smartphone starts to ring\nYou decide to answer the call")  # Prints the statement on 2 lines
print("It's Homelander\nI've got a job for you\nAll you need to do is break into a few banks\nYou'll get a big payday\nIts a in and out job'")  # Prints the statement in 4 lines
print("1 - I could use the extra cash [Embrace the dark side]")  # Prints the statement
print("2 - <say nothing>")  # Prints the statement
print("3 - Sorry, I got out of that life a long time ago [Report them and embrace the light]")  # Prints the statement

def crime_choice():  # Defines the crime_choice function
    try:  # Trys to run the code below
        crime_input = int(input("What choice will you make: "))  # Allows user to input an integer
        while crime_input == 2:  # While input is 2, run the code below
            print("Come on, you'll be safe in the van, it's low risk. Are you in?")  # Prints the statement
            print("1 - I could use the extra cash [Embrace the dark side]")  # Prints the statement
            print("2 - <say nothing>")  # Prints the statement
            print("3 - Sorry, I got out of that life [Report them and embrace the light]")  # Prints the statement
            crime_input = int(input("What choice will you make: "))  # Allows user to input an integer
        if crime_input == 1:  # If input is 1, run the code below
            print("Great!\nMeet me at 145 Elm Street at 10pm")  # Prints the statement on 2 lines
        elif crime_input == 3:  # If input is 3, run the code below
            print("You call the police to report them")  # Prints the statement
            print("You stick to your honest and truthful ways!")  # Prints the statement
            print("Too bad Homelander isnt the type of person to forgive and forget")  # Prints the statement
        else:  # Runs the code below if the input is not 1, 2 or 3
            print("Try Again!")  # Prints the statement
            crime_choice()  # Runs the crime_choice function
    except:  # Runs the code below to avoid error in case of wrong input
        print("Please input 1, 2 or 3 only")  # Prints the statement
        crime_choice()  # Runs the crime_choice function

crime_choice()  # Calls the crime_choice function

#SCENE 4
print("You get in your car and put your home address into the gps") #Prints the statement
print("You finally reach the destination after half an hours of driving") #Prints the statement
print("Suddenly your old friend Lenny knocks on your door") #Prints the statement
print("After conversing with Lenny you find out someone has kidnapped his family so you get in the van with him") #Prints the statement
print("You reach the building where Lenny's family is being held") #Prints the statement
print("Its time for you to use your powers once again") #Prints the statement

print("The miniboss 'Mike Tyson's' health is 20, how do you choose to attack it?") #Prints the statement
print("1 - Try to run past [No Damage]") #Prints the statement
print("2 - Super Kick [Random Damage]") #Prints the statement
print("3 - Hyper Punch [Two Shot]") #Prints the statement

def attack_choice(): #Defines the attack_choice function
    try: #Trys to run the code below
        miniboss_health = 20 #Defines miniboss_health as 20
        attack_input = int(input("What attack will you use: ")) #Allows user to input an integer
        while miniboss_health > 0: #While miniboss_health is more than 0, run the code below
            random_damage = random.randint(1, miniboss_health) #Defines random_damage as a random integer between 1 and the miniboss_health
            if attack_input == 1: #If input is 1, run the code below
                print("You have done 0 damage to Mike Tyson") #Prints the statement
            elif attack_input == 2: #If input is 2, run the code below
                print("You have done", random_damage, "damage to Mike Tyson") #Prints the statement and random_damage
                miniboss_health = (miniboss_health - random_damage) #Redefines miniboss_health as random_damage subtracting from miniboss_health
                print("Mike Tyson's health is", miniboss_health) #Prints the statement and miniboss_health
            elif attack_input == 3: #If input is 3, run the code below
                print("One more shot to take down Mike Tyson") #Prints the statement
                miniboss_health = 0 #Redefines miniboss_health as 0
            else: #Runs the code below if the input is not 1, 2 or 3
                print("Try Again") #Prints the statement
                attack_choice() #Runs the attack_choice function
            attack_input = int(input("What attack will you use: ")) #Allows user to input an integer
            if miniboss_health <= 0: #If miniboss_health is less than or equal to 0, it runs the code below
                print("You defeat Mike Tyson and carry on") #Prints the statement
    except: #Runs the code below to avoid error in case of wrong input
        print("Please enter 1, 2 or 3 only") #Prints the statement
        attack_choice() #Runs the attack_choice function

attack_choice() #Calls the attack_choice function
