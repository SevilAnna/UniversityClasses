#   EMÜ 112 - Homework #4: Maze Game

import random

class Characters:                   # creates class for physicists
    def __init__(self,name,spock,lizard,rock,paper,scissors,health,speech="Default"):
        self.__name = name
        self.__health = health
        self.__spock = spock
        self.__lizard = lizard
        self.__rock = rock
        self.__paper = paper
        self.__scissors = scissors
        self.__speech = speech
    def __str__(self):
        myspeech = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"\
                   "\n\t\t" + self.__speech + "\n\t\t   -- " + self.__name + "\n" \
                   "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        return myspeech
    def check_name(self):           # they return the name, health, or move percentages
        return self.__name
    def check_health(self):
        return self.__health
    def percentage_spo(self):
        return self.__spock
    def percentage_liz(self):
        return self.__lizard
    def percentage_rock(self):
        return self.__rock
    def percentage_pap(self):
        return self.__paper
    def percentage_sci(self):
        return self.__scissors
    def take_damage(self):          # subtracts 50 health when they lose the round
        self.__health = self.__health - 50

speech_F = '"I\'m smart enough to know that I\'m dumb."'
class Feynman (Characters):
    def __init__(self,name="Richard Feynman",spock=20,lizard=40,rock=60,paper=80,scissors=100,health=100):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_F)
speech_C = '"I never see what has been done; I only see what remains to be done."'
class Curie(Characters):
    def __init__(self,name="Marie Curie",spock=35,lizard=70,rock=80,paper=90,scissors=100,health=90):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_C)
speech_S = '"The present is the only things that has no end."'
class Schrodinger (Characters):
    def __init__(self,name="Erwin Schrödinger",spock=10,lizard=45,rock=80,paper=90,scissors=100,health=80):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_S)
speech_D = '"Pick a flower on Earth and you move the farthest star."'
class Dirac (Characters):
    def __init__(self,name="Paul Dirac",spock=10,lizard=20,rock=55,paper=90,scissors=100,health=70):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_D)
speech_N = '"We built too many walls and not enough bridges."'
class Newton (Characters):
    def __init__(self,name="Isaac Newton",spock=10,lizard=20,rock=30,paper=65,scissors=100,health=60):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_N)
speech_P = '"Why did the chicken cross the road? There already was a chicken on this side of the road."'
class Pauli (Characters):
    def __init__(self,name="Wolfgang Pauli",spock=35,lizard=45,rock=55,paper=65,scissors=100,health=50):
        Characters.__init__(self,name,spock,lizard,rock,paper,scissors,health,speech=speech_P)


initialhealth = 200         # character's original health.
# later on, 'herohealth' is returned from function to function in order to keep it consistent

initialmaze = ([" "," "," "," "," "," "," "," "," "," "," "],   # 0     indexes
               [" "," ", 1, 2, 3," ",4, 5, 6, " "," "],         # 1
               [" ", 7,  0, 0, 0, 0, 0, 0, 0, 8,  " "],         # 2
               [" ", 9,  0, 0, 0, 0, 0, 0, 0, 10, " "],         # 3
               [" ", 11, 0, 0, 0, 0, 0, 0, 0, 12, " "],         # 4
               [" "," ", 0, 0, 0,"X",0, 0, 0, " "," "],         # 5
               [" ", 13, 0, 0, 0, 0, 0, 0, 0, 14, " "],         # 6
               [" ", 15, 0, 0, 0, 0, 0, 0, 0, 16, " "],         # 7
               [" ", 17, 0, 0, 0, 0, 0, 0, 0, 18, " "],         # 8
               [" "," ",19,20,21," ",22,23,24," "," "],         # 9
               [" "," "," "," "," "," "," "," "," "," "," "])   # 10
#                0   1   2  3  4  5  6  7  8  9   10

mazelayout = list(initialmaze)


def whichPhysicist():               # randomly chooses a physicist to be placed in each '0 tile' in the map above
    n = random.randint(1,6)
    if n == 1:
        return "F"  # Feynman
    elif n == 2:
        return "C"  # Curie
    elif n == 3:
        return "S"  # Schrödinger
    elif n == 4:
        return "D"  # Dirac
    elif n == 5:
        return "N"  # Newton
    else:
        return "P"  # Pauli

thelist = [0,"X"," ","F","C","S","D","N","P"]
def startingmap():                          # generates the first version of the map and prints it
    dummy = input("press any key to continue...")
    print("________________________________________________________________________________\n")
    S = random.randint(1, 24)               # random number to select one of the 24 S's
    #print("S:", S)
    a = 0
    for n in mazelayout:                    # checks each 'tile' in the map
        for i in range(0, 11):              # places physicists on the '0 tiles'
            if mazelayout[a][i] == 0:
                mazelayout[a][i] = whichPhysicist()
            # print(n[i],end=" ")
        # print()
        b = 0
        for m in n:
            if m == S:                      # Checks for the randomly selected number (S)
                mazelayout[a][b] = "ㅊ"     # and places the character (ㅊ) on the selected S.
            elif m not in thelist:          # Otherwise, checks to make sure selected tile is not a physicist etc
                mazelayout[a][b] = " "      # and then makes those tiles empty - for cleaner game visuals
            b += 1
        a += 1
    for n in mazelayout:                    # prints the map
        for i in range(0, 11):
            print(n[i], end="\t")
        print()

def location():                             # prints the current map
    print("________________________________________________________________________________\n")
    for n in mazelayout:
        for i in range(0, 11):
            print(n[i], end="\t")
        print()

def sillydirection():                   # text is displayed when wrong direction is entered. prompted to enter sth else
    print("\n\t ㅊ  <(   I can't move there, silly! Choose again.   )\n")
    new_input = input("\tinput >>>  ")
    return new_input

def moving(move_input):                     # moves the character depending on the input received.
    flag = True
    i = 0
    while i < 11 and flag == True:
        j = 0
        while j < 11 and flag == True:
            if mazelayout[i][j] == "ㅊ":
                mazelayout[i][j] = "-"              # replaces old path with "-"
                if move_input == "U":
                    mazelayout[i - 1][j] = "ㅊ"
                    flag = False
                elif move_input == "D":
                    mazelayout[i + 1][j] = "ㅊ"
                    flag = False
                elif move_input == "R":
                    mazelayout[i][j + 1] = "ㅊ"
                    flag = False
                elif move_input == "L":
                    mazelayout[i][j - 1] = "ㅊ"
                    flag = False
            j += 1
        i += 1

def check_enemy(move_input,herohealth):     # checks which physicist there is in the tile we're moving to now
    flag = True                             # also displays their speech
    i = 0
    while i < 11 and flag == True:
        j = 0
        while j < 11 and flag == True:
            if mazelayout[i][j] == "ㅊ":     # checks where character is and then which way we're going
                if move_input == "U":
                    physicist = str(mazelayout[i - 1][j])       # assign the physicist's letter
                    flag = False
                elif move_input == "D":
                    physicist = str(mazelayout[i + 1][j])
                    flag = False
                elif move_input == "R":
                    physicist = str(mazelayout[i][j + 1])
                    flag = False
                elif move_input == "L":
                    physicist = str(mazelayout[i][j - 1])
                    flag = False
            j += 1
        i += 1
    if physicist != "X":                # if the character didn't reach the end yet
        if physicist == "F":
            character = Feynman()
            print(character.__str__())  # displays the physicist's speech
        elif physicist == "C":
            character = Curie()
            print(character.__str__())
        elif physicist == "S":
            character = Schrodinger()
            print(character.__str__())
        elif physicist == "D":
            character = Dirac()
            print(character.__str__())
        elif physicist == "N":
            character = Newton()
            print(character.__str__())
        elif physicist == "P":
            character = Pauli()
            print(character.__str__())
        herohealth = battle(character,herohealth)
    return herohealth

def sillymove():            # text is displayed when non-existent move is entered. prompted to enter sth else
    print("\n\t ㅊ  <(   What? That's not a move, don't be silly! What should I choose?    )\n")
    move = input("\t\t1 --> Spock\t\t2 --> Lizard\n\t\t3 --> Rock\t\t"
                 "4 --> Paper\n\t\t5 --> Scissors\n\n\tinput >>>  ")
    print("\n________________________________________________________________________________\n\n")
    return move

def enemymovechoice(character):         # randomly selects a move for physicists
    p1 = character.percentage_spo()
    p2 = character.percentage_liz()
    p3 = character.percentage_rock()
    p4 = character.percentage_pap()
    p5 = character.percentage_sci()
    num = random.randint(1,100)
    if num <= p1:
        return "1"
    elif num <= p1 + p2:
        return "2"
    elif num <= p1 + p2 + p3:
        return "3"
    elif num <= p1 + p2 + p3 + p4:
        return "4"
    else:
        return "5"

def movecomparing(herohealth,move,character):   # compares our move with that of the physicist
    enemymove = enemymovechoice(character)
    if move == "1":                 # spock
        if enemymove == "1":          # vs spock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Spock too! It's a tie!   )")
        elif enemymove == "2":        # vs lizard
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Lizard! Ouch!   )")
            herohealth -= 50
        elif enemymove == "3":        # vs rock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Rock! Yay!   )")
            character.take_damage()
        elif enemymove == "4":        # vs paper
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Paper! Ouch!   )")
            herohealth -= 50
        elif enemymove == "5":        # vs scissors
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Scissors! Yay!   )")
            character.take_damage()
    if move == "2":                 # lizard
        if enemymove == "1":          # vs spock
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Spock! Yay!   )")
            character.take_damage()
        elif enemymove == "2":        # vs lizard
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Lizard too! It's a tie!   )")
        elif enemymove == "3":        # vs rock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Rock! Ouch!   )")
            herohealth -= 50
        elif enemymove == "4":        # vs paper
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Paper! Yay!   )")
            character.take_damage()
        elif enemymove == "5":        # vs scissors
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Scissors! Ouch!   )")
            herohealth -= 50
    if move == "3":                 # rock
        if enemymove == "1":          # vs spock
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Spock! Ouch!   )")
            herohealth -= 50
        elif enemymove == "2":        # vs lizard
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Lizard! Yay!   )")
            character.take_damage()
        elif enemymove == "3":        # vs rock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Rock too! It's a tie!   )")
        elif enemymove == "4":        # vs paper
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Paper! Ouch!   )")
            herohealth -= 50
        elif enemymove == "5":        # vs scissors
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Scissors! Yay!   )")
            character.take_damage()
    if move == "4":                 # peper
        if enemymove == "1":          # vs spock
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Spock! Yay!   )")
            character.take_damage()
        elif enemymove == "2":        # vs lizard
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Lizard! Ouch!   )")
            herohealth -= 50
        elif enemymove == "3":        # vs rock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Rock! Yay!   )")
            character.take_damage()
        elif enemymove == "4":        # vs paper
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Paper! It's a tie!   )")
        elif enemymove == "5":        # vs scissors
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Scissors! Ouch!   )")
            herohealth -= 50
    if move == "5":                 # scissors
        if enemymove == "1":          # vs spock
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Spock! Ouch!   )")
            herohealth -= 50
        elif enemymove == "2":        # vs lizard
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Lizard! Yay!   )")
            character.take_damage()
        elif enemymove == "3":        # vs rock
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Rock! Ouch!   )")
            herohealth -= 50
        elif enemymove == "4":        # vs paper
            print("\n\t ㅊ  <(   ", character.check_name(), " chose Paper! Yay!   )")
            character.take_damage()
        elif enemymove == "5":        # vs scissors
            print("\n\t ㅊ  <(   ",character.check_name() , " chose Scissors too! It's a tie!   )")

    if herohealth > 0 and character.check_health() <= 0:    # if physicist loses all health
        print("\n\t ㅊ  <(   We won!   )")
    if herohealth <= 0 and character.check_health() > 0:    # if hero loses all health
        print("\n\t ㅊ  <(   We lost!   )")
    if character.check_health() < 0:                        # hero gains health if physicist's health < 0
        gainedhealth = ( - character.check_health())
        herohealth += gainedhealth
        print("\n\t ㅊ  <(   We also gained ", gainedhealth, " health! Cool!   )")
        #print(herohealth)
    elif character.check_health() == 0:
        print("\n\t ㅊ  <(   We didn't gain any health this time.   )")
    return herohealth

movelist = ["1","2","3","4","5"]    # moves. 1-spock, 2-lizard, 3-rock, 4-paper, 5-scissors
def battle(character,herohealth):   # battle simulation
    print("\n\t ㅊ  <(   We're fighting " , character.check_name() , "!   )")
    print("\n\t ㅊ  <(   So, our health is",herohealth,"and theirs is",character.check_health(),
          ". Which attack should I choose?   )\n")
    move = input("\t\t1 --> Spock\t\t2 --> Lizard\n\t\t3 --> Rock\t\t"
                 "4 --> Paper\n\t\t5 --> Scissors\n\n\tinput >>>  ")
    print("\n________________________________________________________________________________\n\n")
    while move not in movelist:                                 # in case a non-move is entered
        move = sillymove()
    herohealth = movecomparing(herohealth,move,character)       # compares the moves, assigns new health
    while herohealth > 0 and character.check_health() > 0:      # loops as long as both are still alive
        print("\n\t ㅊ  <(   So, our health is",herohealth,"and theirs is",character.check_health(),
          ". Which attack should I choose next?   )\n")
        move = input("\t\t1 --> Spock\t\t2 --> Lizard\n\t\t3 --> Rock\t\t"
                     "4 --> Paper\n\t\t5 --> Scissors\n\n\tinput >>>  ")
        print("\n________________________________________________________________________________\n\n")
        while move not in movelist:                             # in case a non-move is entered
            move = sillymove()
        herohealth = movecomparing(herohealth,move,character)   # compares the moves, assigns new health
    dummy = input()
    return herohealth

def movement(herohealth):                             # receives input, then moves character & battles accordingly
    print("\n\t ㅊ  <(   Which way should I go?   )\n")
    move_input = input("\t\tU --> Up\t\tD --> Down\n\t\tR --> Right\t\tL --> Left\n\n\tinput >>>  ")    # input
    silly = True
    to_move = True
    while silly:            # loops until the input is correct and we finish battling one physicist
        a=0
        for i in mazelayout:
            b=0
            for j in i:
                if j == "ㅊ" and to_move:                    # finds character on the map
                    if move_input == "U":
                        if mazelayout[a-1][b] == " ":        # prevents the character from leaving the map
                            move_input = sillydirection()
                        else:                                # if they moved to a physicist, then
                            herohealth = check_enemy(move_input,herohealth)     # battle them, assign health
                            moving(move_input)               # move character to the defeated physicist's tile
                            to_move = False                  # we moved. end the loop
                            silly = False                    # we finished entering all inputs for now. end the loop
                    elif move_input == "D":
                        if mazelayout[a+1][b] == " ":           # same as above
                            move_input = sillydirection()
                        else:
                            herohealth = check_enemy(move_input,herohealth)
                            moving(move_input)
                            to_move = False
                            silly = False
                    elif move_input == "R":
                        if mazelayout[a][b+1] == " ":           # same as above
                            move_input = sillydirection()
                        else:
                            herohealth = check_enemy(move_input,herohealth)
                            moving(move_input)
                            to_move = False
                            silly = False
                    elif move_input == "L":
                        if mazelayout[a][b-1] == " ":           # same as above
                            move_input = sillydirection()
                        else:
                            herohealth = check_enemy(move_input,herohealth)
                            moving(move_input)
                            to_move = False
                            silly = False
                    else:                       # if we don't input one of the directions
                        print("\n\t ㅊ  <(   I don't understand... Choose again.   )\n")
                        move_input = input("\t\tU --> Up\t\tD --> Down\n\t\tR --> Right\t\tL --> Left\n\n\tinput >>>  ")
                b+=1
            a+=1
    return herohealth

def main():         # main function
    print("\n ~~~\tWelcome to the Maze Game! Playing on fullscreen is recommended\t~~~\n\n")
    yourname = input("\tEnter your OWN name: \t")
    heroname = input("\tEnter the HERO's name: \t")
    print("________________________________________________________________________________\n\n")
    print("\n\t ㅊ  <(   Hi, I'm ",heroname,"! Let's go on an adventure together!   )\n")
    startingmap()
    print("\n\t ㅊ  <(   So ",yourname,", I'm trying to reach the center X, but as you can see \n"
          "\t\t\t  I'm a little flat-headed and I need your help with deciding!       )")       # haha so punny
    herohealth = movement(initialhealth)
    #print("Health: ", herohealth)
    flag_X = True
    while flag_X and herohealth > 0:    # loop until we reach X or die (so dramatic)
        location()
        herohealth = movement(herohealth)
        #print("Health: ", herohealth)
        flag_X = False
        for n in mazelayout:
            for m in n:
                if m == "X":            # when we reach the center X
                    flag_X = True
    print("________________________________________________________________________________\n\n")
    if herohealth > 0:      # the end
        print("\n\t ㅊ  <(   Wow ",yourname,"! We did it! Thank you for helping me!   )\n")


main()