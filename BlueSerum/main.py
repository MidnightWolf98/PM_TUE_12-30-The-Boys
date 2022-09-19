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

#my_loading()

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

print("1. Unleash the rage building inside and charge the shooters\n2. Grab Frenchie and Run")


def ShotScene1():
    try:
        choice = int(input("WHAT WILL YOU DO?!"))
        if choice == 1:
            print("SCENE B1")
        elif choice == 2:
            print("SCENEA1")
        else:
            print("Only Enter Required Integers!")
            ShotScene1()
    except:
        print("Only Enter Required Integers")
        ShotScene1()

ShotScene1()