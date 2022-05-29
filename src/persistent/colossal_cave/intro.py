#coding:utf-8

#modules
import os
import time
import random
from turtle import clear

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


#import blessings.introAscii as introAscii



#classes



#functions
def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def witness_rapture():
    for i in range(0,7,1):
        print(introGlitch1)
        time.sleep(0.1)
        clear_console()
        print(introGlitch2)
        time.sleep(0.1)
        clear_console()
        print(introGlitch3)
        time.sleep(0.1)
        clear_console()
        print(introGlitch4)
        time.sleep(0.1)
        clear_console()
        print(introGlitch5)
        time.sleep(0.1)
        clear_console()
        print(introGlitch6)
        time.sleep(0.1)
        clear_console()


def play_colCave_intro1():
    """ plays the "colossal cave adventure"-like-related intro """

    #$ for an easier-access copy-paste
    #color_print("To ", Fore.MAGENTA, end="")
    #color_print("You", Fore.CYAN)

    time.sleep(2)
    color_print("\nMy apologies, it must seem to you as if I forgot everything about you, but what was your name again?\n", Fore.MAGENTA)
    time.sleep(4)

    #player inputs their name

def play_colCave_intro2(playerName):
    """ plays the "colossal cave adventure"-like-related intro """

    #$ for an easier-access copy-paste
    #color_print("To ", Fore.MAGENTA, end="")
    #color_print("You", Fore.CYAN)

    #player inputs their name

    time.sleep(1)
    color_print("\nAh, ", Fore.MAGENTA, end="")
    time.sleep(1)
    color_print("that is right.\n", Fore.MAGENTA)
    time.sleep(2)
    color_print("Again, it must appear to you as if I forgot about you, but please, trust me when I say that this could not be farther from the truth.", Fore.MAGENTA)
    time.sleep(5)
    color_print("I have been looking for you all this time, {}.".format(playerName), Fore.MAGENTA)
    time.sleep(3)
    color_print("In fact, ", Fore.MAGENTA, end="")
    color_print("we ", Fore.LIGHTMAGENTA_EX, end="")
    color_print("all were.", Fore.MAGENTA)
    time.sleep(3)

    clear_console()
    color_print("\nAnd to fix that, and finally get a hold of you, I was tasked with bringing you back here.", Fore.MAGENTA)
    time.sleep(5)
    color_print("To both get you to see what ", Fore.MAGENTA, end="")
    color_print("we ", Fore.LIGHTMAGENTA_EX, end="")
    color_print("want you to see, and understand what ", Fore.MAGENTA, end="")
    color_print("we ", Fore.LIGHTMAGENTA_EX, end="")
    color_print("want you to understand.", Fore.MAGENTA)
    time.sleep(5)
    color_print("I'm sure this brings nothing but confusion in your mind, after all, you keep bouncing around this realm aimlessly, which in turn tasks us with the quite difficult objective to track you down.", Fore.MAGENTA)
    time.sleep(7)
    color_print("But that all belongs to the past, now.", Fore.MAGENTA)
    time.sleep(4)

    clear_console()
    time.sleep(1)
    color_print("\nRight now, focus on taking a good ", Fore.MAGENTA, end="")
    color_print("LOOK AT ", Fore.CYAN, end="")
    color_print("the things around you ; ", Fore.MAGENTA, end="")
    time.sleep(4)
    color_print("don't hesitate to ", Fore.MAGENTA, end="")
    color_print("GET ", Fore.CYAN, end="")
    color_print("anything that catches your attention ; ", Fore.MAGENTA, end="")
    time.sleep(4)
    color_print("and without too much misfortune should you not run into anything - or anyone - to ", Fore.MAGENTA, end="")
    color_print("TALK TO", Fore.CYAN, end="")
    color_print(".", Fore.MAGENTA)
    time.sleep(5)

    clear_console()
    time.sleep(1)
    color_print("\nMay all in this place make sense to you, and may you understand why I, as well as my... ", Fore.MAGENTA, end="")
    color_print("employers", Fore.LIGHTMAGENTA_EX, end="")
    color_print(", take such an interest in ", Fore.MAGENTA, end="")
    color_print("your person", Fore.CYAN, end="")
    color_print(".", Fore.MAGENTA)
    time.sleep(7)



#variables
#intro glitches frames
introGlitch1 = R"""
IIIII?I777$77777777$$$777$$77$$$$$7$ZZZZZZZOO88888DNNND88888OOOOOOOOOOOOOOOZ$$$$
II?????7777$$$I$I7777777777II77777I77777$ZZZZO88888:DDDD8DDDDDDDDDDDDDDDDOZZZ$77
I?++++?7$Z$ZZZZZZOOO88OOOOZ788D88OOOZZZZOOOOOZ$$$$$$$$7777777$$$$$$Z$777I===++++
I??I?++?IIIIIIIII777IIIIIIII777IIIIIIIIIIII???????????????????IIIIIII??IIIIIII??
III77II?I77777$$$ZZZZ$$$$$$$ZZZ77IIIIII??I??+++++++++++++++++?IIII77I??IIIIII?++
III77I?II777777III77ZZOOOOOOOOZIIIIIIIIII???+++++++++++???????I7I$$ZZOZZZZ$$$$$$
77I77I+=?$$$$ZZZ$$$$ZZOOZZOOOZO$$ZZZZZZZZZ7?OZZZZZZZZZZOOOO888888DDDDNND88OOOOOO
$7I777$$$$ZOZOOZZ$$77$888OO8OOOO8888888888?IZZZODDD8DDDDDDDDDDDDDNNNNNNNNDDDDD8O
$777777$$ZZOOOOOOOZZZODNNNDDDDNNDDDDDDDDDD88I77ZNNNNNNDNDDMMMMMMMMMMMNNNNDDD88OO
7I?I?????IIIIIIIII???IIIII?????IIIII777$$$77ZZZZZZZ$$$$$7$ZZ$ZZZZ$ZZZZZZOO8OOOOZ
I+=++++++?+++++++++++??I?++=+++++====+==~===~~=~~=+++?+??++++====++=====++++=+++
I+=+===+=++??+??===~==++===~~~~~~~====~~~~~~~~~~~~===+++++++===~~~~==========+==
I++++++++++?++==+==~==+++==~~~~~~~=====~~~~~~~~~=====++?????????????????I???II==
I++++++++=++++==++=====++==~~~~::~~~~~:,:,,,,,,,,,,:,........,,,..,,,,,,,,,,,,.,
I++++==+========++++===++=~~~~~:~~~===~:~~~~~~~~~~~~~==============~============
I+++++==========+++====+=~~~~~~::~~~~~~,,,,:,::::::::,,,,,,,,,,,::::::::::::::::
I++???==========+++====+==~=~~~~::~~~~~,,,,:::::::::,,,.........,,,,,.....,,,:::
I++???=~~=~~~~~~=~~~~====~~~::::,:~~~~~,::::,:::,,,,,....,..,,,::::::~~~~~~~~:::
I++???====~~~~~:~~:~~~~~~~~~~~~:::~====,::::,,::,::,,...,,..,,,,,,,,,,,:::::,,::
I++???====~~~~~~~~:~~~~~~~~~~~~:::~====,::::,,:,,,,,,.......,,,,,,,::,,,,,,,,,..
I++I?+====~~::~~~::~~~~===~~~~~::~~=+==,::::,,,,,,,,,. . ...,,:,,,:,,,,,,,,,,,,,
I++II?=~~~~~:~~~~~~~~==++++++======++++,::::,,:,,,,,,.    ..,,:::::,::::::,,,,,,
I?+I?+=~~~~~~~~~=~~=======~~~~~~~===+==:::::,,:::,,,,.    ..,,:::~~,,:,,,,,,,,,,
I?+77III7777$77$Z$Z$$7$OOZ$$77IIIII+++?I?+++77??I??77ZZZ$$$$ZZ$$$$$Z$$$$$77777$$
?+?77I7$$$$$$$$$$7I???I$$77IIIIII??+++?I????$$III??77ZZZZZZZZZZZZZ$OZ$$ZZ$I7777$
??+77I7Z$$$$$$77$II?+?I$77IIIIIII??+++?I????$Z7777III7$$$$$$ZZ$$$$$88OOOO7I+????
??+77I$Z$$$$$$7$$II?+?I$77II777777777777????$$777$7I7$$$7$$7$$77I77OOZZOZ7?+++==
I?+77I7$7777777$ZII+??I$$7IIII777777I777I???II+++++++II??III7777III$$$$$$7I?++++
7??Z$77$$777777$$II++?I$777IIII777777777I?????+++++++???$III$$77777$Z$$$$7?+?+??
"""

introGlitch2 = R"""
=====++===~=======~~~~~=~~~==~~~~~=~~~~~~~::::::::,,,,,,,::::::::::::::::::~~~~~
==+++++===~~~~=~=======================~~~~~:::,::,I,,,,,,,,,,,,,,,,,,,,,:~~~~==
=++++++=~~~~~~~~::::::::::~=,,,,,:::~~:::::::~~~~~~~~~~~====~~~~~~~~~====?????+?
++++++++========================++=+===+==++++++++++++++++++++=======+++======++
=======+======~~~~~~~~~~~~~~:~~=====+==++++++++++++++???????+++======++====+=+++
======+=============~~:::::::::==+=++===++++???+++++++++++++++===~~~~::::~~~~~~~
======??+~~~~~~:~~~~~~:::::::~:~~~~~~~::~~=+:~~~~~~~~~:::::::::::,,,,..,,:::::::
~===~=~~~~~:::::~~~==~:,:::::::::::,,:::,,+=~~~:,,,,,,,,,,,,,,,,,,,......,,,,,::
~======~~~~:::::::~~~:,...,,,,,,,,,,,,,,,,:,===~...,,,,,,,..............,,,,,:::
==+++++++=========+++++=+++++++========~~~~~::~~:::~~~~~=~~~~~:~~~~~~:::::::::::
=+?+++++?++++++?+++?+++=++???????????+??????????I????+++++++????????????????????
=+???????+++++++???????+?????????????????????IIII????+++????????????????????????
=+?++????+++++??+?????++??????II????????????III??????+++++++++++++++++++++++++??
=+?++?+++??+++?????????+???II?IIII??IIIIIII777777III7777777777777777777777777777
=+??????????????++??????????I?IIII?????IIIIIII?IIII????????????????I????????????
=?+++???????????++?????+???????IIII???IIIIII7IIIIIIII7777777777IIIIIIIIIIIIIIIII
++++++??????????++?????+???????IIIIII?I7IIIIIIIIIIIII77777777777777777777777IIII
++?+++??????II?I??????????IIIIII7II????7IIII7IIIIIII7777777777IIIIIIIIIIIIIIIIII
=+?+++??????IIII?IIII????II??IIIII?????IIIII7IIIIIII7777777777777777777IIIIIIIII
=+?+++?????IIIII?IIII???I??I?IIIIII????IIIII77II7777777777777777777III7777777777
=+?=++????IIIIII?IIII??????I?IIIII?????IIIII77I7777777 7 77777II77I7I7II77777777
=+?==+????IIII?I?II????++++????????+++?IIIII77II777777    77I7IIIIIIIIIIIIIIII77
=++=++??IIIIII?I???????????????????????IIIII77IIIII777    7777IIIII77II777777777
=++=========~~=~~~~~~=~:::~~======+++++=++++==++=++==~~~~~~~~~~~~~~~~~~~~=====~~
+++====~~~~~~~~~~==+++=~~========++++++=++++~~===++==~~:::~~::~~~~~::~~~~~====~~
+++====~~~~~~~=~~==+++=~~=======+++++++=++++~~=======~~~~~~~~~~~~~~::::::==+++++
+++=~=~~~~~~~~=~~==+++=~~===============++++~~===~===~~~=~~=~~=====:::::~=+++???
=++====~~======~~=++++=~~================+++=++++++++++++====~=====~~~~~~==+++++
=++~~==~~======~~=+++++~~================++++++?++++++++~===~~=====~~~~~~=++++++
"""

introGlitch3 = R"""
++++++++???I???I???II??????I?+++++++++++++++++==+?++++++++++=+====++++++?+?+++++
++??????IIIIII??????????I???I+++++++++++=====+++++==+========++~+++++++++++++++=
++++?==?IIIII???+++++++IIII??~==~~~~~~~~~~~~~~===~===========~==+====+++==~===??
++++=+??IIIII?????????III?++?~~~:::::::::~=~::::,,,,....,::::,,,,::~~~~~~~~~~~~:
++=~~:::~+????+=========+++++++=========+==~===:=~~~~~~~~==~~~~~:::::::::~::::::
+==~~~~:=+????+++?++++???+++++=?+++++++=+++++++++==+============~=+???IIIIIIIIII
+==~::==+???++====~:~=~==~=============~======~~~~===~~=~~~=====~++++++?????++++
+++~~:==+???++=~===~~~~~===~=========~=+++==~================++==++?????++++++++
++=~::==+????+++===:~===++??~=======~~==+++========~~=~========~~=++++++++++++++
?==~~,==???++?+=++==++===++==============~~=~~~~~~:~:::::::::::::~~~============
+=~:::==++??++++==++++==+++=+++=+++++==+=========~~~:::~::::::~:~=++++++++~~=~==
++=:::==+?????++==++=+===+==~==?===++=~========++~~=~==~~====++===++====++++=+++
++=~~,=+??????+++=++=+===========++++~~=~=====+=+=~+========~~~~~:~~:~:::,,,,,,,
?????+???III??+++==+=~~~+++++?+++++++~==++++++?+?~~+==+++=~~:::::~~=+++=+==~~~~=
?IIIIIIIIIIII?+??++++~~~+++++++====++===++==++++?~=+++++==~~~~~~::=++++++=======
?IIIIIII777II7IIII??I===+??+++++=+++====++==+?+??==++++++=~~~:~:::==+++++=======
?III7III777777IIII???:~~=+++==========~=++==+?++?==+=++===~~~:~:+,=++++++=======
?III7III77I777IIII???:~~=++++=+====+========+?+??==+=+====~:~:~:::=++++++=======
?III7III777777IIII??+:~~=++++=+=========++==+?+??==+=++===~~~:~:::~++++++=======
?III7III777777IIII??+:~~=+++============++==+?+??==+=++===~~~:~:::=++++++=======
?III7III777777IIII??+:~~=+++============++====+??==+=++===~~~:~:::=++++++=======
?III7III777777IIII??+:~~=+++============++==??++?+?+=++===~~~:~:::=++++++=======
?III7III7777777III??+:~~=+++============++==+?++++?+=++===~~~:~:::~++++++=======
?II7IIII7777777III???:~~=+++=======+====++==?+++++?+++====~~~:~:::~++++++====?==
?III7III7777777III???:~~=+++============++==?+++++?+++====~~~:~:::=++++++=======
?III7III7777777III?I?:~~=+++=========~======+++++++++++===~~~:~:::=++++++=======
?III7IIII777I77III?II:~~=+++=======~======+++???++??~++===~~~~~:::=++++++=======
?III7IIII777I77III?II~~~=+++=======~======+++???????~++===~~==~:::=++++++=======
?II,.?I.....,,~:.........,,..,.,=======,,,,:::::.+??~++===~~~~~:::=+++++++======
"""

introGlitch4 = R"""
++++++??==~~==~~~~~:~~~~~~~~~+???++++++??+??I?7I?+???+??????I?IIII??????=+=+????
++=++===:~:,:~~~=======~~~=~~?++++++++??IIIII???+?II?IIIIIIII??$+?++++++???????I
+???=II=:~:~~~==+???+?+:~:~==$77$$ZZZZ$$$$$$$$7777777777II777$77?II77???I7$7II==
??III?==::::~~========~::~+?+7ZZOOOOOOOZZZI$OOZODDDDNMMMDOOOODDD88O$$$$$$$$$$$ZZ
??IZZOOZ$+==~=?777IIIIII?+++???IIIIIII77?I77777O77$$$$$$$77$Z$$ZOOZZZ8OOO$ZOO88O
?7I$$ZZO7+====++++???++==+?+??I=?++????7+++?????IIIII77777I7IIII$I?=~~~~::::::::
?IIZOO7I+==+++I777$OZI777$7777III7III77Z7II7II7$$$777$$7Z7777II7$II????+===+++?I
?IIZ$O77+===?+7Z777$Z$Z$7I7$777777777ZI???7777IIIIII777777IIII?I7?++++++++++++++
??IZOO77+===++??II7Z$7II??=+$7777777$$7I???I7777III7$7$77777II7$$I?I??????+??+??
=IIZ$D7I+==++=?I??7I+IIII??IIIIIIIIII7III$$7$$$$$ZZZOZOOOOOOOOOOO7$$7777777IIIII
II7OOO77++=~?+??II????I7?+?IIIII?????7III7II77III$$ZZZZZZZZZZOZO$I+???+++?$$I$I7
+?7ZO877?=+~==+?II+?I?77IIII$7I=III?I7$7777I7III?$$I$77$77777+?IIII?IIII?II?I??I
+?7ZZ8II+====+???II?II77IIIIIIIIII???$$777777I?I?I$?7777777I$$$ZZZZZOZZOZD8DD888
~====+~==~:~=++?+II?77$$?+++++?I?????$7II??I?++++$$?II???7$$ZOOOOZ7I???I?77$ZZ77
=:::::~~::::~=++++???7$$I???I?II7III?777I?II?+++=$7+????II$Z$ZZZOO7??????II777II
~::::~~:,,,,,,:::~~=~III++++???III??II7I??II++++=77+?????7$Z$ZZOOO7I+????IIIII77
=:::,:~:,,,,,,::::===Z$$I??IIIIIIIIII777IIII++++=I7?I?III7ZZZZZ8ID7?????II7III77
=:,:,:~:,,,,,,::::==+ZZ$I???IIIIIIIII77IIII7++++=77?I?III7ZZZZZOOO7?????II7III77
=:,:,,~:,,,,,,::::==?Z$$I???IIIIIIIII77IIIII++++=77?I?III7ZZZZZZOO7??????I7III77
=:,:,,~:,,,,,,::::==?Z$$I???IIIIIIIII77IIIII++++=77?I?III7ZZZZZZOO7??????I7III77
=:,:,:~:,,,,,,:::~==?Z$$I???IIIIIIIII77IIIIII7?+=77?I?III7ZZZZZOOO7?????IIIIII77
=:,:,:~:,,,,,,:::~==?OZ$I+??IIIIIIIII77IIIII+=?+++=+I?III7ZZZZZOOO7?????IIIIII77
=:,,,:~:,,,,,,,,:~==?Z$$I+??IIIIIII7777IIIII++?++++?I?III7ZZZZZOOO$?????IIIIII77
=:,,,:~:,,,,,,,::~==+OZ$I+??IIIIIII?I77IIIII+++++++???III7ZZZZZOOO$?????IIIII+77
=:,:,:~:,,,,,,,::~===ZZ$I+??IIIIIIIII77IIIII+++++++???III7ZZZZZOO87?????IIIIII77
=:,:,:~:,,,,,,,:::=:~ZZ$I+??IIIIIIII777IIIII+++++++???III7ZZZZZZOO7?????IIIIII77
=:,:,,~::,,,:,,:::=:~Z$$I+??IIIIIII$7I77II?+++=++++=$?III7ZZ$ZZOOO7?????IIIIII77
=:,:,:~:,,,,~,,::~=:~ZZ$I+??IIIIIII$77IIIII+++=++++=Z+III7ZZ7IZOOO7?????IIIIII77
=:,DN~~MMMMMD8$OMMNNNMMNN8DNNNMNIIII77I88D8888O8M++=Z+III7ZZZZZOOO7???????I7II77
"""

introGlitch5 = R"""
?+=:+?~=~==?7II=I???++??+??+??7+==+I++???+?+???+++++?????+++????7II77777II?I7==+
?+?~?77II??I777I??+=+?77=O7$$7?$7III?III++?~III7:++++I??=?II+==++=+~=+~~~:::~~~~
+~=~:,+,,,,:::::~~:::~::,,:::,:+,:::~::::::::::::~~~+::::::::::::::::::::::::~:+
?==:=::::::::::::::=:~7$$Z:::::,,::,::::~~~~~:::::::~:~~~:::::::::~::::::::::~~=
?:+=::::::::::~:~~:,,,,,,,,::~,,.,+,,,,,,,,,,,,:,..................,,,,,,,,..,::
Z:+:+:::~==:~=+~~~:::~:::::,=.,,.,,:::::..,,,,,,,,,.......,........,,,,,:~=::+~?
?~=:::::::~::~=?~?+==II7+?+7~I+,.,,,,,.,..,,,,,::,,,..,..,,......,.,,,,,:::::?==
+:?~:~+::~,~+~~+===I+$$I+??++~~,,,,,,,,,,+=,:,:~:::,:,,,,$=.:.,....,,,,,:::::+++
+=?=I::::~=+??++++II=+++?=++=:,...,:,,,,.:::I:=~~.==:~~=,~.,,......,,,,:::::=O++
,,=:+,,:~===????II7==+==+=:.:,....,.,.,,::=I+~+==+?===+===~:,~=+=~=?++????$7++++
+=$,:,:,~~==+??+II~+:=?+++,,,,.,,,,,,.=.,:==~~:===~8==~:~=:::::.,,,~~~~~===,,,,.
I=:=,:,,=+???I7I7+~====+++,,,,,,...,,,.~:==~~~+~~~??~~~~:::::...,::..,,,,,,,,,::
I=?=::,:++???III?+====+++++:,,,.,:~=.::::~=~~~~~~~$?~=~~=+:::::::::::::::::::~::
7=?=::,:++???IIII+=+==++==III?,,:,:,,.~::~=~~=~~~~I?+?:==+::::::::::::::::::::::
7+?+~:,,++???IIII???~=++++:::,,,,:,~,~::~~=~=====~I?+=7=~~:~::::::::::::::::::::
I+?+=,:,++???IIII???~==+++:~:,,,,:,,,~:::~=~====~+I?+=~=~~~::::::::::::::::::~::
I+?+=,:,++???III????~===++=~:,,:,,.::~:::,~=~===~=I?+=~=~~~~::::::::::::::::~:::
I+?+=,:,=+???III??~?=====+=~:,,,,,.~:::~:::=~~=+?+~?+===~~~~~:::::::::::::::~:::
7+?+=,:,~++??II+??=~=====+++++::,,.~~::~====~I~I?I=+?=~=~~~~~?~:::::::::::::~:::
7=?==::,~++??IIII+~=====++++++~:,:,,,:::~===~==+=?=??+==~I~~~?:::::::::::~::~:::
7=?=~::,~++?IIII?+======++++~~::,,,.,~::===~~~++~I==+?=~:::~~I::::::::::::::~:::
I+?~:,,,~++?IIII?=~==7==++++~:~~:,,,,,~~==~~~~+I?I~=~=~~:::::::::,::::::=:::::::
??+=:,,==+???II???=====+++++=+++==::,,::~=~~=?+???====~~::::~~+=:=:::::::::::::=
?I+=:,,++??IIII??+~====+++++=+++++::,.::~~~~=7???I==~=~~::::~~?::::::::::::::~::
?I++=,,++??IIII??======+++++~++:++:::.~::~~=~~=7?I==~=~~::::::?:::::::::::::::::
?I++=,,++???I??I??====++++++~~:,,,:::.~:::~=~~=7?+=~~=~~::::::::::::::::::II::~:
?I++=,,++?+?IIII??====++++++~~:,,,,:::::::==~~=7?I=+==~~::::::::::=??:::::::::::
MMMNM,:+=???IIII??~===++++++~~:,,,,D,,ZMMMM.~==7?+====DMMMMMMMI,MM.,:NMMMM::::::
MMMMMMMMMMMMMMDOOZD8OODNNMMMMM7?+:,MMMMMMMMMM..MMMMMMMMMMMMMMM:::MMMMMNMMMMMMI~O
"""

introGlitch6 = R"""
++?I++I????+===?=+++++++++++++=???+=+++++?+?+++?++?+++++++++++++====~~~===+==???
+++?+==+=++====++++?++==?:~~~~+~==+++=+++++?====I?+++=++?+==+??++?+??+?IIIIIII??
+I?II7+77IIIIIIIIIIIIIII7IIII7I?IIIIIIIIIIIIIIIIIIII?IIIIIIIIIIIIIIIIIIIIIIII?I+
+??I?IIIIIIIIIIIIII?II=~~:IIIII77IIIIIII?II??IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII??
+I??IIIIIIIIIIIIIII7II7777IIII7777?777777777777I777777777777777777777777777777II
:I+I+IIII??II??IIIIIIIIIIIII?777777IIIII7777777777777777777777777777777III?II+?+
+I?IIIIIIIIIII?+I++??++=?+?=I=+7777777777777777II7777777777777777777777IIIIII+??
+I+III+III7I???+???+?~~=+++?+?I7777777777+?IIIIIIII7I7777~?7I7I77777777IIIIII+?+
+?+?=IIII??++++++?=+?++++????I77777I77777III=I?I?7??I?I?7I777777777777IIIIII?:++
I7?I?77II???++++===???????I7I77777777777II?=+????++???+???III????I?+++++++~=++++
+?~7IIII????++++==??I?+?+?I77I77777777?77I????I????,??III?IIIII77I7?I?I????77777
=?I?II77?++++====?I????+++I777777777777?I?????+?I?++I??IIIIII7777II777777II77III
=?+?II7I+?+++=++++???????++II777III?7IIIII?II?????~+??II?+IIIIIIIIIIIIIIIIIIIIII
~?+?II7I+?+++====+????++??===+77I7I7I7IIII?I??????=+++I??+IIIIIIIIIIIIIIIIIIIIII
=?+?II7I+++++====+++???+++III7777III7IIIII????????=++?=??IIIIIIIIIIIIIIIIIIIIIII
=++??III+++++=++++++???+++IIII777II77IIIII???????+=++????IIIIIIIIIIIIIIIIIIIIIII
=++??II7+++++===++++?????+?II77II77II?IIIII???????=++????IIIIIIIIIIIIIIIIIIIIIII
=?+??II7?++++===++?+?????+?II77I7I7?IIIIIII????+++?++????III?IIIIIIIIIIIIIIIIIII
=?+??II7??+++==?++???????++++?IIII7IIIII?????=?=+=?++????IIII+IIIIIIIIIIIIIIIIII
=?+??II7?++++===+???????++++++II7I777III???????+?+?++????=III+IIIIIIIIIIIIIIIIII
=?+?III7??++===++???????++++IIIII777IIII????????I=??++?IIIIII=IIIIIIIIIIIIIIIIII
=?+?III7??+++===+????=???++?IIIII7I777II?????I?=++??????IIIIIIIII7IIIIII?IIIIIII
+++?III???+++=++++?????+?+++??++??III7II?????+++++????IIIIIIII+?I?IIIIIIIIIIIII?
+=??I77+?+++===+++??????++++??++++II77IIII???=+++=??I?IIIIIIII+IIIIIIIIIIIIIIIII
+=++?77+?+++=+=++??????+++++I?+I+?III7IIII?????=++??I?IIIIIIII+IIIIIIIIIIIIIIIII
+=++?77+++++=++=++????++++++III77IIII7?III?????=++????IIIIIIIIIIIIIIIIIIII==IIII
+=++?7I+?+++=+++++????++++++IIII7IIIIIIIII?????=+=????IIIIIIIIIIII?++IIIIIIIIIII
.....7I+?+++====++????++++++IIII7I7,77~....7I??=++????,.......=7..7II.....IIIIII
..............,:::,,::,,,.....=++II..........77...............III............=I:
"""



#script
#! DEBUG !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#witness_rapture()
#play_colCave_intro1()
#play_colCave_intro2("John")