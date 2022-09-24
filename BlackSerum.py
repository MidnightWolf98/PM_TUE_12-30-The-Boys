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
print("It's Maeve\nI've got a job for you\nAll you need to do is break into a few banks\nYou'll get a big payday\nIts a in and out job'")  # Prints the statement in 4 lines
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
            print("You meet Maeve at the address and are waiting for her to arrive")#Prints the statement
            print("Its been 20 minutes and you are starting to get suspicious")#Prints the statement
            print("You receive a voicemail from Maeve")#Prints the statement
            print("I know it was you who broke into the factory and tried to destroy the last of super serums, she says")#Prints the statement
            print("Before you can react, you are surrounded by entire police force and the countrys special forces")#Prints the statement
            print("You get out of your car and they see that as a threat and proceed to shoot you")#Prints the statement
            print("Too bad they didnt know you had super powers")#Prints the statement
            print("You defeat all of them and decide to run")#Prints the statement
        elif crime_input == 3:  # If input is 3, run the code below
            print("You call the police and the military to report them")  # Prints the statement
            print("You stick to your honest and truthful ways!")  # Prints the statement
            print("Too bad Maeve isnt the type of person to forgive and forget")  # Prints the statement
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
print("After conversing with Lenny you find out Maeve has kidnapped his family so you get in the van with him") #Prints the statement
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

#SCENE 5
print("After defeating the miniboss Mike Tyson, you need you to hack each of the 4 electronic locks on the safe doors") #Prints the statement
print("You use your hacking experience from your extensive and boring career at EB Hi-Fi")#Prints the statement

def door1_choice(): #Defines the door1_choice function
    try: #Trys to run the code below
        hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]", "4-SQL Injection [Two Shot]"] #Defines hack_list as the statement provided
        print("You access lock 1 of 4") #Prints the statement
        print(hack_list) #Prints hack_list
        door1_health = 30 #Defines door1_health as 30
        hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
        while door1_health > 0: #While door1_health is more than 0, run the code below
            random_hack_damage = random.uniform(1, door1_health) #Defines random_hack_damage as a random integer between 1 and the door1_health
            random_hack_damage = float(random_hack_damage) #Declares random_hack_damage as a float data type
            if hack_input == 1: #If input is 1, run the code below
                print("You have done 0 damage to the lock system") #Prints the statement
            elif hack_input == 2: #If input is 2, run the code below
                print("You have done 5 damage to the lock system") #Prints the statement
                door1_health = (door1_health - 5) #Redefines door1_health as door1_health subtracting 5
                print("The lock systems health is", door1_health) #Prints the statement and door1_health
            elif hack_input == 3: #If input is 3, run the code below
                print("You have done", random_hack_damage, "damage to the lock system") #Prints the statement and random_hack_damage
                door1_health = (door1_health - random_hack_damage) #Redefines door1_health as random_hack_damage subtracted from door1_health
                print("The lock systems health is", door1_health) #Prints the statement and door1_health
            elif hack_input == 4: #If input is 4, run the code below
                print("One more shot to take down the lock system") #Prints the statement
                door1_health = 0 #Redefines door1_health as 0
            else: #Runs the code below if the input is not 1, 2, 3 or 4
                print("Try Again") #Prints the statement
                door1_choice() #Runs the door1_choice function
            hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
            if door1_health <= 0: #If door1_health is less than or equal to 0, it runs the code below
                print("You have disabled the lock of door 1") #Prints the statement
    except: #Runs the code below to avoid error in case of wrong input
        print("Please enter 1, 2, 3 or 4") #Prints the statement
        print("The lock is now full health again, you will have to start again") #Prints the statement
        door1_choice() #Runs the door1_choice function

door1_choice() #Calls the door1_choice function

def door2_choice(): #Defines the door2_choice function
    try: #Trys to run the code below
        hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]", "4-SQL Injection [Two Shot]"] #Defines hack_list as the statement provided
        print("You access lock 2 of 4") #Prints the statement
        print(hack_list) #Prints hack_list
        door2_health = 30 #Defines door2_health as 30
        hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
        while door2_health > 0: #While door2_health is more than 0, run the code below
            random_hack_damage = random.uniform(1, door2_health) #Defines random_hack_damage as a random integer between 1 and the door2_health
            random_hack_damage = float(random_hack_damage) #Declares random_hack_damage as a float data type
            if hack_input == 1: #If input is 1, run the code below
                print("You have done 0 damage to the lock system") #Prints the statement
            elif hack_input == 2:  # If input is 2, run the code below
                print("You have done 5 damage to the lock system")  # Prints the statement
                door2_health = (door2_health - 5)  # Redefines door2_health as door2_health subtracting 5
                print("The lock systems health is", door2_health)  # Prints the statement and door2_health
            elif hack_input == 3:  # If input is 3, run the code below
                print("You have done", random_hack_damage, "damage to the lock system")  # Prints the statement and random_hack_damage
                door2_health = (door2_health - random_hack_damage)  # Redefines door2_health as random_hack_damage subtracted from door2_health
                print("The lock systems health is", door2_health)  # Prints the statement and door2_health
            elif hack_input == 4:  # If input is 4, run the code below
                print("One more shot to take down the lock system")  # Prints the statement
                door2_health = 0  # Redefines door2_health as 0
            else:  # If the code is not 1, 2, 3 or 4, it runs the code below
                print("Try Again")  # Prints the statement
                door2_choice()  # Runs the door2_choice function
            hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
            if door2_health <= 0: #If door2_health is less than or equal to 0, it runs the code below
                print("You have disabled the lock of door 2") #Prints the statement
    except: #Runs the code below to avoid error in case of wrong input
        print("Please enter 1, 2, 3 or 4") #Prints the statement
        print("The lock is now full health again, you will have to start again") #Prints the statement
        door2_choice() #Runs the door2_choice function

door2_choice() #Calls the door2_choice function

def door3_choice():
    try: #Trys to run the code below
        hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]", "4-SQL Injection [Two Shot]"] #Defines hack_list as the statement provided
        print("You access lock 3 of 4") #Prints the statement
        print(hack_list) #Prints hack_list
        door3_health = 30 #Defines door3_health as 30
        hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
        while door3_health > 0: #While door3_health is more than 0, run the code below
            random_hack_damage = random.uniform(1, door3_health) #Defines random_hack_damage as a random integer between 1 and the door3_health
            random_hack_damage = float(random_hack_damage) #Declares random_hack_damage as a float data type
            if hack_input == 1: #If input is 1, run the code below
                print("You have done 0 damage to the lock system") #Prints the statement
            elif hack_input == 2: #If input is 2, run the code below
                print("You have done 5 damage to the lock system") #Prints the statement
                door3_health = (door3_health - 5) #Redefines door3_health as door3_health subtracting 5
                print("The lock systems health is", door3_health) #Prints the statement and door3_health
            elif hack_input == 3: #If input is 3, run the code below
                print("You have done", random_hack_damage, "damage to the lock system") #Prints the statement and random_hack_damage
                door3_health = (door3_health - random_hack_damage) #Redefines door3_health as random_hack_damage subtracted from door3_health
                print("The lock systems health is", door3_health) #Prints the statement and door3_health
            elif hack_input == 4: #If input is 4, run the code below
                print("One more shot to take down the lock system") #Prints the statement
                door3_health = 0 #Redefines door4_health as 0
            else: #If the code is not 1, 2, 3 or 4, it runs the code below
                print("Try Again") #Prints the statement
                door3_choice() #Runs the door3_choice function
            hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
            if door3_health <= 0: #If door3_health is less than or equal to 0, it runs the code below
                print("You have disabled the lock of door 3") #Prints the statement
    except: #Runs the code below to avoid error in case of wrong input
        print("Please enter 1, 2, 3 or 4") #Prints the statement
        print("The lock is now full health again, you will have to start again") #Prints the statement
        door3_choice() #Runs the door3_choice function

door3_choice() #Calls the door3_choice function

def door4_choice():
    try: #Trys to run the code below
        hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]", "4-SQL Injection [Two Shot]"] #Defines hack_list as the statement provided
        print("You access lock 4 of 4") #Prints the statement
        print(hack_list) #Prints hack_list
        door4_health = 30 #Defines door4_health as 30
        hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
        while door4_health > 0: #While door4_health is more than 0, run the code below
            random_hack_damage = random.uniform(1, door4_health) #Defines random_hack_damage as a random integer between 1 and the door4_health
            random_hack_damage = float(random_hack_damage) #Declares random_hack_damage as a float data type
            if hack_input == 1: #If input is 1, run the code below
                print("You have done 0 damage to the lock system") #Prints the statement
            elif hack_input == 2: #If input is 2, run the code below
                print("You have done 5 damage to the lock system") #Prints the statement
                door4_health = (door4_health - 5) #Redefines door4_health as door4_health subtracting 5
                print("The lock systems health is", door4_health) #Prints the statement and door4_health
            elif hack_input == 3: #If input is 3, run the code below
                print("You have done", random_hack_damage, "damage to the lock system") #Prints the statement and random_hack_damage
                door4_health = (door4_health - random_hack_damage) #Redefines door4_health as random_hack_damage subtracted from door4_health
                print("The lock systems health is", door4_health) #Prints the statement and door4_health
            elif hack_input == 4: #If input is 4, run the code below
                print("One more shot to take down the lock system") #Prints the statement
                door4_health = 0 #Redefines door4_health as 0
            else: #If the code is not 1, 2, 3 or 4, it runs the code below
                print("Try Again") #Prints the statement
                door4_choice() #Runs the door4_choice function
            hack_input = int(input("Which hack would you like to use: ")) #Allows user to input an integer
            if door4_health <= 0: #If door4_health is less than or equal to 0, it runs the code below
                print("You have disabled the lock of door 4") #Prints the statement
    except: #Runs the code below to avoid error in case of wrong input
        print("Please enter 1, 2, 3 or 4") #Prints the statement
        print("The lock is now full health again, you will have to start again") #Prints the statement
        door4_choice() #Runs the door4_choice function

door4_choice() #Callss the door4_choice function

print("You have successfully unlocked all 4 doors") #Prints the statement
print("After unlocking all the doors, you see that Maeve has escaped prison and is now holding your mother and father hostage")#Prints the statement
print("You realise Lenny had led you on and betrayed you")#Prints the statement
