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
