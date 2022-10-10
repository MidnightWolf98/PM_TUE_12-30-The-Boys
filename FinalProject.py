#!/bin/python3
import time
from time import sleep
import sys
import random
import os

def blue_serum():
    def Second_Split_Choice():
        try:
            choice = int(input(
                "What will you do? How will you fix this?\n1. Go face Vaught head on and sae your friend and go down ina blaze of glory while trying?\nOr\n2. will you try and save one of your closest friends and leave justice up to karma?"))
            if choice == 1:
                print("You decice to go head to vaughts front gates and give them what they deseve.")
                charge_Scene()

            elif choice == 2:
                print(
                    "\nYou Fly back to your team, wind blowing on your face. You know what needs to be done to save your friend.")
                sleep(3)
                print("\nYou know one way into vaught that they just wont expect...")
                Sneak_Scene()


            else:
                print("Only Enter Required Integers!")
                Second_Split_Choice()
        except:
            print("Only Enter Required Integers")
            Second_Split_Choice()

    def battle(Villian_Name, Villian_Health):
        import random
        Health = Villian_Health
        User_Health = 100
        print(Villian_Name + " prepares to go on the offensive! What do you do?")

        while User_Health > 0 and Health > 0:
            print("Attacks:")
            print("1. Punch")
            print("2. Kick")
            print("3. Special")

            try:
                choice = int(input("WHAT WILL YOU DO?!"))
                print(choice)
                if choice == 1:
                    damage = random.randint(5, 10)
                    print("YOU PUNCH AND DEAL " + str(damage) + " To " + Villian_Name)
                    Health = Health - damage
                    print(Villian_Name + " Has " + str(Health) + " remaining")

                elif choice == 2:
                    damage = random.randint(10, 20)
                    print("YOU KICK AND DEAL " + str(damage) + " To " + Villian_Name)
                    Health = Health - damage
                    print(Villian_Name + " Has " + str(Health) + " remaining")

                elif choice == 3:
                    damage = random.randint(50, 75)
                    print("YOU FLY AT THEM AND DEAL " + str(damage) + " To " + Villian_Name)
                    Health = Health - damage
                    print(Villian_Name + " Has " + str(Health) + " remaining")


            except:
                print("You didnt attack!")
                print(
                    Villian_Name + " Sees you hesitate and KICKS your head off.\nYou failed your friends and the world is doomed now")
                os._exit(1)

            Villian_Damage = random.randint(10, 30)
            User_Health = User_Health - Villian_Damage
            print(Villian_Name + " Does " + str(Villian_Damage) + " Damage To You!")
            print("You have " + str(User_Health) + " Health Left! Be careFul!")
            print("\n")

        print("You defeated " + Villian_Name)

    def sneaking(Direction):
        try:
            choice = (input("You appear at a cross roads. Which direction do you go?"))
            if choice.lower() == Direction:
                print("You head in " + Direction + " and keep heading on the path scribbled on the paper")
            else:
                print(
                    "You go in " + choice + " and turn the corner and *BAM* you get shot from nowhere. You bleed out and feel your life fleeting away")
                os._exit(1)
        except:
            print("Whoops. You made a mistake and died! Try again!")
            os._exit(1)

    def my_loading():
        import time
        import sys

        print("Loading:")

        percent_Bar = ["[#---------]", "[##--------]", "[###-------]", "[####------]", "[#####-----]",
                       "[######----]",
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
            os._exit(1)

        else:
            print("You keep pulling up ")

    def Quick_Time(Action):
        import sys
        import random
        from threading import Timer
        import time

        timeout = random.randint(2, 5)

        # How mant seconds the user has to dodge

        prompt = (f"You have {timeout} seconds to dodge, press enter...\n")
        sleep(1)
        t = Timer(timeout, print, [])  # if user doesnt input prints this

        t.start()  # initalises the countdown

        start_time = time.time()  # imports the current time and sets it as the start time

        answer = input(prompt)  # prints prompt and waits for user input enter

        t.cancel()

        end_time = time.time()  # gets the time after user input

        reaction_time = end_time - start_time  # minus start from end time and calucaltes the difference

        if reaction_time > timeout:  # this if or is for the reaction time being larger than the set timeout
            print("You got hit!")
            os._exit(1)

        else:
            print("You dodged and keep " + str(Action))

    def intro_blue():
        # SCENE1#
        print("*It has been 6 months since that incedent*")
        sleep(1.5)
        print("*You come to your senses*")
        sleep(1.5)
        print(
            "*the gunshots in the room ring through your head*\n*Every Shot feels like an anvil dropped on your head*")
        sleep(2.5)
        print("*The shouting Snaps you back to the moment* \n")
        sleep(1.5)
        print(
            "*Frenchie runs over to you and exlaims:\nAre you Alright? Lets GO! They're getting to close WE. HAVE. TO. GO! ")
        sleep(4)
        print("*You look up and feel a warm liquid get splattered across your face*")
        sleep(1.5)
        print("*THEY SHOT FRENCHIE!* \n")
        sleep(1)
        print(
            "*YOU FILL WITH ANGER AND RAGE* \n *YOU FEEL A BURNING FROM THE INSIDE AND YOU REMEMBER THE SERUM* \n *WHAT DO YOU DO?*")

        print("1. Grab Frenchie and Run\n2. Unleash the rage building inside and charge the shooters\n")
        ShotScene1()
        exit()

    def ShotScene1():
        try:
            choice = int(input("WHAT WILL YOU DO?!"))
            if choice == 1:
                print("SCENE A1")
                Scene_A1()
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
            print("YOU CHARGE AT THE ENEMIES TO GET REVENGE!\nTHEY BEGIN SHOOTING AT YOU. YOU HAVE" + str(
                counter) + " Health")
            prompt = (f"You have {timeout} seconds to dodge a bullet, press enter...\n")
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
        os._exit(1)

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
        print(
            "*Frenchie mutters something incoherently to you\nYou look him in his eyes and promise to get him out of there")
        sleep(4)
        print("*You scoop him up... he feels lighter than normal you think to yourself..")
        sleep(2)
        print(
            "You run and jump out the closest window... you rember youre on the 50th floor.\nYou notice large pieces of debris falling with you")

        Quick_Time_Count = 0
        while Quick_Time_Count < 4:
            Quick_Time("Falling")
            print("You see the ground coming up quickly. SHIT!")
            Quick_Time_Count = Quick_Time_Count + 1

        print("SHIT WHAT DO YOU DO?")
        sleep(3)
        print(
            "You see the ground coming up fast. You close your eyes and your instincts kick in.\nYou feel as if every neuron in your brain is firing at once.")
        sleep(3)
        print(
            "SUddenly you feel your back shoot rivers of pain throughout your entire body. All you see is red. And as if out of nowhere you hear the sound....\nOf a bird?")
        sleep(3)
        print(
            "With your brain moving at 100 Miles an hour you are suddenly taken back...to the lab\nYou recall taking that Syrum and remember the same feeling back then too")
        sleep(3)
        print("You begin to feel the sinew in your back take on a mind of its own and you begin to...")
        sleep(3)
        print("...fly?")
        sleep(3)
        print(
            "As if you had been flying for your whole life you direct your attention towards the nearby aparment complexes.....and head towards them")
        Scene_A2()

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
        print(
            "*You feel something rising inside of you. The internal conflict begins.....*\n \n*You walk towards the window....and jump*")
        sleep(3)
        print(
            "*something about flying makes you feel....free*\nYou stech your wings out and take off and think to yourself.\nWhat will your next steps be to save Kimiko and bring juctice to the world.")
        Second_Split_Choice()

    def charge_Scene():
        sleep(2)
        print("In a fit of rage you fly right at the Vaught headquaters")
        sleep(2)
        print("as youre flying you look above you and see Homelander staring at you with murder in his eyes")
        sleep(2)
        print("You see him charge up his eye lasers to shoot")

        Flying_Count = 0
        while Flying_Count < 4:
            Quick_Time("Flying")
            print("You see Homelander charge up for another shot\n")
            Flying_Count = Flying_Count + 1

        sleep(3)
        print("You look up one more time and Homelander is no longer above you.\n")
        sleep(2)
        print("You shift your attention fowards and BAM you collide with Homelander head on.")
        print("You beggin to lose concious and fall to your doom....\nFailing Everyone...")
        Final_Scene()
        os._exit(1)

    def Sneak_Scene():
        print("You and the gang get to the manhole cover and lift it off and peer down into the abyss.\n")
        sleep(2)
        print("You sure this is going to work? - Asks Hughie.\n")
        sleep(1)
        print("Well shit its got to - You reply with\n")
        sleep(1)
        print(
            "*You look at Hughie and smile and jump down the man hole. The smell hits you first and then when you land...the sound, or rather\nlack of sound...\n")
        sleep(3)
        print(
            "*you hear every step you take down in the sewers*\nYou look down at the map your 'inside man' managed to make\n")
        sleep(1)
        print("╔═══━━━───  •  ───━━━═══╗")
        print("  L > R > D > D > L > R  ")
        print("╚═══━━━───  •  ───━━━═══╝")
        print("You take step after step down this dark sewer path hearing nowthing but rats and water")
        sleep(2)
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("l")
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("r")
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("d")
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("d")
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("l")
        print("plop plop plop you go through the water")
        sleep(2)

        sneaking("r")

        print("plop plop plop you go through the water\n")
        sleep(2)

        print("You finnaly get tp the door you were told about.\n")

        print(
            "You sneak through the door and turn around to close it gentley behind you when you head *AHEM*\n")
        sleep(3)
        print("*You whip your head around and see the deep smirking at you*\n")
        sleep(2)
        print(
            "Well now your head I might aswell stop you and gain some more fame - Yells the Deep triumphantly.\n")
        sleep(3)
        print(
            "You get ready for the fight thats about to ensue. You know this is a test of the devotion you have to your friends.")
        battle("The Deep", 100)
        print("You defeat the deep\n")
        sleep(2)
        print("ypu step over his unconscious body and head up through the building \n")
        sleep(2)
        print("With the alarms BLEARING you walk into the main hallway.")
        sleep(2)
        print("You see him...\n...Homelander...")
        sleep(2)
        print("And hes holding Kimiko")
        sleep(3)
        print("He stares you in the eyes and booms\nSO WHAT ARE YOU GOING TO DO THEN!?")
        sleep(2)
        print("Rage overtakes you and you charge at him")
        sleep(2)
        print("He looks at you dead pan and grins and grabs onto your friend an FLYS out the window")
        sleep(2)
        print("You follow suit and jump out the window to pursue")
        Final_Scene()

    intro_blue()

    # battle("Greg", 100)
    # intro_blue()
    # ShotScene1()
    # Scene_A1()

def red_serum():
    # Scene 2
    # 6 Months Later
    print("You are in your apartment and someone knocks at the front door.")
    print("You open the door and see a man wearing a black coat and a deerstalker on his head.")
    # You begin to talk to them
    print("Hey Sherlock Holmes doppelganger can I help you with anything?")
    # The other character shows me a photograph and replies
    print("I need your your urgent help with a case I'm working on speedster.")
    print("This man in the photograph is the most wanted drug dealer in the city!")
    print("I heard you only hunt those that have abilities.")
    print("So all I need from you is an address of where I could find this guy's stash.")

    print("What do you say?")
    print("1: Have you tried Snake Island?")
    print("2: Have you searched the Royal Casino?")
    print("3: I have recently heard rumors of a secret underground facility in the middle of the city.",
          "\n" "That's where you will probably find your answer detective.")

    def address():
        try:
            addresses = int(input("Please choose one of the options above:"))
            while addresses != 3:
                while addresses == 1:
                    print("Already searched there")
                    break
                while addresses == 2:
                    print("No luck there, you got another address?")
                    break
                addresses = int(input("Please choose one of the options:"))
            if addresses == 3:
                print(
                    "I didn't know this place existed" "\n" "you might have just helped us take down this gangster!!!")
        except:
            print("Please input integers (1,2,3) only! Try again!!")
            address()

    address()

    # Scene 3
    print(
        "Some time after the detective leaves your apartment, you suddenly begin to hear loud sirens going past your building.")
    print("You reach for the tv remote and turn your television on.")
    print("You witness live action of a man called the Boomerang, who has broken into a bank.")
    print("He has captured hostages!!!")
    print("Your assistance is needed regarding defeating the Boomerang.")
    print("What will you do?")

    print("1: You bolt out of your apartment and head towards the Central bank")
    print("2: You turn of the TV and ignore the lives of the innocent civilians.")

    def bank():
        try:
            choice = int(input("Please choose option 1 or 2:"))
            if choice == 1:
                print("You have chosen the heroic path and are on your way of saving lives!")
            elif choice == 2:
                print(
                    "You have chosen to ignore the situation! Innocents have died because of your consequences!!!")
                os._exit(1)
            else:
                print("Please input integers (1 or 2) only! Please try again!")
                bank()
        except:
            print("Please input integers (1 or 2) only! Please try again!")
            bank()

    bank()

    # Scene 4
    print("You reach the Central Bank in a matter of seconds")
    print("You faze through the glass door and see Boomerang in front of you")
    print("It is now time to fight this villain!!!")
    print("Boomerang's health point is 250 and has the ability to control boomerangs.")
    print("How do you want to attack him?")
    print("Attack 1: Speed Jab (light attack)")
    print("Attack 2: Fast Feet (medium attack")
    print("Attack 3: Spin Cycle (heavy attack, however it is random damage each hit)")
    print("Light attack damage is 30")
    print("Medium attack damage is 60")
    print("Heavy attack damage is between 15-100")

    def boomerang():
        try:
            boomerang_health = 250
            light_attack = 30
            medium_attack = 60
            attack_choice = int(input("Please choose one of the attacks:"))
            while boomerang_health != 0:
                heavy_attack = random.randint(15, 100)
                if attack_choice == 1:
                    print("You have done", light_attack, "damage to Boomerang!!!")
                    boomerang_health = (boomerang_health - light_attack)
                    print("Boomerang's health point is now", boomerang_health)
                elif attack_choice == 2:
                    print("You have done", medium_attack, "damage to Boomerang")
                    boomerang_health = (boomerang_health - medium_attack)
                    print("Boomerang's health point is now", boomerang_health)
                elif attack_choice == 3:
                    print("You have done", heavy_attack, "damage to Boomerang")
                    boomerang_health = (boomerang_health - heavy_attack)
                    print("Boomerang's health point is now", boomerang_health)
                else:
                    print(
                        "The input is incorrect!!!" "Your consequence is that Boomerang's health has regenerated")
                    print("Please input 1,2 or 3!!!")
                    boomerang()
                if boomerang_health <= 0:
                    print("Congratulations you have defeated Boomerang!!!")
                    break
                attack_choice = int(input("Please choose one of the attacks"))
        except:
            print("The input is incorrect!!!" "Your consequence is that Boomerang's health has regenerated")
            print("Please input 1,2 or 3!!!")
            boomerang()

    boomerang()

    # Scene 5

    print("All of a sudden, A-Train a popular superhero runs past you and runs through Boomerang!!!")
    print("A-Train just killed him in front of your very eyes")
    print("Although he is portrayed as a superhero in the public, he is secretly a villain")
    print("It's now time to face off with another speedster!!!")

    def ATrain():
        try:
            atrain_health = 250
            light_attack = 30
            medium_attack = 60
            attack_choice = int(input("Please choose one of the attacks:"))
            while atrain_health != 0:
                heavy_attack = random.randint(15, 100)
                if attack_choice == 1:
                    print("You have done", light_attack, "damage to A-Train!!!")
                    atrain_health = (atrain_health - light_attack)
                    print("A-Train's health point is now", atrain_health)
                elif attack_choice == 2:
                    print("You have done", medium_attack, "damage to A-Train")
                    atrain_health = (atrain_health - medium_attack)
                    print("A-Train's health point is now", atrain_health)
                elif attack_choice == 3:
                    print("You have done", heavy_attack, "damage to A-Train")
                    atrain_health = (atrain_health - heavy_attack)
                    print("A-Train's health point is now", atrain_health)
                else:
                    print(
                        "The input is incorrect!!!" "Your consequence is that A_train's health has regenerated")
                    print("Please input 1,2 or 3!!!")
                    ATrain()
                if atrain_health <= 0:
                    print("Congratulations you have defeated A_Train!!!")
                    break
                attack_choice = int(input("Please choose one of the attacks"))
        except:
            print("The input is incorrect!!!" "Your consequence is that A-Train's health has regenerated")
            print("Please input 1,2 or 3!!!")
            ATrain()

    ATrain()

    # Scene 6

    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["Y", "y", "yes"]
    no = ["N", "n", "no"]

    tranquilizer_gun = 0
    purple_potion = 0

    required = ("\nUse only A, B, or C\n")

    def mystery():
        print("Great job!!! You have defeated A-Train, however he makes a run for it")
        print("You chase after him!!! He leads you to a dark alley and disappears.")
        print("All of a sudden you hear a massive growl!!!")
        print(
            "Oh no it's Gorilla Grodd, an intelligent telepathic gorilla who has terrorised the city for some time")
        print("He charges at you. What will you do:")
        time.sleep(1)
        print("""  A. Throw a lightning bolt at him
                      B. Stay still
                      C. Run away""")
        choice = input(">>> ")
        if choice in answer_A:
            lightning_bolt()
        elif choice in answer_B:
            print("\nWelp, that was quick.")
            print("You have died")
        elif choice in answer_C:
            run()
        else:
            print(required)
            mystery()

    def lightning_bolt():
        print("The lightning bolt has stunned him, but it wasn't enough as he regains control")
        print("The gorilla charges at you again. What will you do?")
        time.sleep(1)
        print("A. Run")
        print("B. Throw another lightning strike")
        print("C. Run towards a nearby tunnel underground")
        choice = input(">>> ")
        if choice in answer_A:
            run()
        elif choice in answer_B:
            print("\nYou decided to throw another lighting bolt, but the gorilla dodges it. You have died!! ")

        elif choice in answer_C:
            tunnel()
        else:
            print(required)
            lightning_bolt()

    def tunnel():
        print("While your running from the gorilla, you notice a tranquilizer gun")
        print("Do you pick it up. Y/N?")
        choice = input(">>> ")
        if choice in yes:
            tranquilizer_gun = 1
        else:
            tranquilizer_gun = 0
        print("\nWhat do you do next?")
        time.sleep(1)
        print("A. Hide behind a wall")
        print("B. Fight the gorilla")
        print("C. Run")
        choice = input(">>> ")
        if choice in answer_A:
            print("\nHiding wasn't a smart option. He found you!!!, You have died!!")
        elif choice in answer_B:
            if tranquilizer_gun > 0:
                print("\nYou wait for him in the darkness. Aiming down the gun, waiting to get a clear shot.")
                print("You spot him, and shoot him right in chest 3 times. Congrats you have survived!!!")
                print("Homelander appears out of nowhere and takes Gorilla Grodd and proceeds to drop him from the sky")
                Final_Scene()
            else:
                print("\nYou should have picked up that gun.")
                print("You have died!!!")

        elif choice in answer_C:
            print("As the gorilla enters the tunnel")
            print(" You silently sneak out and continue running.")
            print("However, he spots you")
            run()
        else:
            print(required)
            tunnel()

    def run():
        print("You run as quickly as possible, but the gorilla also has super speed, he's catching up!!!")
        print("What will you do?")
        time.sleep(1)
        print(" A. Hide behind a pillar")
        print("B. Enough running, it's time to fight")
        print("C. Continue running")
        choice = input(">>> ")
        if choice in answer_A:
            print("You're easily spotted. The gorilla outsmarted you.")
            print("You have died!!!")
        elif choice in answer_B:
            print("\nYou try your hardest, but he's too strong.")
            print("You have died!!!")

        elif choice in answer_C:
            continue_running()
        else:
            print(required)
            run()

    def continue_running():
        print("While your running down the street")
        print("You notice a purple potion, just sitting there in the middle of the street")
        print("Do you pick it up?")
        choice = input(">>> ")
        if choice in yes:
            purple_potion = 1
        else:
            purple_potion = 0
        print("You hear its heavy footsteps and prepare yourself to fight the beast!!!")
        time.sleep(1)
        if purple_potion > 0:
            print("\nYou quickly drink the potion. It gave you super strength!!!")
            print("You defeated Gorilla Grodd with the help of the potion")
            print("Congratulations, you have survived!!!")
            print("Homelander appears out of nowhere and takes Gorilla Grodd and proceeds to drop him from the sky")
            Final_Scene()
        else:
            print("\nMaybe you should have picked up the potion!!!")
            print("You have died")

    mystery()

def purple_serum():
    # end game
    def end():  # define end function
        # print statements
        print('- - - - - - - - - ')
        print('Game Over!')
        print('Press any key to exit.')

        end = input()  # ask input to confirm exit
        exit()  # exit program

    # scene 2

    # print statements
    print('You chose the purple serum.')
    print('You feel like something is happening to your body but could not tell.')
    print('The soldiers are coming, there is no time to think!!')

    def escape():  # define escape function
        # print statements
        print('- - - - - - - - - ')
        print('There are two ways to try..')
        print('1 - Break the window next to you and jump.')
        print('2 - Run to rooftop through the stairs.')
        print('What will you do?')
        escape_option()  # call escape_option function

    def escape_option():  # define escape_option function
        try:
            escape = int(input('Enter 1 or 2:'))  # ask user to input an integer
            while escape != 2:  # run code below while input is 1 or 2
                if escape == 1:  # call end function if input is 1
                    print('>>>')
                    print(
                        'You break the window and look..50 floors above the ground, that is not a great choice to jump.')
                    print('The soldiers are coming. You jumped.')
                    print('You died.')
                    end()  # call function

                print('Input invaild! Enter 1 or 2 only1')
                escape = int(input('Enter 1 or 2:'))  # ask user to input an integer

            if escape == 2:  # if input is 2 run the code below
                print('>>>')
                print('Sounds great to try.')
                escape_2()  # call escape_2 function\

        except:  # recall function if input is invaild
            print('Input invaild! Enter integer only')
            escape_option()  # call escape function

    def escape_2():  # define escape_2 function
        # print statements
        print('- - - - - - - - - ')
        print('You run as fast as you can and reach the rooftop before those soldiers catch you.')
        print('You look around to find anything that can help you.')
        print('There is backpack on the floor.\n "who left this here?" you think.')
        print('- - - - - - - - - ')
        print('What will you do?')
        print('1 - Check the backpack on the floor.')
        print('2 - Walk around to see if anything else can help.')
        escape_2_option()  # call escape_2_option function

    def escape_2_option():  # define escape_2_option function
        try:
            escape_2 = int(input('Enter 1 or 2: '))  # ask user to input an integer
            if escape_2 in range(1, 3):  # run code below while input is 1 or 2
                if escape_2 == 1:  # if input is 1 run code below
                    print('>>>')
                    print('A paraglider!\nYou use it to fly before the soldiers come to you.')
                elif escape_2 == 2:  # if input is 2 run code below
                    print('>>>')
                    print(
                        'You found a set of rappel on the edge of the bulding.\nMight be left from some window cleaners.')
                    print('You slide down and reach a lower building and run away from those soldiers.')
            else:  # run code below if input is not in range
                print('Input invaild! Enter 1 or 2 only')
                escape_2_option()  # call escape_2_option function
        except:  # recall function if input is invaild
            print('Input invaild! Enter integer only')
            escape_2_option()

    escape()  # call function

    # scene 3
    # print statements
    print('- - - - - - - - - ')
    print('2 WEEKS LATER')
    print('- - - - - - - - - ')

    print('You come home after work very very tired and going to have a nice bath before bed.')
    print('You get a phone call from your best friend Will. (NEW CHARACTER - WILL)')

    call_time = 0  # create a global variable called call_time

    def phone_call():  # define phone_call function
        # print statements
        print('- - - - - - - - - ')
        print('What will you do?')
        print('1 - Pick up the call')
        print('2 - Hang up the call')
        phone_call_option()  # call phone_call_option function

    def phone_call_option():  # define phone_call_option function
        try:
            call = int(input('Enter 1 or 2: '))  # ask user to input an integer
            if call == 1:  # call call_1 function if input is 1
                print('You pick up the phone.')
                call_1()
            elif call == 2:  # run code below if input is not 1
                global call_time  # get value of global variable  call_time
                while call_time < 2:  # run code below while call_time smaller than 2
                    call_time = call_time + 1  # add 1 to call_time
                    call_2()  # call function call_2
                    break
                if call_time == 2:  # run code below if call_time equal to 2
                    call_3()  # call function call_3
            else:  # run code below if input is not in range
                print('Input invaild! Enter 1 or 2 only')
                phone_call_option()
        except:  # recall function if input is invaild
            print('Input invaild! Enter integer only')
            phone_call_option()

    def call_1():  # define call_1 function
        # print statements
        print('Will: "How are you mate？"\n "There is a party tomorrow nigth, you comming?"')
        print('- - - - - - - - - ')
        print('What are you going to say?')
        print('1 - "Yeah, why not."')
        print('2 - "Let me think about it"')
        print('3 - "Cannot be bother, i wanna stay home."')
        call_1_option()  # call call_1_option function

    def call_1_option():  # define call_1_option function
        try:
            call_1 = int(input('Enter 1, 2 or 3:'))  # ask user to input an integer
            while call_1 == 1 or 2 or 3:  # run code below if input is 1,2 or3
                if call_1 == 1:  # run code below if input is 1
                    print('Will: "Cool! See you then!"')
                    break
                if call_1 == 2 or 3:  # run code below when input is not 1
                    print(
                        'Will: "Come on"\n"We did not go to any party for a whole month."\n"You must be there tomorrow. See you there mate."')
                    break
            if call_1 not in range(1, 4):  # run code below if input is not in range
                print('Input invaild! Enter 1, 2 or 3 only')
                call_1()
        except:  # recall function if input is invaild
            print('input invaild!\nEnter integer only')
            call_1_option()

    def call_2():  # define call_2 function
        # print statements
        print('You hung up the call.')
        print('2 MINUTES LATER..\nWill call you again.')
        print('He might have something needs to say.')
        phone_call()  # call phone_call function
        global call_time  # get value of global variable call_time
        if call_time >= 5:  # run code below if call_time equal to 5
            call_3()  # call call_3 function

    def call_3():  # define call_3 function
        # print statments
        print('20 MINUTES LATER..')
        print('"KNOCK KNOCK"\n"Are you there? Open the door."')
        print('It is Will\nYou opend the door and let him in.')
        print('Will: "What were you doing? I was worrying so I came."')
        call_1()  # call function call_1

    phone_call()  # call phone_call function

    # scene 4
    # print statements
    print('- - - - - - - - - ')
    print('NEXT DAY 7PM')
    print('RAINNING')
    print('- - - - - - - - - ')
    travel_1 = 0  # global variable called travel

    def travel():  # define travel funtion
        # print statements
        print('How do you want to travel to the party?')
        print('1 - Walk(30 mins)')
        print('2 - Bus(15 mins)')
        print('3 - Taxi(5 mins)')
        travel_option()  # call travel_option function

    def travel_option():  # define travel_option function
        try:

            travel = int(input('Enter 1, 2 or 3:'))  # ask user to input an integer, update travel

            if travel in range(1, 4):  # run code below while input is 1, 2 or 3
                if travel == 1:  # run code below if input is 1
                    print('You decide to walk.')
                    travel_1()
                elif travel == 2:  # try this if input is not 1
                    print('You decide to take the bus.')
                    travel_2()
                else:  # run code below if input is not 1 or 2
                    print('You decide to call a taxi.')
                    travel_3()
            if travel not in range(1, 4):  # run code below if input not in range
                print('Input invalid! Enter 1, 2 or 3 only.')
                travel()

        except:  # recall function if input is invaild
            print('input invaild!\nEnter integer only')
            travel_option()

    def travel_1():
        # print statements
        print('>>>')
        print('WALKING ON THE STREET TO THE PARTY...')
        print('Suddenly, you see a shadow appear not far ahead. (NEW CHARACTER - SHADOW)')
        print('You feel like he is looking at you, and he disappear in the alley.')
        print('- - - - - - - - - ')
        print('What will you do?')
        print('1. Follow the shadow.')
        print('2. Ignore it and keep going.')
        travel_1_option()  # call travel_1_option function

    def travel_1_option():
        try:
            global travel_1  # get global value travel_1
            travel_1 = int(input('Enter 1 or 2:'))  # ask user to input an integer
            while travel_1 in range(1, 3):  # run code below if input in range
                if travel_1 == 1:  # run code below if input is 1
                    print('You walk into the alley after him.')
                    break
                else:  # run code below if input is not 1
                    # print statements
                    print('You continue walking.')
                    print('You see a girl who looks familiar, you walk up and talk to her.')
                    print(
                        'She turn around and regonise you. She is going to the party as well. (NEW CHARACTER - HAYLEY)')
                    print('You tell her about the shadow, she decided to check it out with you.')
                    print('You walk into the alley looking for the shadow.')
                    shadow()  # call shadow function
                    break  # exit while loop

            if travel_1 not in range(1, 3):  # run code below if input is not in range
                print('Input invalid! Enter 1 or 2 only.')
                travel_1_option()
        except:  # recall function if input is invaild
            print('input invaild!\nEnter integer only')
            travel_1_option()

    def travel_2():
        # print statements
        print('>>>')
        print('ON THE BUS...')
        print(
            '"There is a car accident ahead, if you are hurry, walk to the bus stop next street please." from the bus driver.')

        print('- - - - - - - - - ')
        print('What will you do?')
        print('1. "Yeah sure."')
        print('2. "Just wait on the bus."')

        travel_2_option()  # call travel_2_option function

    def travel_2_option():
        try:
            travel_2 = int(input('Enter 1 or 2:'))  # ask user to input an integer
            while travel_2 != 1:  # run code below while input is not 1
                if travel_2 == 2:  # run code below if input is 2
                    print('You will be late for the party.')
                    break  # exit while loop
                travel_2 = int(input('Enter 1 or 2:'))  # ask user to input an integer
            if travel_2 == 1:  # run code below if input is 1
                print('You get off the bus and walk.')
                fight()  # call fight function
        except:  # recall function if input is invaild
            print('input invaild!\nEnter integer only')
            travel_2_option()

    def travel_3():
        # print statements
        print('>>>')
        print('ON THE TAXI...')
        print(
            'The taxi driver did not sleep well last night. When the traffic light turns red, he did not stop.')
        print('A truck comes from the side with a high speed, hits the taxi.')
        print('You died.')
        end()  # call end function

    # scene 5

    def shadow():
        global travel_1  # get value for global variable travel_1_option
        # print statments
        print('>>>')
        print('It is getting dark, you can barely see when walking in the alley.')
        print('You hear something is moving towards you.')
        print('The shadow is coming to kill you.')

        if travel_1 == 1:  # if Hayley did not appear
            # print statments
            print('The shadow is moving so fast that you can not dodge.')
            print('You get hit by it.')
            print('You died.')
            end()  # call end function

        if travel_1 == 2:  # if Hayley appears
            # print statments
            print('Just before the shadow hits you, Hayley pushes you to the side.')
            print('It missed, and Hayley stabs it from its back with her dagger.')
            print('It falls down, you and Hayley run away.')
            fight()  # call fight funciton

    # scene 6

    def fight():
        # print statments
        print('>>>')
        print('You arrive the party, having fun.')
        print('Suddenly the door is smashed open and a man appears, followed by a group of soldiers')
        print('You regonise them, they were the soldiers from the night when you took the serum.')
        print('You must fight them, with the power given to you by the serum.')
        try:
            # set health points
            soldiers_health = 100
            my_health = 100

            # set attack damage
            wind_attack = random.randint(5, 19)
            lightning_attack = random.randint(20, 39)
            tsunami_attack = random.randint(40, 60)

            # print statments
            print('Which level of attack will you use?')
            print('1. Wind - light attack')
            print('2. Lightning - medium attack')
            print('3. Tsunami - heavy attack')

            attack = int(input('Enter 1, 2 or 3:'))  # ask user to input integer
            while soldiers_health != 0 and my_health != 0:  # run code below if both alive
                if attack == 1:
                    print('You have dealt them', wind_attack, 'points of damage.')
                    soldiers_health = soldiers_health - wind_attack
                    print('Their health point is now', soldiers_health)
                elif attack == 2:
                    print('You have dealt them', lightning_attack, 'points of damage.')
                    soldiers_health = soldiers_health - lightning_attack
                    print('Their health point is now', soldiers_health)
                elif attack == 3:
                    print('You have dealt them', tsunami_attack, 'points of damage.')
                    print('This attack is so strong, yourself also been afftected.')
                    soldiers_health = soldiers_health - tsunami_attack
                    my_health = my_health - tsunami_attack
                    print('Their health point is now', soldiers_health)
                    print('Your health point is now', my_health)

                # if anyone died
                if soldiers_health <= 0:  # if soldiers died
                    print('Congratulations, you have defeated the soldiers.')
                    break  # exit while loop
                if my_health <= 0:  # if user died
                    print('You died.')
                    end()  # call end function

                attack = int(input('Enter 1, 2 or 3:'))  # ask user to input integer


        except:  # recall function if input is invaild
            print('input invaild!\nEnter integer only')
            fight()

    travel()  # call travel function

def black_serum():
    # SCENE 2
    print("One Year Later")  # Prints the statement
    print("You are at work at EB-Hi-Fi\nbored out of your mind\nas usual...")  # Prints the statement in 3 lines
    print(
        "You get a phone call from a customer:\n'How may I help you today?'")  # Prints the statement in 2 lines
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
    print(
        "You decide to open the blinds in your apartment and see minions and the teletubbies casually brawling in the sky")  # Prints the statement
    print(
        "You then close your blinds and go back to gaming like nothings happening outside")  # Prints the statement
    print(
        "Just as you put your headset on, one of the minions falls out of the sky, through your roof, into your apartment")  # Prints the statement
    print(
        "'THAT HOLE IS GONNA COST ME A FORTUNE TO FIX, IM ALREADY BEHIND ON THE BILLS!!' you shout out loud")  # Prints the statement
    print("The minion sees and decides to attack")  # Prints the statement
    print(
        "Without looking, you flick the minion away and it explodes into a million pieces")  # Prints the statement
    print("'NOW I HAVE TO CLEAN THIS TOO!!!'")  # Prints the statement

    # Scene 3
    print(
        "After fixing your roof, \ncleaning the apartment \nand getting rid of the remaining minions and teletubbies with your powers\nyou decide to go back to your normal and average life by continuing to hide your powers")  # Prints the statement
    print(
        "Suddenly your new smartphone starts to ring\nYou decide to answer the call")  # Prints the statement on 2 lines
    print(
        "It's Maeve\nI've got a job for you\nAll you need to do is break into a few banks\nYou'll get a big payday\nIts a in and out job'")  # Prints the statement in 4 lines
    print("1 - I could use the extra cash [Embrace the dark side]")  # Prints the statement
    print("2 - <say nothing>")  # Prints the statement
    print(
        "3 - Sorry, I got out of that life a long time ago [Report them and embrace the light]")  # Prints the statement

    def crime_choice():  # Defines the crime_choice function
        try:  # Trys to run the code below
            crime_input = int(input("What choice will you make: "))  # Allows user to input an integer
            while crime_input == 2:  # While input is 2, run the code below
                print("Come on, you'll be safe in the van, it's low risk. Are you in?")  # Prints the statement
                print("1 - I could use the extra cash [Embrace the dark side]")  # Prints the statement
                print("2 - <say nothing>")  # Prints the statement
                print(
                    "3 - Sorry, I got out of that life [Report them and embrace the light]")  # Prints the statement
                crime_input = int(input("What choice will you make: "))  # Allows user to input an integer
            if crime_input == 1:  # If input is 1, run the code below
                print("Great!\nMeet me at 145 Elm Street at 10pm")  # Prints the statement on 2 lines
                print("You meet Maeve at the address and are waiting for her to arrive")  # Prints the statement
                print("Its been 20 minutes and you are starting to get suspicious")  # Prints the statement
                print("You receive a voicemail from Maeve")  # Prints the statement
                print(
                    "I know it was you who broke into the factory and tried to destroy the last of super serums, she says")  # Prints the statement
                print(
                    "Before you can react, you are surrounded by entire police force and the countrys special forces")  # Prints the statement
                print(
                    "You get out of your car and they see that as a threat and proceed to shoot you")  # Prints the statement
                print("Too bad they didnt know you had super powers")  # Prints the statement
                print("You defeat all of them and decide to run")  # Prints the statement
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

    # SCENE 4
    print("You get in your car and put your home address into the gps")  # Prints the statement
    print("You finally reach the destination after half an hours of driving")  # Prints the statement
    print("Suddenly your old friend Lenny knocks on your door")  # Prints the statement
    print(
        "After conversing with Lenny you find out Maeve has kidnapped his family so you get in the van with him")  # Prints the statement
    print("You reach the building where Lenny's family is being held")  # Prints the statement
    print("Its time for you to use your powers once again")  # Prints the statement

    print("The miniboss 'Mike Tyson's' health is 20, how do you choose to attack it?")  # Prints the statement
    print("1 - Try to run past [No Damage]")  # Prints the statement
    print("2 - Super Kick [Random Damage]")  # Prints the statement
    print("3 - Hyper Punch [Two Shot]")  # Prints the statement

    def attack_choice():  # Defines the attack_choice function
        try:  # Trys to run the code below
            miniboss_health = 20  # Defines miniboss_health as 20
            attack_input = int(input("What attack will you use: "))  # Allows user to input an integer
            while miniboss_health > 0:  # While miniboss_health is more than 0, run the code below
                random_damage = random.randint(1,
                                               miniboss_health)  # Defines random_damage as a random integer between 1 and the miniboss_health
                if attack_input == 1:  # If input is 1, run the code below
                    print("You have done 0 damage to Mike Tyson")  # Prints the statement
                elif attack_input == 2:  # If input is 2, run the code below
                    print("You have done", random_damage,
                          "damage to Mike Tyson")  # Prints the statement and random_damage
                    miniboss_health = (
                            miniboss_health - random_damage)  # Redefines miniboss_health as random_damage subtracting from miniboss_health
                    print("Mike Tyson's health is", miniboss_health)  # Prints the statement and miniboss_health
                elif attack_input == 3:  # If input is 3, run the code below
                    print("One more shot to take down Mike Tyson")  # Prints the statement
                    miniboss_health = 0  # Redefines miniboss_health as 0
                else:  # Runs the code below if the input is not 1, 2 or 3
                    print("Try Again")  # Prints the statement
                    attack_choice()  # Runs the attack_choice function
                attack_input = int(input("What attack will you use: "))  # Allows user to input an integer
                if miniboss_health <= 0:  # If miniboss_health is less than or equal to 0, it runs the code below
                    print("You defeat Mike Tyson and carry on")  # Prints the statement
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please enter 1, 2 or 3 only")  # Prints the statement
            attack_choice()  # Runs the attack_choice function

    attack_choice()  # Calls the attack_choice function

    # SCENE 5
    print(
        "After defeating the miniboss Mike Tyson, you need you to hack each of the 4 electronic locks on the safe doors")  # Prints the statement
    print(
        "You use your hacking experience from your extensive and boring career at EB Hi-Fi")  # Prints the statement

    def door1_choice():  # Defines the door1_choice function
        try:  # Trys to run the code below
            hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]",
                         "4-SQL Injection [Two Shot]"]  # Defines hack_list as the statement provided
            print("You access lock 1 of 4")  # Prints the statement
            print(hack_list)  # Prints hack_list
            door1_health = 30  # Defines door1_health as 30
            hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
            while door1_health > 0:  # While door1_health is more than 0, run the code below
                random_hack_damage = random.uniform(1,
                                                    door1_health)  # Defines random_hack_damage as a random integer between 1 and the door1_health
                random_hack_damage = float(
                    random_hack_damage)  # Declares random_hack_damage as a float data type
                if hack_input == 1:  # If input is 1, run the code below
                    print("You have done 0 damage to the lock system")  # Prints the statement
                elif hack_input == 2:  # If input is 2, run the code below
                    print("You have done 5 damage to the lock system")  # Prints the statement
                    door1_health = (door1_health - 5)  # Redefines door1_health as door1_health subtracting 5
                    print("The lock systems health is", door1_health)  # Prints the statement and door1_health
                elif hack_input == 3:  # If input is 3, run the code below
                    print("You have done", random_hack_damage,
                          "damage to the lock system")  # Prints the statement and random_hack_damage
                    door1_health = (
                            door1_health - random_hack_damage)  # Redefines door1_health as random_hack_damage subtracted from door1_health
                    print("The lock systems health is", door1_health)  # Prints the statement and door1_health
                elif hack_input == 4:  # If input is 4, run the code below
                    print("One more shot to take down the lock system")  # Prints the statement
                    door1_health = 0  # Redefines door1_health as 0
                else:  # Runs the code below if the input is not 1, 2, 3 or 4
                    print("Try Again")  # Prints the statement
                    door1_choice()  # Runs the door1_choice function
                hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
                if door1_health <= 0:  # If door1_health is less than or equal to 0, it runs the code below
                    print("You have disabled the lock of door 1")  # Prints the statement
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please enter 1, 2, 3 or 4")  # Prints the statement
            print("The lock is now full health again, you will have to start again")  # Prints the statement
            door1_choice()  # Runs the door1_choice function

    door1_choice()  # Calls the door1_choice function

    def door2_choice():  # Defines the door2_choice function
        try:  # Trys to run the code below
            hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]",
                         "4-SQL Injection [Two Shot]"]  # Defines hack_list as the statement provided
            print("You access lock 2 of 4")  # Prints the statement
            print(hack_list)  # Prints hack_list
            door2_health = 30  # Defines door2_health as 30
            hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
            while door2_health > 0:  # While door2_health is more than 0, run the code below
                random_hack_damage = random.uniform(1,
                                                    door2_health)  # Defines random_hack_damage as a random integer between 1 and the door2_health
                random_hack_damage = float(
                    random_hack_damage)  # Declares random_hack_damage as a float data type
                if hack_input == 1:  # If input is 1, run the code below
                    print("You have done 0 damage to the lock system")  # Prints the statement
                elif hack_input == 2:  # If input is 2, run the code below
                    print("You have done 5 damage to the lock system")  # Prints the statement
                    door2_health = (door2_health - 5)  # Redefines door2_health as door2_health subtracting 5
                    print("The lock systems health is", door2_health)  # Prints the statement and door2_health
                elif hack_input == 3:  # If input is 3, run the code below
                    print("You have done", random_hack_damage,
                          "damage to the lock system")  # Prints the statement and random_hack_damage
                    door2_health = (
                            door2_health - random_hack_damage)  # Redefines door2_health as random_hack_damage subtracted from door2_health
                    print("The lock systems health is", door2_health)  # Prints the statement and door2_health
                elif hack_input == 4:  # If input is 4, run the code below
                    print("One more shot to take down the lock system")  # Prints the statement
                    door2_health = 0  # Redefines door2_health as 0
                else:  # If the code is not 1, 2, 3 or 4, it runs the code below
                    print("Try Again")  # Prints the statement
                    door2_choice()  # Runs the door2_choice function
                hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
                if door2_health <= 0:  # If door2_health is less than or equal to 0, it runs the code below
                    print("You have disabled the lock of door 2")  # Prints the statement
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please enter 1, 2, 3 or 4")  # Prints the statement
            print("The lock is now full health again, you will have to start again")  # Prints the statement
            door2_choice()  # Runs the door2_choice function

    door2_choice()  # Calls the door2_choice function

    def door3_choice():
        try:  # Trys to run the code below
            hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]",
                         "4-SQL Injection [Two Shot]"]  # Defines hack_list as the statement provided
            print("You access lock 3 of 4")  # Prints the statement
            print(hack_list)  # Prints hack_list
            door3_health = 30  # Defines door3_health as 30
            hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
            while door3_health > 0:  # While door3_health is more than 0, run the code below
                random_hack_damage = random.uniform(1,
                                                    door3_health)  # Defines random_hack_damage as a random integer between 1 and the door3_health
                random_hack_damage = float(
                    random_hack_damage)  # Declares random_hack_damage as a float data type
                if hack_input == 1:  # If input is 1, run the code below
                    print("You have done 0 damage to the lock system")  # Prints the statement
                elif hack_input == 2:  # If input is 2, run the code below
                    print("You have done 5 damage to the lock system")  # Prints the statement
                    door3_health = (door3_health - 5)  # Redefines door3_health as door3_health subtracting 5
                    print("The lock systems health is", door3_health)  # Prints the statement and door3_health
                elif hack_input == 3:  # If input is 3, run the code below
                    print("You have done", random_hack_damage,
                          "damage to the lock system")  # Prints the statement and random_hack_damage
                    door3_health = (
                            door3_health - random_hack_damage)  # Redefines door3_health as random_hack_damage subtracted from door3_health
                    print("The lock systems health is", door3_health)  # Prints the statement and door3_health
                elif hack_input == 4:  # If input is 4, run the code below
                    print("One more shot to take down the lock system")  # Prints the statement
                    door3_health = 0  # Redefines door4_health as 0
                else:  # If the code is not 1, 2, 3 or 4, it runs the code below
                    print("Try Again")  # Prints the statement
                    door3_choice()  # Runs the door3_choice function
                hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
                if door3_health <= 0:  # If door3_health is less than or equal to 0, it runs the code below
                    print("You have disabled the lock of door 3")  # Prints the statement
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please enter 1, 2, 3 or 4")  # Prints the statement
            print("The lock is now full health again, you will have to start again")  # Prints the statement
            door3_choice()  # Runs the door3_choice function

    door3_choice()  # Calls the door3_choice function

    def door4_choice():
        try:  # Trys to run the code below
            hack_list = ["1-Phishing [0 Damage]", "2-DDoS [5 Damage]", "3-Trojan [Random Damage]",
                         "4-SQL Injection [Two Shot]"]  # Defines hack_list as the statement provided
            print("You access lock 4 of 4")  # Prints the statement
            print(hack_list)  # Prints hack_list
            door4_health = 30  # Defines door4_health as 30
            hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
            while door4_health > 0:  # While door4_health is more than 0, run the code below
                random_hack_damage = random.uniform(1,
                                                    door4_health)  # Defines random_hack_damage as a random integer between 1 and the door4_health
                random_hack_damage = float(
                    random_hack_damage)  # Declares random_hack_damage as a float data type
                if hack_input == 1:  # If input is 1, run the code below
                    print("You have done 0 damage to the lock system")  # Prints the statement
                elif hack_input == 2:  # If input is 2, run the code below
                    print("You have done 5 damage to the lock system")  # Prints the statement
                    door4_health = (door4_health - 5)  # Redefines door4_health as door4_health subtracting 5
                    print("The lock systems health is", door4_health)  # Prints the statement and door4_health
                elif hack_input == 3:  # If input is 3, run the code below
                    print("You have done", random_hack_damage,
                          "damage to the lock system")  # Prints the statement and random_hack_damage
                    door4_health = (
                            door4_health - random_hack_damage)  # Redefines door4_health as random_hack_damage subtracted from door4_health
                    print("The lock systems health is", door4_health)  # Prints the statement and door4_health
                elif hack_input == 4:  # If input is 4, run the code below
                    print("One more shot to take down the lock system")  # Prints the statement
                    door4_health = 0  # Redefines door4_health as 0
                else:  # If the code is not 1, 2, 3 or 4, it runs the code below
                    print("Try Again")  # Prints the statement
                    door4_choice()  # Runs the door4_choice function
                hack_input = int(input("Which hack would you like to use: "))  # Allows user to input an integer
                if door4_health <= 0:  # If door4_health is less than or equal to 0, it runs the code below
                    print("You have disabled the lock of door 4")  # Prints the statement
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please enter 1, 2, 3 or 4")  # Prints the statement
            print("The lock is now full health again, you will have to start again")  # Prints the statement
            door4_choice()  # Runs the door4_choice function

    door4_choice()  # Callss the door4_choice function

    print("You have successfully unlocked all 4 doors")  # Prints the statement
    print(
        "After unlocking all the doors, you see that Maeve has escaped prison and is now holding your mother and father hostage")  # Prints the statement
    print("You realise Lenny had led you on and betrayed you")  # Prints the statement

    # SCENE 6
    print(
        "Just as you are about to free your mother and father, Maeve drops from the roof in the last second and kicks you away")  # Prints the statement
    print(
        "It seems this whole thing was a trap to kill you but luckily you called 3 of your closest military friends to help")  # Prints the statement
    print("She takes a newly made serum and it seems it multiplies her powers by 10")
    print("This fight is unwinnable but she has your parents")
    print("BOSS FIGHT: Maeve")

    def rating_choice():  # Defines the rating_choice function
        try:  # Trys to run the code below
            rating = float(input(
                "Please rate the game on a scale from 0.0 to 1.0, 0.0 - 0.1 being bad and 0.9 - 1.0 being good: "))  # Allows user to input a float
            while rating == "":  # While input is empty, run the code below
                rating = float(input(
                    "Please rate the game on a scale from 0.0 to 1.0, 0.0 - 0.1 being bad and 0.9 - 1.0 being good: "))  # Allows user to input a float
            while rating > 1.0:  # While input is more then 1.0, run the code below
                print("Choose between 0.0 - 1.0 only")  # Prints the statement
                rating = float(input(
                    "Please rate the game on a scale from 0.0 to 1.0, 0.0 - 0.1 being bad and 0.9 - 1.0 being good: "))  # Allows user to input a float
            print("Thank you for rating the game a", rating, "out of 1.0")  # Prints the statement and rating
        except:  # Runs the code below to avoid error in case of wrong input
            print("Enter in a float only")  # Prints the statement
            rating_choice()  # Runs the rating_choice function

    def escape3_choice():  # Defines the escape3_choice function
        try:  # Trys to run the code below
            print("What would you like to do?")  # Prints the statement
            print("1 - Leave your parents and run like a coward")  # Prints the statement
            print(
                "2 - Alert your team to fall back from the trap to get her by herself")  # Prints the statement
            print("3 - Try and fight a suped up Maeve")  # Prints the statement
            escape_input = int(input("What will you do: "))  # Allows user to input an integer
            if escape_input == 1:  # If the input is 1, run the code below
                print("You quickly get outside but Maeve is right behind you")  # Prints the statement
                print(
                    "While you may have your superpowers, you know if she even hits you, you will explode into a million pieces")  # Prints the statement
                print("You keep running but unfortunately she catches up to you")  # Prints the statement
                print(
                    "You beg for your life but before you can say a word she kills you so quick you didnt realise you died until 2 seconds later")  # Prints the statement
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            elif escape_input == 2:  # If the input is 2, run the code below
                print(
                    "The last team member makes it back but Maeve runs after you and your team")  # Prints the statement
                print("Luckily your team called for backup")  # Prints the statement
                print("The newly appointed joint super task force arrives just in time")  # Prints the statement
                print("Both the Avengers and the Justice League have come to your aid")  # Prints the statement
                print(
                    "Maeve isnt scared and try's to outflank them but theres too many of them")  # Prints the statement
                print(
                    "She gets pummeled so hard by everybody and is eventually captured to be held in the new supermax cell designed just for her")  # Prints the statement
                print("You thank the task force and save your parents")  # Prints the statement
                print("Unfortunately Homelander comes out of nowhere")
                Final_Scene()
            elif escape_input == 3:  # If the input is 3, run the code below
                print("You attempt to save your parents")  # Prints the statement
                print("Its you, your team and Maeve ")  # Prints the statement
                print(
                    "he first team member attempts to attack her thinking she will be weak")  # Prints the statement
                print(
                    "Before he has a chance to even touch her, he gets hit so hard, his body is flung to the other side of the warehouse")  # Prints the statement
                print("The second team member attempts to gun her down with an AK-47")  # Prints the statement
                print("Unfortunately he doesnt know that shes bullet proof")  # Prints the statement
                print(
                    "Maeve quickly jumps in the air and fly kicks him out of existence")  # Prints the statement
                print(
                    "The last team member, after seeing his other two team members die in front of his eyes, decides to run but Maeve throws a rock from the ground to his head")  # Prints the statement
                print(
                    "In doing so, his head explodes and in turn you are the last one left")  # Prints the statement
                print("Its you and Maeve in the ring")  # Prints the statement
                print("You ask her why she is going to such lengths to hurt you")  # Prints the statement
                print(
                    "She says you decided to get rid of what made her special so she is trying to get rid of you")  # Prints the statement
                print(
                    "You try and talk her down but she see what you are trying to do and runs towards you")  # Prints the statement
                print("You two engage in a battle each blocking each others hits")  # Prints the statement
                print(
                    "You start to get tired and it feels like you are losing your powers as each hit does more and more damage")  # Prints the statement
                print("You cant go anymore and Maeve gets in one last hit")  # Prints the statement
                print("Unfortunately she kills you so quick you didnt realise you died until 2 seconds later")
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            else:  # Runs the code below if the input is not 1, 2 or 3
                print("Try Again!")  # Prints the statement
                escape3_choice()  # Runs the escape3_choice function
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please choose 1, 2 or 3")  # Prints the statement
            escape3_choice()  # Runs the escape3_choice function

    def escape2_choice():  # Defines the escape2_choice function
        try:  # Trys to run the code below
            print("What would you like to do?")  # Prints the statement
            print("1 - Leave your parents and run like a coward")  # Prints the statement
            print(
                "2 - Alert your team to fall back from the trap to get her by herself")  # Prints the statement
            print("3 - Try and fight a suped up Maeve")  # Prints the statement
            escape_input = int(input("What will you do: "))  # Allows user to input an integer
            if escape_input == 1:  # If the input is 1, run the code below
                print("You quickly get outside but Maeve is right behind you")  # Prints the statement
                print(
                    "While you may have your superpowers, you know if she even hits you, you will explode into a million pieces")  # Prints the statement
                print("You keep running but unfortunately she catches up to you")  # Prints the statement
                print(
                    "You beg for your life but before you can say a word she kills you so quick you didnt realise you died until 2 seconds later")  # Prints the statement
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            elif escape_input == 2:  # If the input is 2, run the code below
                print(
                    "Another person makes it back, but the last team member is still in there")  # Prints the statement
                escape3_choice()  # Runs the escape3_choice function
            elif escape_input == 3:  # If the input is 3, run the code below
                print("You attempt to save your parents")  # Prints the statement
                print("Its you, your team and Maeve ")  # Prints the statement
                print("he first team member attempts to attack her thinking she will be weak")  # Prints the statement
                print(
                    "Before he has a chance to even touch her, he gets hit so hard, his body is flung to the other side of the warehouse")  # Prints the statement
                print("The second team member attempts to gun her down with an AK-47")  # Prints the statement
                print("Unfortunately he doesnt know that shes bullet proof")  # Prints the statement
                print("Maeve quickly jumps in the air and fly kicks him out of existence")  # Prints the statement
                print(
                    "The last team member, after seeing his other two team members die in front of his eyes, decides to run but Maeve throws a rock from the ground to his head")  # Prints the statement
                print("In doing so, his head explodes and in turn you are the last one left")  # Prints the statement
                print("Its you and Maeve in the ring")  # Prints the statement
                print("You ask her why she is going to such lengths to hurt you")  # Prints the statement
                print(
                    "She says you decided to get rid of what made her special so she is trying to get rid of you")  # Prints the statement
                print(
                    "You try and talk her down but she see what you are trying to do and runs towards you")  # Prints the statement
                print("You two engage in a battle each blocking each others hits")  # Prints the statement
                print(
                    "You start to get tired and it feels like you are losing your powers as each hit does more and more damage")  # Prints the statement
                print("You cant go anymore and Maeve gets in one last hit")  # Prints the statement
                print("Unfortunately she kills you so quick you didnt realise you died until 2 seconds later")
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            else:  # Runs the code below if the input is not 1, 2 or 3
                print("Try Again!")  # Prints the statement
                escape2_choice()  # Runs the escape2_choice function
            escape_input = int(input("What will you do: "))  # Allows user to input an integer
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please choose 1, 2 or 3")  # Prints the statement
            escape2_choice()  # Runs the escape2_choice function

    def escape1_choice():  # Defines the escape1_choice function
        try:  # Trys to run the code below
            print("What would you like to do?")  # Prints the statement
            print("1 - Leave your parents and run like a coward")  # Prints the statement
            print(
                "2 - Alert your team to fall back from the trap to get her by herself")  # Prints the statement
            print("3 - Try and fight a suped up Maeve")  # Prints the statement
            escape_input = int(input("What will you do: "))  # Allows user to input an integer
            if escape_input == 1:  # If the input is 1, run the code below
                print("You quickly get outside but Maeve is right behind you")  # Prints the statement
                print(
                    "While you may have your superpowers, you know if she even hits you, you will explode into a million pieces")  # Prints the statement
                print("You keep running but unfortunately she catches up to you")  # Prints the statement
                print(
                    "You beg for your life but before you can say a word she kills you so quick you didnt realise you died until 2 seconds later")  # Prints the statement
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            elif escape_input == 2:  # If the input is 2, run the code below
                print("While 1 person makes it back, the other 2 are still in there")  # Prints the statement
                escape2_choice()  # Runs the escape2_choice function
            elif escape_input == 3:  # If the input is 3, run the code below
                print("You attempt to save your parents")  # Prints the statement
                print("Its you, your team and Maeve ")  # Prints the statement
                print(
                    "he first team member attempts to attack her thinking she will be weak")  # Prints the statement
                print(
                    "Before he has a chance to even touch her, he gets hit so hard, his body is flung to the other side of the warehouse")  # Prints the statement
                print("The second team member attempts to gun her down with an AK-47")  # Prints the statement
                print("Unfortunately he doesnt know that shes bullet proof")  # Prints the statement
                print(
                    "Maeve quickly jumps in the air and fly kicks him out of existence")  # Prints the statement
                print(
                    "The last team member, after seeing his other two team members die in front of his eyes, decides to run but Maeve throws a rock from the ground to his head")  # Prints the statement
                print(
                    "In doing so, his head explodes and in turn you are the last one left")  # Prints the statement
                print("Its you and Maeve in the ring")  # Prints the statement
                print("You ask her why she is going to such lengths to hurt you")  # Prints the statement
                print(
                    "She says you decided to get rid of what made her special so she is trying to get rid of you")  # Prints the statement
                print(
                    "You try and talk her down but she see what you are trying to do and runs towards you")  # Prints the statement
                print("You two engage in a battle each blocking each others hits")  # Prints the statement
                print(
                    "You start to get tired and it feels like you are losing your powers as each hit does more and more damage")  # Prints the statement
                print("You cant go anymore and Maeve gets in one last hit")  # Prints the statement
                print("Unfortunately she kills you so quick you didnt realise you died until 2 seconds later")
                print("You were an honorary team member at EB-Hi-Fi")  # Prints the statement
                print(
                    "You were a honest person but unfortunately got caught up in a world where you didnt belong")  # Prints the statement
                print("Thank you for playing The Boys: Text-Based Game!")  # Prints the statement
                rating_choice()  # Runs the rating_choice function
                os._exit(1)  # Uses the os module to exit the code
            else:  # Runs the code below if the input is not 1, 2 or 3
                print("Try Again!")  # Prints the statement
                escape1_choice()  # Runs the escape1_choice function
            escape_input = int(input("What will you do: "))  # Allows user to input an integer
        except:  # Runs the code below to avoid error in case of wrong input
            print("Please choose 1, 2 or 3")  # Prints the statement
            escape1_choice()  # Runs the escape1_choice function

    escape1_choice()  # Calls the escape1_choice function

    escape2_choice()  # Calls the escape2_choice function

    escape3_choice()  # Calls the escape3_choice function


#Intro
print("You finally break into the restricted facility to destroy the super serums that have terrorised the city")
print("However you accidentally trigger an alarm and dozens of soldiers approach and find yourself in a difficult situation")
print("The serum you have come to destroy is the only thing that can save your life.")
print("It is time to break your morals and choose a serum that will save your life.")
print("Blue Serum=ability to fly and shoot lasers out of your eyes\nRed Serum=ability to run like the flash\nPurple Serum=ability to control weather\nBlack Serum=super strength and high durability\n")

# Ending
def Final_Choice():
    try:
        choice = int(input(
            "1. Will you go through with this and finally get your revenge?\nor\n2. Will You let him live and keep your humanity in turn?"))
        if choice == 1:
            print("You double down and squeeze harder....\nFeeling his heartbeat begin to fade....\n")
            sleep(4)
            print(
                "After feeling his life leave his body you turn to the crowd of vaught employees that had gathered to watch...\n")
            sleep(3)
            print(
                "You see red and attack...somehow justifying that they are guilty too by association...\n")
            sleep(2)
            print("as if in the final irony....you too have become...\n...")
            sleep(1)
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("A monster too...")
            os._exit(1)



        elif choice == 2:
            print("You gingerly release pressure and look at the crowed gathered around you\n")
            sleep(3)
            print("You realise that they think your murdering a hero... and that you're the villain\n")
            sleep(3)
            print("You get up and run as fast and as hard as you can to get away from the crowed.\n")
            sleep(3)
            print(
                "with cameras flashing and people screaming you manage to knock a man off his motorbike and ride away\n")
            sleep(3)
            print("You think to yourself\n")
            sleep(2)
            print("You might have lost your chance of revenge...but what you didn't loose...\n")
            sleep(3)
            print("Was your humanity...")
            os._exit(1)


        else:
            print("Only Enter Required Integers!")
            Final_Choice()
    except:
        print("Only Enter Required Integers")
        Final_Choice()


def battle(Villian_Name, Villian_Health):
    import os
    import random
    Health = Villian_Health
    User_Health = 100
    print(Villian_Name + " prepares to go on the offensive! What do you do?")

    while User_Health > 0 and Health > 0:
        print("Attacks:")
        print("1. Punch")
        print("2. Kick")
        print("3. Special")

        try:
            choice = int(input("WHAT WILL YOU DO?!"))
            print(choice)
            if choice == 1:
                damage = random.randint(5, 10)
                print("YOU PUNCH AND DEAL " + str(damage) + " To " + Villian_Name)
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")

            elif choice == 2:
                damage = random.randint(10, 20)
                print("YOU KICK AND DEAL " + str(damage) + " To " + Villian_Name)
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")

            elif choice == 3:
                damage = random.randint(50, 75)
                print("YOU CHARGE AT THEM AND WITH YOUR NEW FOUND STRENGHT AND DEAL " + str(
                    damage) + " To " + Villian_Name)
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")


        except:
            print("You didnt attack!")
            print(
                Villian_Name + " Sees you hesitate and KICKS your head off.\nYou failed your friends and the world is doomed now")
            os._exit(1)

        Villian_Damage = random.randint(10, 30)
        User_Health = User_Health - Villian_Damage
        print(Villian_Name + " Does " + str(Villian_Damage) + " Damage To You!")
        print("You have " + str(User_Health) + " Health Left! Be careFul!")
        print("\n")

    print("You defeated " + Villian_Name)


def Final_Scene():
    sleep(3)
    print("You slowly and cutiously make your way towards Homelander\n")
    sleep(2)
    print(
        "Every Step you take you can hear your heart beat, your sweat bead on your forehead you can ~feel~ the thickness in the air\n")
    sleep(2)
    print("You dont take your eyes off your friend...who has, over the past months, become family..\n")
    sleep(3)
    print(
        "You hear HomeLander yell the words\n*I WOULDNT COME ANY CLOSER! OTHERWISE YOUR LITTLE FRIEND HERE GETS IT!*\n")
    sleep(3)
    print(
        "*You slow your breathing and make eyecontact with your friend. With Their eyes glazed over they grin at you and reach of their knife\n")
    sleep(4)
    print("NOOOOOOOOOOO\nYou scream at the top of your lungs\n")
    sleep(2)
    print("You feel as if your lungs are about to give out\n")
    sleep(3)
    print(
        "You look over and as if youre watching in slow motion you see Homelander look down at them and grin.\n")
    sleep(3)
    print(
        "You see Homelanders eyes glow red and you beggin sprinting towards them\nEven with your new found strength and speed from the serum you know you make it in time\n")
    sleep(5)
    print(
        "Whilst sprinting towards them you seeing Homelanders lazer connect with your frie...no familys head....thats it...theyre gone\n")
    sleep(5)
    print("As if by instinct you immedietly go for the kill\n")
    battle("HomeLander", 250)

    sleep(4)
    print("Between panting desperate breaths you pin Homelander to the ground\n")
    sleep(3)
    print(
        "Blinded with anger you place your hands around his neck and think back to everything he has done to ruin your line\n")
    sleep(2)
    print("EVERYTHING HE HAS DONE TO YOU FRIENDS AND FAMILY. EVEN THEN WORLD\n")
    sleep(2)
    print("You begin to squeeze with all your might until the memories\n")
    sleep(2)
    print(
        "With the memories eating you alive you think tou yourself...is it all worth it... taking a life?")
    Final_Choice()

def serum_choice():  # Defines the game_choice function
    try:  # Trys to run the code below
        print("Choose Serum 1,2,3 or 4")
        pathway_input = int(input("What Serum will I choose?"))  # Allows user to input an integer
        if pathway_input == 1:  # If input is 1, run the code below
            blue_serum()
        elif pathway_input == 2:  # If input is 2, run the code below
            red_serum()
        elif pathway_input == 3:  # If input is 3, run the code below
            purple_serum()
        elif pathway_input == 4:  # If input is 4, run the code below
            black_serum()
        else:  # If the input is not 1, 2, 3 or 4, it runs the code below
            print("Try again")  # Prints the statement
            serum_choice()  # Runs the game_choice function
    except:  # Runs the code below to avoid error in case of wrong input
        print("Please enter a number between 1 and 4 only")  # Prints the statement
        serum_choice()  # Runs the game_choice function

serum_choice()  # Calls the game_choice function


