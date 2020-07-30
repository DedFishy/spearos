devmode = False
#Top
import time, colorama, os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()
colorama.init()
if devmode == False:
    print(colorama.Fore.RED + colorama.Back.WHITE + r'''
████████████████████████████████████████
██████████               ███████████████
█████████████    ███████   █████████████
███████████████    ██████   ████████████
█████████████████   ███████ ████████████
██████████████████   ███████████████████
██████████████████   ██████ ████████████
█████████████████    █████   ███████████
██████████████     █████    ████████████
██████████               ███████████████
████████████████████████████████████████
            B GAME STUDIOS              ''' + colorama.Style.RESET_ALL)
    time.sleep(1)
    clear()
    print(colorama.Back.BLUE + colorama.Fore.CYAN + '''
██████████████████████
█            █████████
█          ███████████
█        █████████████
█          ███████████
█    ██      █████████
█  ██████      ███████
███████████      █████
█████████████      ███
███████████████      █
█████████████████    █
██████████████████████
█SPEAR█-█-█-█-█-█-█-██
█OS   -█-█-█-█-█-█-█-█
█TEAM █-█-█-█-█-█-█-██
██████████████████████
██████████████████████
''' + colorama.Style.RESET_ALL)
    time.sleep(1)
    clear()
    print(colorama.Fore.WHITE, colorama.Back.CYAN)
    print(r'     _____                          ____   _____ ')
    time.sleep(0.2)
    print(r'    / ____|                        / __ \ / ____|')
    time.sleep(0.2)
    print(r'   | (___  _ __   ___  __ _ _ __  | |  | | (___  ')
    time.sleep(0.2)
    print(r'    \___ \|  _ \ / _ \/ _  |  __| | |  | |\___ \ ')
    time.sleep(0.2)
    print(r'    ____) | |_) |  __| (_| | |    | |__| |____) |')
    time.sleep(0.2)
    print(r'   |_____/|  __/ \___|\____|_|     \____/|_____/ ')
    time.sleep(0.2)
    print(r'          | |                                    ')
    time.sleep(0.2)
    print(r'          |_|     _________________              ')
    time.sleep(0.2)
    print(r'                 |POWERED BY PYTHON|             ')
    time.sleep(0.2)
    print(r'                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾              ')
    time.sleep(0.5)
    print(colorama.Back.BLUE + 'Version 2.0' + colorama.Back.CYAN + '                                      ')
    time.sleep(1)
print(colorama.Back.GREEN + 'Setting up Spear OS...                           ' + colorama.Style.RESET_ALL)
print('[Importing libraries]')
try:
    import socket, datetime, sys, random, requests, pyfiglet, keyboard, urllib
except Exception as e:
    print('It looks like you are missing some libraries.', e + '.')
    time.sleep(1)
    os.system('pip install keyboard')
    os.system('pip install pyfiglet')
    os.system('pip install requests')
    print('We tried to install the required libraries. Now restarting...')
    time.sleep(2)
print(colorama.Fore.GREEN + '[Done]' + colorama.Style.RESET_ALL)
print('[Defining functions and variables]')
tips = ['Spear OS is now being developed in either Repl.it or Spyder!', 'Check our website at www.spearos.tk for new updates!', 'Use the arrow keys to navigate menus.', 'You can help develop Spear OS by emailing bgamestudios@mail.com with a request to join the team.', 'Spear OS is developed by B Game Studios (not a fitting name).', 'Visit the Spear OS website at www.spearos.tk for downloads and stuff.', 'The calculator supports basic equations so you can MATH IT or something.', 'You can turn on Dev mode in the settings to disable startup animations and make other changes.', 'There are power options in settings, such as "Reboot" and "Shut Down".', 'Try out some of the games in the "Games" section of the home menu!', 'XDecoder can be used to encode and decode messages.', 'You can download and use other apps using the "Download App" and "Load App" optons from the home menu!', 'You can edit the source code of Spear OS to fit your style!', '"Faceify" makes random text art faces!']
nouns = ['Apple', 'Computer', 'Bottle', 'Book', 'Animal', 'Peanut', 'Table', 'Curtain', 'Outlet', 'Blanket', 'Wall', 'Human', 'Cliff', 'Water', 'Candy', 'Arrow', 'Mouse', 'Light', 'Blindfold', 'Speaker', 'Llama', 'Shield', 'Wire', 'Movie', 'Receipt', 'Fist', 'Switch', 'Company', 'Ledge', 'Hair']
adjs = ['Silly', 'Evil', 'Red', 'Bright', 'Sharp', 'Edible', 'Short', 'Dangerous', 'Large', 'Furry', 'Mean', 'Tall', 'Transparent', 'Tasty', 'Annoying', 'Long', 'Horrible', 'Cool', 'Hot', 'Shady', 'Barbarous', 'Stupid', 'Round', 'Solid', 'Messy', 'Fussy', 'Flying', 'Broken', 'Weird', 'Dying']
def nouny():
    print('=_-Nouny-_=')
    input('Press enter to generate something.')
    clear()
    time.sleep(random.randint(1, 4))
    print(random.choice(adjs), random.choice(nouns))
    input('Press enter to exit')
def faceify():
    print('Faceify!')
    input('Press enter to start')
    clear()
    print('Randomizing you a sweet face...')
    hair = random.choice(['//////', '``````', '""""""', '______', '||||||'])
    eyes = random.choice(['|o\/o|', '|/oo\|', '| o-o|', '|[][]|', '| `` |'])
    mouth = random.choice(['|  O |', '|  / |', '|  * |', '|  > |', '|  ~ |'])
    time.sleep(random.randint(1, 4))
    print('Done!')
    input('Press enter to see the face!')
    clear()
    time.sleep(1)
    print(hair)
    time.sleep(1)
    print(eyes)
    time.sleep(1)
    print(mouth)
    time.sleep(1)
    print('\____/')
    time.sleep(1)
    input('Press enter to continue')
def figlet():
    print('Enter the text:')
    txt = input('>')
    f = pyfiglet.Figlet(font='standard')
    print(f.renderText(txt))
    input('Press Enter to exit')
#Beginning of menu defining
menuoptions = []
menuopt_return = ''
menucur_option = 0
menuout_i = 0
menuselected = 0
menuname = ''
menurunning = False
def menudec_option(args):
    global menucur_option, menuoptions, menuout_i, menurunning
    if menurunning == True:
        if not menucur_option == len(menuoptions) - 1:
            menucur_option += 1
        else:
            menucur_option = 0
        menureload()
def menuinc_option(args):
    global menucur_option, menuoptions, menuout_i, menurunning
    if menurunning == True:
        if not menucur_option == 0:
            menucur_option -= 1
        else:
            menucur_option = len(menuoptions) - 1
        menureload()
def menureload():
    ptime = datetime.datetime.now()
    curhour = ptime.hour
    if ptime.hour > 11:
        aorp = "PM"
        curhour -= 12
    else:
        aorp = "AM"
        curhour = 12
    curmin = ptime.minute
    minlen = len(str(curmin))
    if minlen < 2:
        minute = '0' + str(curmin)
    else:
        minute = str(ptime.minute)
    if curhour == 0:
        curhour = 12
    clear()
    if menuname == 'home':
        #Home menu title
        print(str(curhour) + ":" + minute, aorp + colorama.Fore.RED + ' ' + str(ptime.month) + "/" + str(ptime.day) + "/" + str(ptime.year), colorama.Fore.BLUE + colorama.Style.RESET_ALL) 
        print(colorama.Fore.GREEN + 'Dev mode is', str(devmode)) 
        if os.name == 'nt':
            hostname = 'Windows'
        elif os.name == 'posix':
            hostname == 'Linux/Mac OS'
        else:
            hostname = 'unknown'
        try:
            urllib.request.urlopen('http://google.com')
            print('You are connected to the internet')
        except:
            print('You are not connected to the internet')
        print('The host OS is "' + os.name + '", which is', hostname + colorama.Style.RESET_ALL)
        print('_______________' + colorama.Fore.CYAN)
        print(' SPEAR OS HOME' + colorama.Style.RESET_ALL)
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    else:
        print(colorama.Fore.GREEN + menuname + colorama.Style.RESET_ALL)
    global menuout_i, menuselected, menucur_option
    if menucur_option > len(menuoptions):
        menucur_option = 0
    for menuout_i in range(0, len(menuoptions)):
        if menuout_i == menucur_option:
            print(colorama.Fore.BLUE, menuoptions[menuout_i], colorama.Style.RESET_ALL)
            menuselected = menuout_i
        else:
            print(menuoptions[menuout_i])
def showmenu():
    global menuout_i, menurunning, menucur_option
    menurunning = True
    menucur_option = 0
    menureload()
    keyboard.wait('enter')
    menurunning = False
    input()
    return menuoptions[menuselected]
    clear()
keyboard.on_press_key('down', menudec_option)
keyboard.on_press_key('up', menuinc_option)
#End of menu defining
def games():
    global menuoptions, menuname
    menuname = 'Games'
    menuoptions = ['Rock, Paper, Scissors', 'ASCII Art', 'Roll It!', 'SAFARI' , 'Storytime', 'Faceify', 'Nouny', 'Back']
    inp = showmenu()
    clear()
    if inp == 'Rock, Paper, Scissors':
        rps()
    elif inp == 'ASCII Art':
        figlet()
    elif inp == 'Roll It!':
        print('Rolling the die...')
        roll = random.randint(1, 6)
        time.sleep(random.randint(2, 8))
        print('You rolled a', str(roll))
        time.sleep(2)
    elif inp == 'SAFARI':
        safari()
    elif inp == 'Storytime':
        storytime()
    elif inp == 'Faceify':
        faceify()
    elif inp == 'Nouny':
        nouny()
    elif inp == 'Back':
        pass
def settings():
    global menuname, menuoptions
    menuname = 'Settings'
    menuoptions = ['Dev mode', 'Power', 'Back']
    inp = showmenu()
    if inp == 'Dev mode':
        sdm()
    elif inp == 'Power':
        menuname = 'Power Options'
        menuoptions = ['Shut down', 'Restart', 'Suspend', 'Back']
        inp = showmenu()
        if inp == 'Shut down':
            sys.exit()
        elif inp == 'Restart':
            os.execl(sys.executable, sys.executable, * sys.argv)
        elif inp == 'Suspend':
            print('Suspending, press enter to wake')
            time.sleep(2)
            clear()
            input()
        elif inp == 'Back':
            pass
    elif inp == 'Back':
        pass
def cmd():
    try:
        print("Host Command Line")
        print("Use 'hcl-info' for info")
        print("Use 'hcl-exit' to return to Home")

        def maincmd():
            while True:
                cmd = input(socket.gethostname() + ":" + os.getcwd() + ">")
                if cmd == "hcl-info":
                    print(
                        "PyCMD is an attempt at a command line written completely in Python."
                    )
                elif cmd == "hcl-exit":
                    break
                else:
                    os.system(cmd)
                if "cd " in cmd:
                    cmd = cmd.replace("cd ", "")
                    os.chdir(cmd)

        maincmd()
    except FileNotFoundError:
        print("The system cannot find the file specified")
        maincmd()
def rps():
    global menuname, menuoptions
    computerchoice = random.randint(1, 3)
    menuname = 'What do you choose?'
    menuoptions = ['Rock', 'Paper', 'Scissors']
    yourchoicemenu = showmenu()
    yourchoice = ''
    if yourchoicemenu == 'Rock':
        yourchoice = '1'
    elif yourchoicemenu == 'Paper':
        yourchoice = '2'
    elif yourchoicemenu == 'Scissors':
        yourchoice = '3'
    else:
        print('An error occurred with the RPS engine...')
        print(yourchoice)
    if yourchoice == '1' and computerchoice == 3:
        print('You chose rock')
        print('Computer chose scissors')
        print('You win!')

    elif yourchoice == '2' and computerchoice == 1:
        print('You chose paper')
        print('Computer chose rock')
        print('You win!')

    elif yourchoice == '3' and computerchoice == 2:
        print('You chose scissors')
        print('Computer chose paper')
        print('You win!')

    elif yourchoice == '1' and computerchoice == 2:
        print('You chose rock')
        print('Computer chose paper')
        print('You lose!')

    elif yourchoice == '2' and computerchoice == 3:
        print('You chose paper')
        print('Computer chose scissors')
        print('You lose!')

    elif yourchoice == '3' and computerchoice == 1:
        print('You chose scissors')
        print('Computer chose rock')
        print('You lose!')

    elif yourchoice == '1' and computerchoice == 1:
        print('You chose rock')
        print('Computer chose rock')
        print('You tied!')

    elif yourchoice == '2' and computerchoice == 2:
        print('You chose paper')
        print('Computer chose paper')
        print('You tied!')

    elif yourchoice == '3' and computerchoice == 3:
        print('You chose scissors')
        print('Computer chose scissors')
        print('You tied!')

    else:
        print("That's not a choice.")
        print(yourchoice, str(computerchoice))
    time.sleep(3)

def storytime():
    print('Welcome to...')
    print('Story Time!')
    print('Name...')
    w1 = input('An adjective>')
    w2 = input('An adjective (capitalized)>')
    w3 = input('A plural noun>')
    w4 = input('A noun>')
    w5 = input('A noun>')
    w6 = input('A game>')
    w7 = input('A noun>')
    w8 = input('A verb ending in "ing">')
    w9 = input('A verb ending in "ing">')
    w10 = input('A plural noun>')
    w11 = input('A verb>')
    w12 = input('A plural noun>')
    w13 = input('A plant>')
    w14 = input('A part of the body>')
    w15 = input('A place>')
    w16 = input('A verb>')
    w17 = input('An adjective>')
    w18 = input('A number>')
    w19 = input('A plural noun>')
    clear()
    print('<Vacations>')
    print('')
    print('Do you like ' + w1 + ' food?')
    print('Then youll love ' + w2 + ' Snacks! They are good for your')
    print('health and they taste like ' + w3 + ' mixed with a ' + w4 + '.')
    print('They make you feel like you can fly as high as a(n) ' + w5)
    print('or beat your friends playing ' + w6)
    print('or shoot and kill a(n) ' + w7 + '. I like')
    print(w8 + ' or ' + w9 + ' them as I eat them.')
    print('When parents look at the ingredient label,')
    print('they eat three ' + w10 +
            ' of them, screaming, "THEYRE HEALTHY!"')
    print('Then they ' + w11 + '. Last summer, my little brother')
    print('ate one too many and puked a bunch of ' + w12 +
            ' and fell onto a ' + w13 + ' and got pricky needles')
    print('in his ' + w14 + '. My family is going to (the)')
    print(w15 + ', and I will ' + w16 + ' a lot of these snacks there.')
    print('Parents really like these snacks because they are')
    print(w17 + ' and because they have have to work ' + w18)
    print('hour(s) every day all year making enough ' + w19 + ' to pay')
    print('for the snacks. Theyre expensive!.')
    input('Press Enter to exit')
    clear()

def pycmd():
    try:
        print("Python Shell")
        print("Type 'exit' to quit")

        def mainpycmd():
            while True:
                command = input(">>>")
                if command == 'exit':
                    break
                else:
                    exec(command)

        mainpycmd()

    except Exception as e:
        print(
            "An error occurred in your code and the Python Shell will shut down to prevent crashing in 3 seconds. The error:"
        )
        print(e)
        time.sleep(3)
        main()
def xdecoder():
    global menuname, menuoptions
    print("=XDECODER=")
    print("Spear OS Edition")
    time.sleep(2)
    while True:
        menuname = 'What do you want to do?'
        menuoptions = ['Encode', 'Decode']
        operation = showmenu()
        if operation == "Encode":
            txt = input("Enter the text to encode >>>")
            txt = txt.lower()
            txt = txt.replace("|", "")
            txt = txt.replace("a", "|836|")
            txt = txt.replace("b", "|713|")
            txt = txt.replace("c", "|595|")
            txt = txt.replace("d", "|813|")
            txt = txt.replace("e", "|702|")
            txt = txt.replace("f", "|204|")
            txt = txt.replace("g", "|921|")
            txt = txt.replace("h", "|053|")
            txt = txt.replace("i", "|913|")
            txt = txt.replace("j", "|671|")
            txt = txt.replace("k", "|235|")
            txt = txt.replace("l", "|578|")
            txt = txt.replace("m", "|572|")
            txt = txt.replace("n", "|203|")
            txt = txt.replace("o", "|357|")
            txt = txt.replace("p", "|153|")
            txt = txt.replace("q", "|079|")
            txt = txt.replace("r", "|122|")
            txt = txt.replace("s", "|019|")
            txt = txt.replace("t", "|325|")
            txt = txt.replace("u", "|121|")
            txt = txt.replace("v", "|091|")
            txt = txt.replace("w", "|268|")
            txt = txt.replace("x", "|273|")
            txt = txt.replace("y", "|937|")
            txt = txt.replace("z", "|219|")
            print("Here's your encoded text:", txt)
        elif operation == "Decode":
            txt = input("Enter the text to decode >>>")
            txt = txt.lower()
            txt = txt.replace("|836|", "a")
            txt = txt.replace("|713|", "b")
            txt = txt.replace("|595|", "c")
            txt = txt.replace("|813|", "d")
            txt = txt.replace("|702|", "e")
            txt = txt.replace("|204|", "f")
            txt = txt.replace("|921|", "g")
            txt = txt.replace("|053|", "h")
            txt = txt.replace("|913|", "i")
            txt = txt.replace("|671|", "j")
            txt = txt.replace("|235|", "k")
            txt = txt.replace("|578|", "l")
            txt = txt.replace("|572|", "m")
            txt = txt.replace("|203|", "n")
            txt = txt.replace("|357|", "o")
            txt = txt.replace("|153|", "p")
            txt = txt.replace("|079|", "q")
            txt = txt.replace("|122|", "r")
            txt = txt.replace("|019|", "s")
            txt = txt.replace("|325|", "t")
            txt = txt.replace("|121|", "u")
            txt = txt.replace("|091|", "v")
            txt = txt.replace("|268|", "w")
            txt = txt.replace("|273|", "x")
            txt = txt.replace("|937|", "y")
            txt = txt.replace("|219|", "z")
            print("Here's your decoded text:", txt)
        input('Press enter to continue')
        menuname = 'Go again?'
        menuoptions = ['Yes', 'No']
        again = showmenu()
        if again == "No":
            break

def safari():
    import time
    time.sleep(1)
    clear()
    print('S.A.F.A.R.I. 5')
    print("*Some elements may be adapted to work in Spear OS*")
    print(
        'Enter "1" before pressing Enter to get info. Enter "2" before pressing Enter for update information.'
    )
    time.sleep(2)
    start = input('Press ENTER when ready to start!')
    clear()
    time.sleep(1)
    if '1' in start:
        print('This is a text-based Choose')
        print('Your Own Adventure game where')
        print('you have to make decisions based')
        print('on the situation. When you get a')
        print('y/n question, make your answer')
        print('LOWERCASE. When you enter an answer,')
        print('press Enter to verify it.')
        print('Versions 1, 2, 3, and 4 were made in Thonny Python IDE.')
        print('Version 5')
        print('DO NOT press Enter in an option without typing anything.')
        input('Press Enter to play!')
        clear()
    elif '2' in start:
        print(
            'This update fixes spelling issues that were present in version 4'
        )
        input('Press Enter when ready to start!')
        clear()
    print('---------------------------------')
    print('You are walking through the African plain.')
    print('You have been hired by S.A.F.A.R.I. to')
    print('find a rare species of hippo that has been discovered by')
    print('African sciecntists. They have an unmistakable red stripe and')
    print(
        'are going extinct. Your job is to find a male and female to take')
    print('them to the S.A.F.A.R.I. zoo so they can repopulate.')
    print('You have two people with you. Carter, the technician, and')
    print(
        'Amanda, the beauty expert that doesnt know much about anything.')
    print('You are wandering when you see a lion!')
    print(
        'Amanda says you should back away slowly, because thats what you do with'
    )
    print('bears, but Carter has already ran off. What do you do?')
    print('1 for back away, 2 for run away.')
    choice1 = input('>')
    clear()
    choice1 = int(choice1)
    if choice1 == 1:
        print('NO! The lion notices you, and pursues you!.')
        print('You try to run, but he catches you and eats you')
        print('alive.')
        print('GAME OVER')
        time.sleep(10)
        main()
    elif choice1 == 2:
        print(
            'You run, but when you think he wont see, he notices and chases you!'
        )
        print('You can keep running, or dive into a hole you are passing.')
    else:
        print('Invalid.')
        print('GAME OVER')
        time.sleep(10)
        main()
    choice2 = input('Will you dive in? y/n>')
    clear()
    if 'y' in choice2:
        print('You dive in, and there is water at the bottom!')
        print('The lion is confused, and wanders off.')
    elif 'n' in choice2:
        print('While you are running, you get exhausted.')
        print('The lion catches up, and eats you.')
        print('GAME OVER')
        time.sleep(10)
        main()
    else:
        print('Invalid.')
        print('GAME OVER')
        time.sleep(10)
        main()
    print('You are in a cave, and you wander')
    print('around. Amanda followed you, so she is with you, but')
    print('Carter is still above. Should you look for him, or are')
    print('the hippos more important?')
    print('1 for explore the cave, 2 to look for Carter.')
    choice3 = input('>')
    clear()
    if '1' in choice3:
        print(
            'You explore the cave, looking for an exit when you see a crystal! But it is over a deep chasm.'
        )
        print(
            'You might be able to jump it, but youre not sure. What do you do?'
        )
        print('Will you jump it? y/n')
        choice4 = input('>')
        clear()
        if 'y' in choice4:
            print('You make it over! You grab the crystal.')
            print(
                'It speaks to you. It says, "You will be punished for your greediness".'
            )
            print('Then, a boulder falls and crushes you.')
            time.sleep(10)
            main()
        elif 'n' in choice4:
            print(
                'You start exploring, but the cave collapses and you and Amanda die.'
            )
            print('But Carter makes it out alive.')
            print('GAME OVER')
            time.sleep(10)
            main()
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    elif '2' in choice3:
        print('You find an exit and climb out. You look')
        print('around, but you dont see Carter anywhere.')
        print('Suddenly, a jeep pulls next to you. The people inside')
        print('offer to take you for a ride to find Carter. Do you')
        print('accept?')
        choice5 = input('Do you ride with them? y/n>')
        clear()
        if 'y' in choice5:
            print('You and Amanda are excited. You might find Carter!')
            print('Then, your jeep falls into another hole!')
            print(
                'When you land, you see somthing shining. Do you get it?')
            choice6 = input('Do you get it? y/n>')
            clear()
            if 'n' in choice6:
                print(
                    'You press a button on the middle console in the jeep')
                print('It starts playing "baby shark" over and over.')
                print(
                    'It drives you out of the jeep. You fall down a hole and die.'
                )
                print('GAME OVER')
                time.sleep(10)
                main()
            elif 'y' in choice6:
                print('You head for it. Its a teleportation')
                print('device! You teleport out of the hole.')
                print(
                    'Then the teleporter dies. You thank your drivers, and they go away'
                )
            else:
                print('Invalid')
                print('GAME OVER')
                time.sleep(10)
                main()
        elif 'n' in choice5:
            pass
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    print('You wander around, when you see someone. Its Carter!')
    print('You are reunited.')
    print(
        'After all the craziness, you remember you have to find the hippo.'
    )
    print('You can head to some giraffes, or there are a')
    print(
        'bunch of zebras the other way, and a family of lions the other way. Where will you go?'
    )
    print('1 for giraffes, 2 for zebras, 3 for lions')
    choice7 = input('>')
    clear()
    if '1' in choice7:
        print('You head over. Amanda says you should')
        print('climb on top of one. Will you?')
        choice8 = input('Will you? y/n>')
        clear()
        if 'y' in choice8:
            print('You climb on, and you see one of the hippos!')
            print(
                'But, the giraffe throws you off and you break your leg.')
            print(
                'You black out. You wake up in a hospital room. Carter is')
            print(
                'there. He tells you everything. Apparently, They got the first'
            )
            print(
                'hippo you spotted, and they called in a helicopter for you.'
            )
            print(
                'They said you werent in good enough condition, so they went and'
            )
            print(
                'found the other hippo without you. You and Amanda and Carter'
            )
            print(
                'recieved 250,000 dollars from S.A.F.A.R.I. for your deed.'
            )
            print('Enjoy your reward!')
            print('--------')
            print('ENDING 1')
            print('--------')
            time.sleep(10)
            main()
        elif 'n' in choice8:
            print('You get kicked in the head by')
            print('one of the giraffes. You get a')
            print('concussion. Carter and Amanda')
            print('try to save you, but they run out of time and')
            print('you die. But if it soothes you, it didnt')
            print('make Amanda feel bad one bit.')
            print('GAME OVER')
            time.sleep(10)
            main()
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    elif '2' in choice7:
        print('You go to the zebras. Then they start running!')
        print('You wonder why. Then you see a lion! But it looks')
        print(
            'scared. Thats because its being chased by one of the hippos!')
        print(
            'You get out of the way, and they dont even notice. Carter says'
        )
        print(
            'to follow it because it might have a mate. Amanda says to catch'
        )
        print('it now in case it might not have a mate. What do you do?')
        choice9 = input('Do you follow it? y/n>')
        clear()
        if 'y' in choice9:
            print(
                'You start to follow it, when you fall into a small ravine! You break your leg.'
            )
            print(
                'Carter and Amanda cant pull you up. While they try, they fall in! Then, a lion'
            )
            print('spots you and you get misrably eaten.')
            print('GAME OVER')
            time.sleep(10)
            main()
        elif 'n' in choice9:
            print(
                'You chase it around, when it falls into a hole and traps itself!'
            )
            print(
                'Its mate comes to help it, and falls in! You call over a helicopter'
            )
            print(
                'and it gets them. You get 275,000 dollars from S.A.F.A.R.I. for your'
            )
            print('reward!')
            print('--------')
            print('ENDING 2')
            print('--------')
            time.sleep(10)
            main()
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    elif '3' in choice7:
        print('You slowly walk closer to them. Then, you see two of the')
        print('baby hippos, a boy and a girl, surrounded by them! Amanda')
        print(
            'wants to rush in and get them, but Carter wants to creep up')
        print('to them. What do you do?')
        choice10 = input('Do you rush in? y/n>')
        clear()
        if 'y' in choice10:
            print('They notice and start to chase you!')
            print('You keep running, and think you are doomed, when')
            print('you hear a new noise. The jeep! They ask if you')
            print('need help. ')
            choice11 = input('Do you go with them? y/n>')
            clear()
            if 'y' in choice11:
                pass
            elif 'n' in choice11:
                print('You go it alone. You do good for a while,')
                print(
                    'but you trip and fall! The lions eat you and your crew.'
                )
                print('GAME OVER')
                time.sleep(10)
                main()
            else:
                print('Invalid')
                print('GAME OVER')
                time.sleep(10)
                main()
        elif 'n' in choice10:
            print(
                'While you are sneaking up, they go away, so you easily get them.'
            )
            print(
                'S.A.F.A.R.I. wanted grownups, so they could get the exibit as fast as'
            )
            print(
                'possible, so you only got 5,000 dollars. but still a decent payout'
            )
            print('---------')
            print('ENDING 3')
            print('--------')
            time.sleep(10)
            main()
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    else:
        print('Invalid')
        print('GAME OVER')
        time.sleep(10)
        main()
    print(
        'You go with them, and outdrive the lions. You thank the drivers, and get out.'
    )
    print('You get out, and you spot a road! Do you go down it?')
    choice12 = input('Do you? y/n>')
    clear()
    if 'y' in choice12:
        pass
    elif 'n' in choice12:
        print('You wander around a few days. You get hungry.')
        print('You see a plate of steak. You head for it.')
        print('Its a mirage! You and your crew die of hunger.')
        print('GAME OVER')
        time.sleep(10)
        main()
    else:
        print('Invalid')
        print('GAME OVER')
        time.sleep(10)
        main()
    print('You go down it, and there is a fork')
    print('in the road. One way has a mountain at')
    print('the end, and the other has a stream.')
    print('1 for mountain, 2 for stream')
    choice13 = input('>')
    clear()
    if '1' in choice13:
        print('You head for it, but')
        print('its farther than it looks.')
        print('When you finally get there, you are')
        print('out of supplies. There is a shack there.')
        choice13 = input('Do you go in? y/n>')
        clear()
        if 'n' in choice13:
            print('You starve.')
            print('GAME OVER')
            time.sleep(10)

            main()
        elif 'y' in choice13:
            print('There is a remote of some sort.')
            print('It has a button on it. Do you press it?')
            choice14 = input('Do you? y/n>')
            clear()
            if 'n' in choice14:
                print('You starve to death.')
                print('GAME OVER')
                time.sleep(10)

                main()
            elif 'y' in choice14:
                print('You press it.')
                print('It teleports you')
                print('to the stream!')
            else:
                print('Invalid')
                print('GAME OVER')
                time.sleep(10)

                main()
        else:
            print('Invalid')
            print('GAME OVER')
            time.sleep(10)
            main()
    elif '2' in choice13:
        print('You make it to the stream')
    else:
        print('Invalid')
        print('GAME OVER')
        time.sleep(10)
        main()
    print('There are hippos all over in it')
    print('You scan the stream with your eyes')
    print('There! You see one! Theres another!')
    print('And another! They all have a red stripe!')
    print('You call in a S.A.F.A.R.I. plane. They take them and')
    print('make an exibit. You found the motherload!')
    print('As a reward, they give you ONE MILLION DOLLARS!!!!')
    print('Enjoy!')
    print('--------')
    print('ENDING 4')
    print('--------')
    time.sleep(10)
    main()
def calc():
    while True:
        print(
            "Type in your equation. Type 'help' for an example or 'exit' to leave"
        )
        equ = input("")
        if equ == "help":
            print("Use + for addition:")
            print("1 + 1")
            print("Use - for subtraction:")
            print("1 - 1")
            print("Use / for division:")
            print("1 / 1")
            print("Use * for multiplication:")
            print("1 * 1")
        elif equ == "exit":
            break
        else:
            try:
                runme = 'res =' + equ
                exec(runme)
                exec('print("The answer is:", res)')
                time.sleep(2)
            except:
                print("There was an error in your equation. Try again.")
def sdm():
    global devmode, menuname, menuoptions
    menuname = 'What do you want to set Dev mode to?'
    menuoptions = ['True', 'False']
    inp = showmenu()
    if inp == 'False':
        ndms = 'devmode = False'
        devmode = False
    else:
        ndms = 'devmode = True'
        devmode = True
    with open(__file__, 'r') as f:
        lines = f.read().split('\n')
        new_line = (ndms).format(ndms)
        '\n'.join([new_line] + lines[1:])

    with open(__file__, 'w') as f:
        f.write('\n'.join([new_line] + lines[1:]))
    print('Complete.')
    time.sleep(1)
def extapp():
    if devmode == False:
        print(
            "This tool is used to run an external application. The app should be a .py (Python) file and should be in the same folder as Spear OS. The app code should be in a function called 'app()'. Please enter the file name (without '.py'). Or, if you downloaded an app, just type its name."
        )
    else:
        print('Enter the app name:')
    name = input('>')
    print('Loading the app...')
    try:
        exec('import ' + name)
        clear()
        exec(name + ".app()")
        time.sleep(2)
        clear()
        print('This app has exited.')
    except Exception as e:
        print('There was an error while trying to run the app.')
        if devmode == True:
            print(e)
    time.sleep(2)
def dlapp():
    print(
        "This will download apps for you. You will need the link to the app. The app MUST be a Python script (.py). Enter the link below:"
    )
    try:
        applink = input(">")
        r = requests.get(applink, allow_redirects=True)
        print(
            "Enter the name you want to use to run this application. REMEMBER IT!"
        )
        fn = input(">")
        fn = fn + '.py'
        open(fn, 'wb').write(r.content)
        print('Success! Use the Load App application to use your new app!')
    except Exception as e:
        print("An error ocurred:", e)
    time.sleep(3)
def main():
    global menutitle, menuoptions, menuname
    while True:
        menuoptions = ['Python Shell', 'System Shell', 'XDecoder', 'Calculator', 'Games', 'Load App', 'Download App', 'Settings']
        menuname = 'home'
        inp = showmenu()
        inp = str(inp)
        clear()
        if inp == 'Python Shell':
            pycmd()
        elif inp == 'System Shell':
            cmd()
        elif inp == 'XDecoder':
            xdecoder()
        elif inp == 'Calculator':
            calc()
        elif inp == 'Load App':
            extapp()
        elif inp == 'Download App':
            dlapp()
        elif inp == 'Settings':
            settings()
        elif inp == 'Games':
            games()
        else:
            pass
if devmode == False:
    print(colorama.Fore.GREEN + '[Done]')
    print('Spear OS is ready' + colorama.Style.RESET_ALL)
    print('Tip:', random.choice(tips))
    input("Press Enter to continue to Home")
main()
clear()
#Bottom