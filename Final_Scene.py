def Final_Choice():
    import time
    from time import sleep
    import sys
    import os
    try:
        choice = int(input("1. Will you go trhough with this and finally get your revenge?\nor\n2. Will YOu let him live and keep your humanity in turn?"))
        if choice == 1:
            print("You double down and squueze harder....\nFeeling his heartbeat begin to fade....\n")
            sleep(4)
            print("After feeling his life leave his body you turn to the crowed of vaught employees that had gathered to watch...\n")
            sleep(3)
            print("You see red and attack...somehow justifying that they are guily too by association...\n")
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
            print("You realise that they think your murdering a hero... and that youre the villian\n")
            sleep(3)
            print("You get up and run as fast and as hard as you can to get away from the crowed.\n")
            sleep(3)
            print("with cameras flashing and people screaming you manage to knock a man off his motorbike and ride away\n")
            sleep(3)
            print("You think to yourself\n")
            sleep(2)
            print("You might have lost your chance of revenge...but what you didnt loose...\n")
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
                damage = random.randint(5,10)
                print("YOU PUNCH AND DEAL " + str(damage) + " To " +Villian_Name )
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")

            elif choice == 2:
                damage = random.randint(10, 20)
                print("YOU KICK AND DEAL " + str(damage) + " To " + Villian_Name)
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")

            elif choice == 3:
                damage = random.randint(50, 75)
                print("YOU CHARGE AT THEM AND WITH YOUR NEW FOUND STRENGHT AND DEAL " + str(damage) + " To " + Villian_Name)
                Health = Health - damage
                print(Villian_Name + " Has " + str(Health) + " remaining")


        except:
            print("You didnt attack!")
            print(Villian_Name + " Sees you hesitate and KICKS your head off.\nYou failed your friends and the world is doomed now")
            os._exit(1)




        Villian_Damage = random.randint(10,30)
        User_Health = User_Health - Villian_Damage
        print(Villian_Name + " Does " + str(Villian_Damage) + " Damage To You!")
        print("You have " + str(User_Health) + " Health Left! Be careFul!")
        print("\n")

    print("You defeated " + Villian_Name)


def Final_Scene():
    import sys
    import time
    from time import sleep


    sleep(3)
    print("You slowly and cutiously make your way towards Homelander\n")
    sleep(2)
    print("Every Step you take you can hear your heart beat, your sweat bead on your forehead you can ~feel~ the thickness in the air\n")
    sleep(2)
    print("You dont take your eyes off your friend...who has, over the past months, become family..\n")
    sleep(3)
    print("You hear HomeLander yell the worhds\n*I WOULDNT COME ANY CLOSER! OTHERWISE YOUR LITTLE FRIEND HERE GETS IT!*\n")
    sleep(3)
    print("*You slow your breathing and make eyecontact with your friend. With Their eyes glazed over they grin at you and reach of their knife\n")
    sleep(4)
    print("NOOOOOOOOOOO\nYou scream at the top of your lungs\n")
    sleep(2)
    print("You feel as if your lungs are about to give out\n")
    sleep(3)
    print("You look over and as if youre watching in slow motion you see Homelander look down at them and grin.\n")
    sleep(3)
    print("You see Homelanders eyes glow red and you beggin sprinting towards them\nEven with your new found strength and speed from the serum you know you make it in time\n")
    sleep(5)
    print("Whilst sprinting towards them you seeing Homelanders lazer connect with your frie...no familys head....thats it...theyre gone\n")
    sleep(5)
    print("As if by instict you immedietly go for the kill\n")
    battle("HomeLander", 250)

    sleep(4)
    print("Between panting desperate breaths you pin Homelander to the ground\n")
    sleep(3)
    print("Blinded with anger you place your hands around his neck and think back to everything he has done to ruin your line\n")
    sleep(2)
    print("EVERYTHING HE HAS DONE TO YOU FRIENDS AND FAMILY. EVEN THEN WORLD\n")
    sleep(2)
    print("You begin to squeeze with all your might until the memories\n")
    sleep(2)
    print("With the memories eating you alive you think tou yourself...is it all worth it... taking a life?")
    Final_Choice()


Final_Scene()