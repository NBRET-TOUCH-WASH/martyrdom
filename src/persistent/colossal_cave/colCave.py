#coding:utf-8

#modules
import os
import time

#? colorama lib setup
from colorama import init, Fore, Back, Style
init()

FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

def color_print(s, color = Fore.WHITE, brightness = Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#variables
#transition speeds
FLASH = 0.25

QUICK = 1.0
FASTER = 2.0
FAST = 3.0

MEDIUM = 4.0

SLOW = 5.0
SLOWER = 6.0
LONG = 7.0


arrivalLightning = R"""
       .                                                                        
     ..:::...                                                                   
     .:.::^:......                                                              
     .....:^^:::::..                                                            
    .    ...:::^^!::..                                                          
            ...:^!^::..                                                         
              ..::^!~::...                                                      
               ..::^7!^^::...                                                   
                ..:^~??!!~^::..                                                 
                ..:^!~~~~!77~::..                                               
                ..::~~:::^^~?!^::..                                             
              ...:^^^:....::^!77!^:..                                           
             ...:^:....   ..::^~?7^:..                                          
          ....:::...        .::^!J^^:.                                          
        ...:::...            .:^~J~^:..                                         
         .....              ..:^~7J^^:.                                         
          ..               .:^~~!JY~~^:..                                       
          .              ..:^~?YY5PY?!~^^:...                                   
          .              ..:^7G7777?JYJ7!~^^::.                                 
                          .::^?^^^~~~!?YYJY?~^^::..       ........              
                            ........:^^~!775Y!!~~^^^:::::^^^^^^^^:::...         
                                     ..::^~!Y5YY5Y?7!!!!777?J55J??7~~^:::...    
                                        ..:^~!?Y5JYY5YY5YYJJ??YPYJJJ?J7!~~^:.   
                                          .:^~JJ!!!!!!!~~~~~~~~!?Y5J??J??7!^:.  
                                           .::^7?7~~^^^:::...::^~!?Y55P5J!~^:.  
                                            ..::^!77!^^:..  ..::^~!7JYYY5J~^:.  
                                             ..::^^!J?!^::...:^!7777!~~~~~^:.   
                                           .....:^^!??J~~^::^^?!~^::::::...     
                                            ..:::^^~7??7~~~~~!J~^::.            
                                           ...::~^~~7!~77~!!!JJ~^:.             
                                          ...^^^~^^^^^^~7!!7?Y7~^:.             
                                         ...:~:::....::^~7?JYY7~~^:.            
                                       ...::^:.......::^!7777!!~^::.            
                                       .:::::......::^^~~^~~^^::..              
                                      .:...:....:^^^^:::::^^...                 
                                      ..   ..:.:~::.......::.                   
                                      .     ..::^:...                           
                                             ..:^:..                            
                                              .::..                             
                                                .                               
"""



#script
def play_colCave(playerName):
    clear_console()
    time.sleep(1)
    print(arrivalLightning)
    time.sleep(FLASH)

    clear_console()
    time.sleep(QUICK)
    print("\nWhen you open your eyes for what feels like the first time in about seven months, you notice you've been transported somewhere.")
    time.sleep(MEDIUM)
    print("It is dark, rainy and stormy, making out the shape of the things before you is hard.")
    time.sleep(FAST)

    print("\nAfter a few seconds of effort, you start to combine the few elements your brain can properly process:")
    time.sleep(MEDIUM)
    print("A door, ", end="")
    time.sleep(QUICK)
    print("windows, ", end="")
    time.sleep(QUICK)
    print("a roof...")
    time.sleep(FASTER)

    print("\nYou realize you're standing before a house, the lightnings' glow rapidly printing its image on your retina.")
    time.sleep(MEDIUM)
    print("Ahead of you is a path to enter said house ; behind you, a road, crossing your path left to right from the edges of a street that seemingly stretches into infinity.")
    time.sleep(LONG)

    while True:
        userInput = input("\n\n\nWhat will you do?\n> ").upper()

        if "GO TO" in userInput:
            if "HOUSE" in userInput:
                color_print("\nYou approach the house.", Fore.CYAN, Style.BRIGHT)
                time.sleep(FASTER)
                print("From what your eyes can gather, it looks pretty modern.")
                time.sleep(MEDIUM)
                print("A nice little porch leading to a regular wooden door framed into a normal white cement wall ; truly an ordinary home.")
                time.sleep(LONG)
                break

        if "LOOK" in userInput:
            if "BEHIND" in userInput:
                color_print("\nYou look behind yourself.", Fore.CYAN, Style.BRIGHT)
                time.sleep(FASTER)
                print("While as expected, a road crosses your gaze's path, an infinite black void you'll never fully make out stretches and blends into itself from across the street.")
                time.sleep(MEDIUM)

                print("\nAs you blink, text flashes before your pupils as if painlessly carved into your eyelids with light, it reads:")
                time.sleep(MEDIUM)
                color_print("\"Do not stare into the abyss too long, for it too, will stare back.\"", Fore.MAGENTA)
                time.sleep(FAST)
                color_print("\nYou feel hollow just by trying to discern what causes the darkness to stir in unthinkable ways.", Fore.YELLOW, Style.DIM)
                time.sleep(MEDIUM)
                continue

            if "AT SELF" in userInput:
                color_print("\nYou look at yourself.", Fore.CYAN, Style.BRIGHT)
                time.sleep(FASTER)
                print("You think you recognize what you see, but deep down you know that's just a lie you keep telling yourself.")
                time.sleep(SLOW)
                color_print("\nYou feel empty realizing that all of this warping across the realm has caused you to lose more and more of what composes you.", Fore.YELLOW, Style.DIM)
                time.sleep(SLOW)
                continue

        if "GET" in userInput:
            color_print("\nThere is nothing to get here.", Fore.CYAN, Style.BRIGHT)
            time.sleep(FASTER)
            continue

        if "TALK TO" in userInput:
            color_print("\nThere is nothing and nobody to talk to here.", Fore.CYAN, Style.BRIGHT)
            time.sleep(FASTER)
            continue

        if "RETURN COFFIN" in userInput:
            time.sleep(1)
            color_print("\nYet Another conflict", Fore.GREEN)
            time.sleep(1)
            color_print("Where communication is dead", Fore.GREEN)
            time.sleep(1)
            color_print("Their solution is a bullet to your head", Fore.GREEN)
            time.sleep(1)
            color_print("\n[...]", Fore.GREEN)
            time.sleep(1)
            color_print("\nYou're a coffin returned hero", Fore.GREEN)
            time.sleep(1)
            color_print("But you've died for nothing.", Fore.GREEN)
            time.sleep(1)
            color_print("\n[...]", Fore.GREEN)
            time.sleep(1)
            color_print("\nDie for nothing", Fore.GREEN)
            time.sleep(1)
            color_print("Like all those before", Fore.GREEN)
            time.sleep(1)
            color_print("\nScythelord - \"Die for Nothing\", Toxic Minds - track 3; 2016", Fore.GREEN)
            time.sleep(2)


    clear_console()
    time.sleep(QUICK)
    print("\nBut then you realize it.")
    time.sleep(FASTER)
    print("You realize why here, ")
    time.sleep(FASTER)
    print("why this home, ")
    time.sleep(FASTER)
    print("why you can't see the sky and the surroundings of this house outside, ")
    time.sleep(FAST)
    print("why you can't recognize yourself, see what you really look like, ")
    time.sleep(FAST)
    print("why you feel so empty and hollow inside, ")
    time.sleep(FASTER)
    print("why nothing's here,")
    time.sleep(QUICK)
    print("but everything's there, ")
    time.sleep(QUICK)
    print("and why the house and its content are but a vast decoy, ")
    time.sleep(FASTER)
#midlertidig
    clear_console()
    time.sleep(QUICK)
    print("\nAnd now it all makes sense.")
    time.sleep(FASTER)
    print("And now \"all in here makes sense to you\".")
    time.sleep(FAST)

    clear_console()
    time.sleep(QUICK)
    print("\nYou are ", end="")
    color_print("{}".format(playerName), Fore.CYAN, end="")
    print(".")
    time.sleep(FASTER)
    print("For as long as you can remember you've ", end="")
    color_print("Entered the HomeGeon", Fore.LIGHTRED_EX, end="")
    print(", only to get you to come and serve ", end="")
    color_print("their ", Fore.LIGHTMAGENTA_EX, end="")
    print("interests, or die trying, in a final state of ", end="")
    color_print("Martyrdom ", Fore.RED, end="")
    print("for ", end="")
    color_print("their ", Fore.LIGHTMAGENTA_EX, end="")
    print("contracts.")
    time.sleep(LONG)

    clear_console()
    time.sleep(QUICK)
    print("\nThen ", end="")
    color_print("their ", Fore.MAGENTA, end="")
    print("voice is heard again:")
    time.sleep(FASTER)
    color_print("\nWell, well, isn't this just like old times.", Fore.MAGENTA)
    time.sleep(FAST)
    color_print("So nice to have you with us, {}.".format(playerName), Fore.MAGENTA)
    time.sleep(FAST)
    color_print("I will see you up ahead.", Fore.MAGENTA)
    time.sleep(FAST)

    print("\nAnd with this sudden recollection, ", end="")
    color_print("you ", Fore.CYAN, end="")
    color_print("Enter the HomeGeon ", Fore.LIGHTRED_EX, end="")
    print("once again.")

    input("(Press [RETURN] to accept Martyrdom) > ")

#! DEBUG!
#play_colCave("debugName")