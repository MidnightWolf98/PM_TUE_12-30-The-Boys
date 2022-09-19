

#scene 2
print('You chose the purple serum.')
print('You feel like something is happening to your body but could not tell.')
print('The soldiers are coming, there is no time to think!!')

def escape(): #define function called escape
    print('There are two ways to try..')
    print('1 - Break the window next to you and jump.')
    print('2 - Run to rooftop through the stairs.')
    try:
        escape = int(input('Enter 1 or 2:')) #ask user to input an integer
        if escape != 2: #if input is not 2 run the code below
            print('You break the window and look..50 floors above the ground, that is not a great choice to jump.')
            print('Try something else.')
            escape = int(input('Enter 1 or 2:'))#ask user to input an integer
            if escape == 2:
                escape_2()
        else: #if input is 2 run the code below
            print('Sounds great to try.')
            escape_2() #call escape_2 function
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        escape() #call escape function

def escape_2():
    print('You run as fast as you can and reach the rooftop before those soldiers catch you.')
    print('You look around to find anything that can help you.')
    print('There is backpack on the floor.\n "who left this here?" you think.')
    print('1 - Check the backpack on the floor.')
    print('2 - Walk around to see if anything else can help.')
    try:
        escape_2 = int(input('Enter 1 or 2: ')) #ask user to input an integer
        if escape == 1: #if input is 1 run code below
            print('A paraglider!\nYou use it to fly before the soldiers come to you.')
        else:
            print('You found a set of rappel on the edge of the bulding.\nMight be left from some window cleaners.')
            print('You slide down and reach a lower bulding and run away from those soldiers.')
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        escape_2()

escape() #call escape function


#scene 3
print('2 WEEKS LATER')
print('You are very very tired and going to have a nice bath before bed.')
print('You get a phone call from your best friend Will.')

call_time = 0

def phone_call():
    print('1 - Pick up the call')
    print('2 - Hang up the call')
    try:
        call = int(input('Enter 1 or 2: '))
        if call == 1:
            call_1()
        else:
            global call_time
            while call_time < 2:
                call_time = call_time + 1
                call_2()
                if call_time == 2:
                    call_3()
                    break 

    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        phone_call()

def call_1():
    print('You pick up the phone,')
    print('Will: "How are you mate？"\n "There is a party tomorrow nigth, you comming?"')
    print('1 - "Yeah, why not."')
    print('2 - "Let me think about it"')
    print('3 - "Cannot be bother, i wanna stay home."')
    try:
        call_1 = int(input('Enter 1, 2 or 3'))
        if call_1 == 1:
            print('Will: "Cool! See you then!"')
        else:
            print('Will: "Come on"\n"We did not go to any party for a whole month."\n"You must be there tomorrow. See you there mate."')
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        call_1()

def call_2():
    print('You hung up the call.')
    print('2 MINUTES LATER..\nWill call you again.')
    print('He might have something needs to say.')
    phone_call()
    global call_time
    if call_time >= 5:
        call_3()

def call_3():
    print('20 MINUTES LATER..')
    print('"KNOCK KNOCK"\n"Are you there? Open the door."')
    print('It is Will')
    input()
phone_call()
