print("Grabbing start-up dependencies and moving screen area to bottom...")
import time
import colorama

colorama.init()
print(colorama.Fore.BLUE, colorama.Style.DIM)
for i in range(0, 120):
    print()
print(r'''
''')
print(r'''
  >=>>=>   >======>   >=======>       >>       >======>     
>=>    >=> >=>    >=> >=>            >>=>      >=>    >=>   
 >=>       >=>    >=> >=>           >> >=>     >=>    >=>   
   >=>     >======>   >=====>      >=>  >=>    >> >==>      
      >=>  >=>        >=>         >=====>>=>   >=>  >=>     
>=>    >=> >=>        >=>        >=>      >=>  >=>    >=>   
  >=>>=>   >=>        >=======> >=>        >=> >=>      >=> 
                                                            
                      >===>        >=>>=>                   
                    >=>    >=>   >=>    >=>                 
                  >=>        >=>  >=>                       
                  >=>        >=>    >=>                     
                  >=>        >=>       >=>                  
                    >=>     >=>  >=>    >=>                 
                      >===>        >=>>=>                   

              POWERED BY PYTHON AND REPL.IT                                                                        
''')
print(colorama.Style.RESET_ALL + 'By B Game Studios')
time.sleep(2)
print('Setting up Spear OS...')
print('Importing libraries...')
import os, socket, datetime, sys, random
print('Defining functions...')
def clear():
    for i in range(0, 120):
        print()
def cmd():
    try:
        print("Host Command Line")
        print("Use 'hcl-info' for info")
        print("Use 'hcl-exit' to return to Home")
        def maincmd():
            while True:
                cmd = input(socket.gethostname() + ":" + os.getcwd() + ">")
                if cmd == "hcl-info":
                    print("PyCMD is an attempt at a command line written completely in Python.")
                    print("Version 1.0")
                    print("Changelog:")
                    print("First release")
                    print("Built in Windows, bugs may occur in other operating systems.")
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
    computerchoice = random.randint(1, 3)
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    yourchoice = input('>')
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
    time.sleep(3)
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
        
    except:
        print("An error occurred in your code and the Python Shell will shut down to prevent crashing in 3 seconds.")
        time.sleep(3)
        home()
def rl():
    
    print("REMEMBERLIST")
    rlist = open("rememberlist.txt", "r")
    print("Current list:")
    print(rlist.read())
    rlist.close()
    print()
    print("1. Close")
    print("2. Rewrite List")
    c = input(">")
    clear()
    if c == "2":
        rlist = open("rememberlist.txt", "w")
        print("Type what you want to put on the list, press Enter to save.")
        text = input("")
        rlist.write(text)
        rlist.close()
        clear()
        print("Saved.")
        print("1. Close")
        print("2. REMEMBERLIST home")
        c = input(">")
        if c == "2":
            clear()
            rl()
def xdecoder():
    print("=XDECODER=")
    print("Spear OS Edition")
    while True:
        print("1 for encoding")
        print("2 for decoding")
        operation = input(">>>")
        if operation == "1":
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
        elif operation == "2":
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
            print("Here's your encoded text:", txt)
        again = input("Go again? [Y/N] >>>")
        if again.upper() == "N":
            break
def main():
    while True:
        clear()
        ptime = datetime.datetime.now()
        curhour = ptime.hour
        if ptime.hour > 11:
            aorp = "PM"
            curhour -= 12
        else:
            aorp = "AM"
        print(str(ptime.month) + "/" + str(ptime.day) + "/" + str(ptime.year), str(curhour) + ":" + str(ptime.minute), aorp)
        print("Home")
        print(colorama.Fore.YELLOW)
        print("| 1. Rock, Paper, Scissors | 2. Python Shell |")
        print("| 3. System Shell | 4. Shutdown |")
        print("| 5. Suspend | 6. Rememberlist |")
        print("| 7. XDecoder |")
        print(colorama.Style.RESET_ALL)
        inp = input(">")
        if inp == "1":
            clear()
            rps()
        elif inp == "2":
            clear()
            pycmd()
        elif inp == "3":
            clear()
            cmd()
        elif inp == "4":
            clear()
            sys.exit()
        elif inp == "5":
            print("Suspending in 5 seconds, press Enter to unsuspend.")
            time.sleep(5)
            clear()
            susp = input("")
        elif inp == "6":
            rl()
        elif inp == "7":
            xdecoder()
        else:
            clear()
    main()
start = input("Press Enter to continue to Home")
main()
