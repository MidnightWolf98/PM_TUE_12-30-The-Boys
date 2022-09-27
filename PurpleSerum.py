
#end game
def end():
    print('- - - - - - - - - ')
    print('Game Over!')
    print('Press any key to exit.')
    end = input()
    exit()


#scene 2
print('You chose the purple serum.')
print('You feel like something is happening to your body but could not tell.')
print('The soldiers are coming, there is no time to think!!')


def escape():
    print('There are two ways to try..')
    print('1 - Break the window next to you and jump.')
    print('2 - Run to rooftop through the stairs.')
    escape_option()


def escape_option(): #define function called escape
    try:
        escape = int(input('Enter 1 or 2:')) #ask user to input an integer
        while escape == 1 or escape == 2: #run code below while input is 1 or 2
            if escape == 1: #while input is not 2 run the code below
                print('You break the window and look..50 floors above the ground, that is not a great choice to jump.')
                print('The soldiers are coming. You jumped.')
                print('You died.')
                end() #call function
            else: #if input is 2 run the code below
                print('Sounds great to try.')
                escape_2() #call escape_2 function
        if escape not in range(1,2): #run code below if input is not in range
            print('input invaild!\nEnter 1 or 2 only')
            escape() #call function
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        escape() #call escape function

def escape_2():
    print('You run as fast as you can and reach the rooftop before those soldiers catch you.')
    print('You look around to find anything that can help you.')
    print('There is backpack on the floor.\n "who left this here?" you think.')
    print('1 - Check the backpack on the floor.')
    print('2 - Walk around to see if anything else can help.')
    escape_2_option()

def escape_2_option():
    try:
        escape_2 = int(input('Enter 1 or 2: ')) #ask user to input an integer
        while escape_2 == 1 or 2:
            if escape == 1: #if input is 1 run code below
                print('A paraglider!\nYou use it to fly before the soldiers come to you.')
            else:
                print('You found a set of rappel on the edge of the bulding.\nMight be left from some window cleaners.')
                print('You slide down and reach a lower bulding and run away from those soldiers.')
                break
        if escape_2 not in range(1,2):
            escape_2()
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        escape_2()

escape() #call function

#scene 3
print('- - - - - - - - - ')
print('2 WEEKS LATER')
print('You come home after work very very tired and going to have a nice bath before bed.')
print('You get a phone call from your best friend Will.')

call_time = 0 #global variable called call_time

def phone_call():
    print('1 - Pick up the call')
    print('2 - Hang up the call')
    phone_call_option()

def phone_call_option():
    try:
        call = int(input('Enter 1 or 2: ')) #ask user to input an integer
        if call == 1: #run code below if input is 1
            print('You pick up the phone,')
            call_1()
        if call == 2: #run code below if input is not 1
            global call_time #get value of global variable  call_time
            while call_time < 2: #run code below while call_time smaller than 2
                call_time = call_time + 1 #add 1 to call_time
                call_2() #call function call_2
                if call_time == 2: #run code below if call_time equal to 2
                    call_3() #call function call_3
                    break #exit while loop

    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        call_1()

def call_1():
    print('Will: "How are you mate？"\n "There is a party tomorrow nigth, you comming?"')
    print('1 - "Yeah, why not."')
    print('2 - "Let me think about it"')
    print('3 - "Cannot be bother, i wanna stay home."')
    call_1_option()

def call_1_option():
    try:
        call_1 = int(input('Enter 1, 2 or 3')) #ask user to input an integer
        while call_1 == 1 or 2 or 3:
            if call_1 == 1: #run code below if input is 1
                print('Will: "Cool! See you then!"')
            if call == 2 or 3: #run code below when input is not 1
                print('Will: "Come on"\n"We did not go to any party for a whole month."\n"You must be there tomorrow. See you there mate."')
        if call_1 not in range(1,3):
            print('input invaild!\nEnter 1, 2or 3 only')
            call_1()
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        call_1()


def call_2():
    print('You hung up the call.')
    print('2 MINUTES LATER..\nWill call you again.')
    print('He might have something needs to say.')
    phone_call()
    global call_time #get value of global variable call_time
    if call_time >= 5: #run code below if call_time equal to 5
        call_3()

def call_3():
    print('20 MINUTES LATER..')
    print('"KNOCK KNOCK"\n"Are you there? Open the door."')
    print('It is Will\nYou opend the door and let him in.')
    print('Will: "What were you doing? I was worrying so I came."')
    call_1() #call function call_1

phone_call() #call phone_call function


#scene 4
print('- - - - - - - - - ')
print('NEXT DAY 7PM')
print('RAINNING')

def travel():
    print('How do you want to travel to the party place?')
    print('1 - Walk(30 mins)')
    print('2 - Taxi(5 mins)')
    #travel()

#def travel_opiton():

    #try:
        #travel = int(input('Enter 1 or 2:'))
        #if travel == 1:



input()
