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
print("2: Have you searched the Golden Temple?")
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
            print("You hav chosen to ignore the situation! Innocents have died because of your consequences!!!")
            os._exit(1)
        else:
            print("Please input integers (1 or 2) only! Please try again!")
            bank()
    except:
        print("Please input integers (1 or 2) only! Please try again!")
        bank()


bank()
