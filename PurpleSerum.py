import time

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
            escape = int(input('Enter 1 or 2:'))
        else: #if input is 2 run the code below
            print('Sounds great to try.')
            escape_2()
    except:
        print('input invaild!\nEnter 1 or 2 only')
        escape()

def escape_2():
    print('You run as fast as you can and reach the rooftop before those soldiers catch you.')
    print('You look around to find anything that can help you.')
    print('There is backpack on the floor.\n "who left this here?" you think.')
    print('1 - Check the backpack on the floor.')
    print('2 - Walk around to see if anything else can help.')
    try:
        escape_2 = int(input('Enter 1 or 2:')) #ask user to input an integer
        if escape == 1: #if input is 1 run code below
            print('A paraglider!\nYou use it to fly before the soldiers come to you.')
        else:
            print('You found a set of rappel on the edge of the bulding.\nMight be left from some window cleaners.')
            print('You slide down and reach a lower bulding and run away from those soldiers.')
    except:
        print('input invaild!\nEnter 1 or 2 only')
        escape_2()

escape()
