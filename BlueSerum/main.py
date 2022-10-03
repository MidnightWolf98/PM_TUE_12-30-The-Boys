from time import sleep


def my_loading():
    import time
    import sys

    print("Loading:")

    percent_Bar = ["[#---------]", "[##--------]", "[###-------]", "[####------]", "[#####-----]", "[######----]",
                   "[#######---]", "[########--]", "[#########-]", "[##########]"]

    for i in range(len(percent_Bar)):
        time.sleep(0.4)
        sys.stdout.write("\r" + percent_Bar[i % len(percent_Bar)])
        sys.stdout.flush()

    print("\n")


def Button_Mash():
    import sys
    import random
    from threading import Timer
    import time

    timeout = 2

    # How mant seconds the user has to dodge

    prompt = ("PRESS PRESS PRESS\n")
    t = Timer(timeout, print, [])  # if user doesnt input prints this

    t.start()  # initalises the countdown

    start_time = time.time()  # imports the current time and sets it as the start time

    answer = input(prompt)  # prints prompt and waits for user input enter

    t.cancel()

    end_time = time.time()  # gets the time after user input

    reaction_time = end_time - start_time  # minus start from end time and calucaltes the difference

    if reaction_time > timeout:  # this if or is for the reaction time being larger than the set timeout
        print("You FAILED AND WENT S P L A T!")
        sys.exit()

    else:
        print("You keep pulling up ")







def Quick_Time(Action):
    import sys
    import random
    from threading import Timer
    import time

    timeout = random.randint(2,5)



    # How mant seconds the user has to dodge

    prompt = (f"You have {timeout} seconds to dodge, press enter...\n")
    t = Timer(timeout, print, [])  # if user doesnt input prints this

    t.start()  # initalises the countdown

    start_time = time.time()  # imports the current time and sets it as the start time

    answer = input(prompt)  # prints prompt and waits for user input enter

    t.cancel()

    end_time = time.time()  # gets the time after user input

    reaction_time = end_time - start_time  # minus start from end time and calucaltes the difference

    if reaction_time > timeout:  # this if or is for the reaction time being larger than the set timeout
        print("You got hit!")
        sys.exit()

    else:
        print("You dodged and keep " + str(Action))





def intro_blue():
                      #SCENE1#
    print("*It has been 6 months since that incedent*")
    sleep(1.5)
    print("*You come to your senses*")
    sleep(1.5)
    print("*the gunshots in the room ring through your head*\n*Every Shot feels like an anvil dropped on your head*")
    sleep(2.5)
    print("*The shouting Snaps you back to the moment* \n")
    sleep(1.5)
    print("*Frenchie runs over to you and exlaims:\nAre you Alright? Lets GO! They're getting to close WE. HAVE. TO. GO! ")
    sleep(4)
    print("*You look up and feel a warm liquid get splattered across your face*")
    sleep(1.5)
    print("*THEY SHOT FRENCHIE!* \n")
    sleep(1)
    print("*YOU FILL WITH ANGER AND RAGE* \n *YOU FEEL A BURNING FROM THE INSIDE AND YOU REMEMBER THE SERUM* \n *WHAT DO YOU DO?*")

    print("1. Grab Frenchie and Run\n2. Unleash the rage building inside and charge the shooters\n")


def ShotScene1():
    try:
        choice = int(input("WHAT WILL YOU DO?!"))
        if choice == 1:
            print("SCENE A1")
        elif choice == 2:
            print("SCENE B1")
            Scene_B1()
        else:
            print("Only Enter Required Integers!")
            ShotScene1()
    except:
        print("Only Enter Required Integers")
        ShotScene1()


def Scene_B1():
    import sys
    from threading import Timer
    import time

    timeout = 4
    counter = 3
    while counter > 0:

        # How mant seconds the user has to dodge

        prompt = (f"You have {timeout} seconds to dodge, press enter...\n")
        t = Timer(timeout, print, [
            "\n You got hit from stadning there and hesitating \n " + prompt])  # if user doesnt input prints this

        t.start()  # initalises the countdown

        start_time = time.time()  # imports the current time and sets it as the start time

        answer = input(prompt)  # prints prompt and waits for user input enter

        t.cancel()

        end_time = time.time()  # gets the time after user input

        reaction_time = end_time - start_time  # minus start from end time and calucaltes the difference

        if reaction_time > timeout:  # this if or is for the reaction time being larger than the set timeout
            print("You got hit!")
            counter = counter - 1
            timeout = timeout - 0.5
            print("You think of what they did to you friends and get back up and charge")
            print("Health: " + str(counter) + '\n')
            prompt



        else:
            print("You dodged and keep charging at the enemy ")
            timeout = timeout - 0.5
            counter = counter - 0.5
            prompt

    print(
        "\n*You feel a sharp pain in your back. The world begins to fade to black. The last thing you remember is...her*")
    sys.exit()




def Scene_A1():
    my_loading()
    print("You run over and grab Frenchie")
    sleep(1)
    print("FRENCHIE! CAN YOU HEAR ME! - you yell")
    sleep(0.5)
    print("***")
    sleep(0.5)
    print("***")
    sleep(0.5)
    print("***")
    print("*Frenchie mutters something incoherently to you\nYou look him in his eyes and promise to get him out of there")
    sleep(4)
    print("*You scoop him up... he feels lighter than normal you think to yourself..")
    sleep(2)

    Quick_Time_Count = 0
    while Quick_Time_Count < 4:
        Quick_Time("Falling")
        print("You see the ground coming up quickly. SHIT!")
        Quick_Time_Count = Quick_Time_Count + 1

    print("SHIT WHAT DO YOU DO?")
    sleep(3)
    print("You see the ground coming up fast. You close your eyes and your instincts kick in.\nYou feel as if every neuron in your brain is firing at once.")
    sleep(5)
    print("SUddenly you feel your back shoot rivers of pain throughout your entire body. All you see is red. And as if out of nowhere you hear the sound....\nOf a bird?")
    sleep(4)
    print("With your brain moving at 100 Miles an hour you are suddenly taken back...to the lab\nYou recall taking that Syrum and remember the same feeling back then too")
    sleep(5)
    print("You begin to feel the sinew in your back take on a mind of its own and you begin to...")
    sleep(3)
    print("...fly?")
    sleep(3)
    print("As if you had been flying for your whole life you direct your attention towards the nearby aparment complexes.....and head towards them")




def Scene_A2():
    my_loading()
    print("*Days have passed and you and the gang are in hiding out in Hughies Apartment*")
    sleep(2)
    print("WHAT DO WE DO!\nTHEY TOOK KIMIKO!-Exclaims Hughie")
    sleep(2)
    print("The group begins to bicker between themselves")
    sleep(3)
    print("SHUT UP WE HAVE TO DO SOMETHING! - Shouts MM")
    sleep(1)
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("...\n")
    sleep(2)
    print("*You feel something rising inside of you. The internal conflict begins.....*\n \n*You walk towards the window....and jump*")
    sleep(3)
    print("*something about flying makes you feel....free*\nYou stech your wings out and take off and think to yourself.\nWhat will your next steps be to save Kimiko abd bing juctice to the world.")

    def Second_Split_Choice():
        try:
            choice = int(input("What will you do? How will you fix this?\nGo face Vaught head on and sae your friend or go down ina blaze of glory while trying?\nOr will you try and save one of your closest friends and leave justice up to karma?"))
            if choice == 1:
                print("You decice to go head to vaughts front gates and give them what they deseve.")
            elif choice == 2:
                print("You Fly back to your team, wind blowing on your face. You know what needs to be done to save your friend.")
                sleep(3)
                print("You know one way into vaught that they just wont expect...")
                Scene_B1()
            else:
                print("Only Enter Required Integers!")
                Second_Split_Choice()
        except:
            print("Only Enter Required Integers")
            ShotScene1()









#Quick_Time()
#intro_blue()
#ShotScene1()
#Scene_A1()

