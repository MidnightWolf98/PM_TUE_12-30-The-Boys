import random
import os
import time
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
print("3: I have recently heard rumors of a secret underground facility in the middle of the city.", "\n" "That's where you will probably find your answer detective.")

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
            print("I didn't know this place existed" "\n" "you might have just helped us take down this gangster!!!")
    except:
        print("Please input integers (1,2,3) only! Try again!!")
        address()

address()

#Scene 3
print("Some time after the detective leaves your apartment, you suddenly begin to hear loud sirens going past your building.")
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
            print("You have chosen to ignore the situation! Innocents have died because of your consequences!!!")
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
        light_attack= 30
        medium_attack = 60
        attack_choice = int(input("Please choose one of the attacks:"))
        while boomerang_health != 0:
            heavy_attack = random.randint(15,100)
            if attack_choice == 1:
                print("You have done", light_attack,"damage to Boomerang!!!")
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
                print("The input is incorrect!!!" "Your consequence is that Boomerang's health has regenerated")
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
        light_attack= 30
        medium_attack = 60
        attack_choice = int(input("Please choose one of the attacks:"))
        while atrain_health != 0:
            heavy_attack = random.randint(15,100)
            if attack_choice == 1:
                print("You have done", light_attack,"damage to A-Train!!!")
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
                print("The input is incorrect!!!" "Your consequence is that A_train's health has regenerated")
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
    print("Oh no it's Gorilla Grodd, an intelligent telepathic gorilla who has terrorised the city for some time")
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
    print( "A. Run")
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
    else:
        print("\nMaybe you should have picked up the potion!!!")
        print("You have died")

mystery()





