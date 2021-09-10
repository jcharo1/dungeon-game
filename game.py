import random
import time

with open('Dungeon-of-pain.txt') as f :
    castle_txt= f.read()


yes_or_no = ["yes", "no"]

doors = ['iron', 'blue', 'red', 'green']

red_room_options = ['exit']
blue_room_options = ['exit', 'search']
iron_room_options = ['exit', 'search']
green_room_options = ['exit', 'talk']
character_name = ''

# for testing
character_starting_items = ['bubbleGum', 'lint', 'mixtape']

# utility functions #################


def pocketItems():
    pretty_items = ''
    for item in character_starting_items:
        if item == 'mixtape':
            item = character_name + "'s " + item
        pretty_items = pretty_items + "\n" + '-' + item

    print(pretty_items)


def delayedp(text, sec=1):
    print(text)
    time.sleep(sec)


def steal():
    taken_item = random.choice(character_starting_items)
    delayedp('The goblin takes yo ' + taken_item)
    character_starting_items.remove(taken_item)


def goblin_roll():
    global character_name
    delayedp('Listen here newbie!', 1)
    delayedp('Time is money guy!', 1)
    delayedp(
        'Lets throw some bones my friend, Highest roller wins big ' +
        'shot!!!', 2)
    delayedp('Are you willing to risk it all?', 1)
    delayedp('Items you have in pocket:', 1)
    pocketItems()

    response = ''
    while response not in yes_or_no:
        response = input('type: yes or no\n')
        if response == "yes":
            you = random.randint(1, 6)
            goblin = random.randint(1, 6)
            delayedp('** You rolled a ' + str(you) + '**')
            delayedp('** Goblin rolled a ' + str(goblin) + '**')

            if you > goblin:
                delayedp(
                    'You won!\n The goblin hands over a Shield of '
                    + 'Reflection'
                )
                title = ' The Gambler'
                character_name = character_name + title
                delayedp('[ACHIEVEMENT] ' + character_name)
                character_starting_items.append('Shield of Reflection')

            elif goblin > you:
                # you lose
                delayedp('you lost the goblin laughs')
                steal()

            else:
                delayedp('wow its a tie!')

            goblin_roll()

        elif response == "no":
            green_door()
        else:
            delayedp('I didnt understand! You speak newb?')


def intro():
    global character_name
    delayedp('You wake up in a courtyard...')
    delayedp('You cant remember anything...')

    delayedp('Do you remember you name?')
    character_name = input("Please enter your name\n")

    delayedp('You check your pockets you find: ')
    pocketItems()
    courtyard()


def courtyard():
    delayedp("Greetings, " + character_name + "! If thats even your name...")

    delayedp("You look around the courtyard where to go... where to go....")

    # where do you want to go
    response = ""
    while response not in doors:
        response = input(
            "choose a door: red, blue, green or iron\n")
        if response == "iron":
            iron_door()
        elif response == "blue":
            blue_door()
        elif response == "red":
            red_door()
        elif response == "green":
            green_door()
        else:
            delayedp("That is not an option. Please try again...\n")


def play_game():
    delayedp(castle_txt)
    delayedp('Welcome to the dungeon of pain!')
    delayedp('Would you like to play a game?!')
    response = ""
    while response not in yes_or_no:
        response = input("type yes or no\n")
        if response == "yes":
            intro()
        elif response == "no":
            play_game()
        else:
            delayedp("I did not understand\n")


def iron_door():
    delayedp('\n')
    delayedp('You\'re in the iron room')
    delayedp(
        'You look around.... It seems to be bigger than all the previous '
        + 'rooms.. ')
    delayedp('The smell of musk hits you like a sack of potatoes')
    delayedp('You walk down the hall...')
    delayedp('The room opens up to a collisium')
    delayedp('A gate begins to rise')
    delayedp(
        'you see a fog of breath slowly emerging from the shadows beyond '
        + 'the gate...')
    delayedp('In the distance you see 2 bright lights...')
    delayedp(
        'As the beast walks forward you relize the bright light are '
        + 'in fact his eyes piercing through your soul')
    delayedp('he takes a step forward...')
    delayedp('The beast says welcome ' + character_name +
             ' I\'ve heard so much about you I\'m here to take your soul')
    delayedp('\n')

    delayedp('Takes a deep breadth..')

    hasSword = 'The Sword of the Gods' in character_starting_items
    hasShield = 'Shield of Reflection' in character_starting_items

    if hasShield:
        delayedp(
            'You pick up your shield to block. The beast blows fire '
            + 'and your shield of reflection beams the fire back at the beast '
            + 'injuring it!')
    else:
        delayedp(
            'You pick up your hands to block your face. The fire consumes '
            + 'you and you die')
        delayedp('GAME OVER!')
        play_game()

    if hasSword:
        delayedp(
            'The beast is blind.... now is the time to attack .... ' +
            'you pick up the Sword of the Gods and slay the beast!')
        delayedp('You are now the ' + character_name + ' The Great')
        # play_game()
    else:
        delayedp('you try and punch the beast but the beast is unfazed')
        delayedp('The Beast laughs in enjoyment and rips ya arm off ')
        delayedp('GAME OVER!')
        play_game()

    play_game()
    # response = ""
    # while response not in yes_or_no:
    #     response = input("type yes or no\n")


def blue_door():
    delayedp('you have now entered the blue room')
    response = ""
    while response not in blue_room_options:
        response = input("choose exit or search\n")
        if response == 'search':
            delayedp(
                'You begin to search and see a large ' +
                'Sword in the corner of the room')
            character_starting_items.append("The Sword of the Gods")
            delayedp('** [RECIEVED] The Sword of the Gods **')
            delayedp(
                'This Ancient Sword has slain many kings and will serve '
                + 'you well in the Iron dungeon')
            courtyard()
        elif response == 'exit':
            delayedp('you exit the room')
            courtyard()
        else:
            delayedp('You only have 2 options, your not very bright ehh?')


def red_door():
    delayedp('you have now entered the red room', 1)
    delayedp(
        'the floor drops from under you and you are forever falling in a '
        + 'pit nothingness', 3)
    delayedp('GAME OVER ' + character_name + '!!!', 3)
    play_game()


def green_door():
    delayedp('you have now entered the green room ' + character_name)
    delayedp('You look around the room you see a goblin..')
    delayedp('Do you talk to the goblin or exit the room')
    response = ""
    while response not in green_room_options:
        response = input("choose: exit or talk\n")
        if response == 'talk':
            goblin_roll()
        elif response == 'exit':
            delayedp('you exit the room')
            courtyard()
        else:
            delayedp('What?')


play_game()
