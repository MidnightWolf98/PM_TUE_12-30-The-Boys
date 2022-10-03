
#end game
def end(): #define end function
    #print statements
    print('- - - - - - - - - ')
    print('Game Over!')
    print('Press any key to exit.')

    end = input() #ask input to confirm exit
    exit() #exit program


#scene 2

#print statements
print('You chose the purple serum.')
print('You feel like something is happening to your body but could not tell.')
print('The soldiers are coming, there is no time to think!!')


def escape(): #define escape function
    #print statements
    print('- - - - - - - - - ')
    print('There are two ways to try..')
    print('1 - Break the window next to you and jump.')
    print('2 - Run to rooftop through the stairs.')
    print('What will you do?')
    escape_option() #call escape_option function


def escape_option(): #define escape_option function
    try:
        escape = int(input('Enter 1 or 2:')) #ask user to input an integer
        while escape != 2: #run code below while input is 1 or 2
            if escape == 1: #call end function if input is 1
                print('>>>')
                print('You break the window and look..50 floors above the ground, that is not a great choice to jump.')
                print('The soldiers are coming. You jumped.')
                print('You died.')
                end() #call function

            print('Input invaild! Enter 1 or 2 only1')
            escape = int(input('Enter 1 or 2:')) #ask user to input an integer

        if escape == 2: #if input is 2 run the code below
            print('>>>')
            print('Sounds great to try.')
            escape_2() #call escape_2 function\

    except: #recall function if input is invaild
        print('Input invaild! Enter 1 or 2 only2')
        escape() #call escape function

def escape_2(): #define escape_2 function
    #print statements
    print('- - - - - - - - - ')
    print('You run as fast as you can and reach the rooftop before those soldiers catch you.')
    print('You look around to find anything that can help you.')
    print('There is backpack on the floor.\n "who left this here?" you think.')
    print('- - - - - - - - - ')
    print('What will you do?')
    print('1 - Check the backpack on the floor.')
    print('2 - Walk around to see if anything else can help.')
    escape_2_option() #call escape_2_option function

def escape_2_option(): #define escape_2_option function
    try:
        escape_2 = int(input('Enter 1 or 2: ')) #ask user to input an integer
        if escape_2 in range(1,3): #run code below while input is 1 or 2
            if escape_2 == 1: #if input is 1 run code below
                print('>>>')
                print('A paraglider!\nYou use it to fly before the soldiers come to you.')
            elif escape_2 == 2: #if input is 2 run code below
                print('>>>')
                print('You found a set of rappel on the edge of the bulding.\nMight be left from some window cleaners.')
                print('You slide down and reach a lower bulding and run away from those soldiers.')
        else: #run code below if input is not in range
            print('Input invaild! Enter 1 or 2 only3')
            escape_2_option() #call escape_2_option function
    except: #recall function if input is invaild
        print('Input invaild! Enter 1 or 2 only4')
        escape_2()

escape() #call function

#scene 3
#print statements
print('- - - - - - - - - ')
print('2 WEEKS LATER')
print('- - - - - - - - - ')

print('You come home after work very very tired and going to have a nice bath before bed.')
print('You get a phone call from your best friend Will. (NEW CHARACTER - WILL)')

call_time = 0 #create a global variable called call_time

def phone_call(): #define phone_call function
    #print statements
    print('- - - - - - - - - ')
    print('What will you do?')
    print('1 - Pick up the call')
    print('2 - Hang up the call')
    phone_call_option() # call phone_call_option function

def phone_call_option(): #define phone_call_option function
    try:
        call = int(input('Enter 1 or 2: ')) #ask user to input an integer
        if call == 1: #call call_1 function if input is 1
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
        if call not in range(1,2): #run code below if input is not in range
            print('Input invaild! Enter 1 or 2 only')
            phone_call_option()
    except: #recall function if input is invaild
        print('Input invaild! Enter 1 or 2 only')
        call_1()

def call_1(): #define call_1 function
    #print statements
    print('Will: "How are you mate？"\n "There is a party tomorrow nigth, you comming?"')
    print('- - - - - - - - - ')
    print('What are you going to say?')
    print('1 - "Yeah, why not."')
    print('2 - "Let me think about it"')
    print('3 - "Cannot be bother, i wanna stay home."')
    call_1_option() #call call_1_option function

def call_1_option(): #define call_1_option function
    try:
        call_1 = int(input('Enter 1, 2 or 3')) #ask user to input an integer
        while call_1 == 1 or 2 or 3: #run code below if input is 1,2 or3
            if call_1 == 1: #run code below if input is 1
                print('Will: "Cool! See you then!"')
            if call == 2 or 3: #run code below when input is not 1
                print('Will: "Come on"\n"We did not go to any party for a whole month."\n"You must be there tomorrow. See you there mate."')
        if call_1 not in range(1,3): #run code below if input is not in range
            print('Input invaild! Enter 1, 2or 3 only')
            call_1()
    except: #recall function if input is invaild
        print('input invaild!\nEnter 1 or 2 only')
        call_1()


def call_2(): #define call_2 function
    #print statements
    print('You hung up the call.')
    print('2 MINUTES LATER..\nWill call you again.')
    print('He might have something needs to say.')
    phone_call() #call phone_call function
    global call_time #get value of global variable call_time
    if call_time >= 5: #run code below if call_time equal to 5
        call_3() #call call_3 function

def call_3(): #define call_3 function
    #print statments
    print('20 MINUTES LATER..')
    print('"KNOCK KNOCK"\n"Are you there? Open the door."')
    print('It is Will\nYou opend the door and let him in.')
    print('Will: "What were you doing? I was worrying so I came."')
    call_1() #call function call_1

phone_call() #call phone_call function


#scene 4

#print statements
print('- - - - - - - - - ')
print('NEXT DAY 7PM')
print('RAINNING')

def travel(): #define travel funtion
    #print statements
    print('How do you want to travel to the party place?')
    print('1 - Walk(30 mins)')
    print('2 - Bus(15 mins)')
    print('3 - Taxi(5 mins)')
    travel_option() #call travel_option function

def travel_option(): #define travel_option function
    try:
        travel = int(input('Enter 1 or 2:')) #ask user to input an integer
        while travel == 1 or 2 or 3: #run code below while input is 1, 2 or 3
            if travel == 1: #run code below if input is 1
                print('You decide to walk.')
                travel_1()
            elif travel == 2: #try this if input is not 1
                print('You decide to take the bus.')
                travel_2()
            else: #run code below if input is not 1 or 2
                print('You decide to call a taxi.')
                travel_3()
        if travel not in range(1,3): #run code below if input not in range
            print('Input invalid! Enter 1, 2 or 3 only.')
            travel_option()
    except: #recall function if input is invaild
        print('input invaild!\nEnter integer only')
        travel()

def travel_1():
    #print statements
    print('>>>')
    print('WALKING ON THE STREET TO THE PARTY...')
    print('Suddenly, you see a shadow appear not far ahead.')
    print('You feel like he is looking at you, and he disappear in the alley.')
    print('- - - - - - - - - ')
    print('What will you do?')
    print('1. Follow the shadow.')
    print('2. Ignore it and keep going.')
    travel_1_option() #call travel_1_option function

def travel_1_option():
    try:
        travel_1 = int(input('Enter 1 or 2:')) #ask user to input an integer
        while travel_1 in range(1,3): # run code below if input in range
            if travel_1 == 1: #run code below if input is 1
                print('You walk into the alley after him.')
                break #exit while loop
            else: #run code below if input is not 1
                print('You continue walking.')
                break #exit while loop
        if travel_1 not in range(1,3): #run code below if input is not in range
            print('Input invalid! Enter 1 or 2 only.')
            travel_1_option()
    except:
        except: #recall function if input is invaild
            print('input invaild!\nEnter integer only')
            travel_1()

def travel_2():
    #print statements
    print('>>>')
    print('ON THE BUS...')
    print('You see a girl who looks familiar sitting next to the window, you walk up and sit next to her.')
    print('She turn around and regonise you. She is going to the party as well. (NEW CHARACTER - HAYLEY)')

    print('CHATTING WITH HAYLEY..')
    print('"There is a car accident ahead, if you are hurry, walk to the bus stop next street please." from the bus driver.')
    print('"Should we walk?" Hayley ask you.')
    print('- - - - - - - - - ')
    print('What will you say?')
    print('1. "Yeah sure."')
    print('2. "I might just wait on the bus."')
    travel_2_option() #call travel_2_option function

def travel_2_option():
    try:
        travel_2 = int(input('Enter 1 or 2:')) #ask user to input an integer
        while travel_2 in range(1,3): #run code below if input is in range
            while travel_2 != 1: #run code below if input is not 1
                print('"We will be late for the party."says Hayley.')
                travel_2_option()
                break #exit while loop
            if travel_2 == 1: #run code below if input is 1
                print('You get off the bus and walk with Hayley.')
        if travel_2 not in range(1,3): #run code below if input is not in range
            print('Input invalid! Enter 1 or 2 only.')
            travel_2_option()
    except:
        except: #recall function if input is invaild
            print('input invaild!\nEnter 1 or 2 only')
            travel_2()

def travel_3():
    #print statements
    print('>>>')
    print('ON THE TAXI...')
    print('The taxi driver did not sleep well last night. When the traffic light turns red, he did not stop.')
    print('A truck comes from the side with a high speed, hits the taxi.')
    print('You died.')
    end() #call end function



#scene 5











input()
