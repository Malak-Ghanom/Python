from game_character import GameCharacter
from medic import Medic
from warrior import Warrior
from explorer import Explorer
from datetime import datetime
import sys
import csv
import re
from random import randint

#Variables:
life = True
round = 1

#insert names of teams
name1 = input("TEAM (1) please insert the team name: ").upper()
name2 = input("TEAM (2) please insert the team name: ").upper()

#select which charcter do you want and call the function that shows the ability of the chosen character
def choose_character(name,team1,team2):

    char = int(input(f"\033[1;33;40m>> Round: ({round})\033[1;37;40m\n{name}'s turn Choose one of the following character:\n1- {team1[0].name}\n2- {team1[1].name}\n3- {team1[2].name}\nwhat do you want to choose: "))
    return choose_ability(char, team1, team2, name)


#shows and select ability of a specific char and call the function that force the abilities
def choose_ability(char, team1, team2, name):

    if char == 1 :
        print(f"\nyou have chosen worrior \033[1;33;40m'{team1[0].name}'\033[1;37;40m to play this round\n")
        print(f"\033[1;33;40m'{team1[0].name}' can do the following:\033[1;37;40m\n1- attack\n2- cast a spell\n3- buy armor\n4- share intelligence\n5- stun opponent")
        ability = int(input("Choose of the above options: "))
        warrior_ability(ability, team1, team2, name)

    elif char == 2 :
        print(f"you have chosen medic '{team1[1].name}' to play this round\n")
        print(f"\033[1;33;40m'{team1[1].name}' can do the following:\033[1;37;40m\n1- heal\n2- cast a spell\n3- back to future\n4- stun opponents and attack them")
        ability = int(input("Choose of the above options: "))
        medic_attack(ability, team1, team2, name)

    elif char == 3 :
            print(f"you have chosen worrior '{team1[2].name}' to play this round\n")
            print(f"\033[1;33;40m'{team1[2].name}' can do the following:\033[1;37;40m\n1- search for gold\n2- cast a spell\n3- Inforced Explorer to search for gold (-10 health)")
            ability = int(input("Choose of the above options: "))
            explorer_attack(ability,team1,team2,name)
    

#the whole abilities for worrior 
def warrior_ability(ability, team1, team2, name):
    #attack
    if ability == 1:
        opponent = int(input(f'\n\033[1;33;40mWhich opponent do you wish to attack?\033[1;37;40m \n1- {team2[0].name}\n2- {team2[1].name}\n3- {team2[2].name}\nChoose opponent: '))

        if opponent == 1:
            team1[0].attack(team2[0])
        if opponent == 2:
            team1[0].attack(team2[1])
        if opponent == 3:
            team1[0].attack(team2[2])
    #cast a spell on
    elif ability == 2:
        opponent = int(input(f'\n\033[1;33;40mWhich opponent do you wish to cast a spell on?\033[1;37;40m \n1- {team2[0].name}\n2- {team2[1].name}\n3- {team2[2].name}\nChoose opponent: '))    
        if opponent == 1:
            team1[0].cast_spell_on(team2[0])
        if opponent == 2:
            team1[0].cast_spell_on(team2[1])
        if opponent == 3:
            team1[0].cast_spell_on(team2[2])
    #buy armor
    elif ability == 3:
        if team1[2].get_gold() > 0:
            member = int(input(f'\n\033[1;33;40mWhich member do you wish to buy armor for it:\033[1;37;40m \n1- {team1[0].name}\n2- {team1[1].name}\n3- {team1[2].name}\nChoose member: '))
            if member == 1:
                team1[0].buy_armor(team1[2],team1[0])
            if member == 2:
                team1[0].buy_armor(team1[2],team1[1])
            if member == 3:
                team1[0].buy_armor(team1[2],team1[2])
        else:
            print("\n\033[1;31;40mThere is no enough gold\033[1;37;40m\n")
            return choose_ability(team1[0], team1, team2, name)
    #share intelligence
    elif ability == 4:
        team1[0].share_intelligence(team1[2])        
    #stun opponent and increase members healths
    elif ability == 5:
        team1[0].stun_opponents(team1,name)


#the whole abilities for medic
def medic_attack(ability, team1, team2, name):

    #heal
    if ability == 1:
        member = int(input(f'\n\033[1;33;40mWhich member do you wish to heal him?\033[1;37;40m \n1- {team1[0].name}\n2- {team1[1].name}\n3- {team1[2].name}\nChoose member: '))
        if member == 1:
            team1[1].heal(team1[0])
        if member == 2:
            team1[1].heal(team1[1])
        if member == 3:
            team1[1].heal(team1[2])

    #cast a spell
    elif ability == 2:
        opponent = int(input(f'\n\033[1;33;40mWhich opponent do you wish to cast a spell on him?\033[1;37;40m \n1- {team2[0].name}\n2- {team2[1].name}\n3- {team2[2].name}\nChoose opponent: '))    
        if opponent == 1:
            team1[1].cast_spell_on(team2[0])
        if opponent == 2:
            team1[1].cast_spell_on(team2[1])
        if opponent == 3:
            team1[1].cast_spell_on(team2[2])

    #back to the furure
    elif ability == 3:
        today = datetime.now()
        micro = today.microsecond
        team1[1].back_to_the_future(micro)

    #stun opponent to decrease their health
    elif ability == 4:
        team1[1].stun_opponents(team1,team2,name)


#the whole abilities for explorer
def explorer_attack(ability, team1, team2, name):
    #go on guest
    if ability == 1:        
        treasure_maps = open("D:\\python\\PA03\\treasure_maps.txt", "r")  #read file      
        map =[]
        for line in treasure_maps:
            line = re.sub("]|[|[|]|\n|,|''|'| |",'', line) #extract useless sympols
            for char in line:
                map.append(char)  #append remaining

        maps = []
        #append all maps togther
        for i in range(6): #number of maps
            sub_map = [[map[x] for x in range (4)] for y in range(4)] 
            del map[0:4]
            maps.append(sub_map) 
        x,y = randint(0,3),randint(0,3)
        position = (x,y)
        map_index = randint(0,5)
        team1[2].go_on_quest( maps[map_index] , position, team1)
    #cast a spell
    elif ability == 2:
        opponent = int(input(f'\n\033[1;33;40mWhich opponent do you wish to cast a spell on him?\033[1;37;40m \n1- {team2[0].name}\n2- {team2[1].name}\n3- {team2[2].name}\nChoose opponent: '))    
        if opponent == 1:
            team1[2].cast_spell_on(team2[0])
        if opponent == 2:
            team1[2].cast_spell_on(team2[1])
        if opponent == 3:
            team1[2].cast_spell_on(team2[2])
    #inforce explorer to go on quest if the foresight level = 0
    elif ability == 3:
        team1[2].set_foresight_level(1)
        team1[2].health-=10
        return explorer_attack(1,team1,team2,name)


#check if any of the char die to end the game (health of char = 0)
def check_death (name1, name2, team1, team2):
    global life
    #check if any member of team (1) die
    if team1[0].health == 0 or team1[1].health == 0 or team1[2].health == 0:                  
        print(f"\n\n\t\tGame Over : \N{grinning face} \033[1;36;41m *** {name1} Vectory ***\033[1;37;40m\N{grinning face}\n\n")
        sys.exit()

    #check if any member of team (2) die
    elif team2[0].health == 0 or team2[1].health ==0 or team2[2].health == 0:            
        print(f"\n\n\t\tGame Over : \N{grinning face} \033[1;36;41m *** {name2} Vectory ***\033[1;37;40m\N{grinning face}\n\n")            
        sys.exit()


#after the rounds end the team who has the highest sum of thier healths will win the game
def chech_winner(name1, name2, team1 , team2):
    sum_health_team1 = 0
    for i in range(0,3):
        sum_health_team1 += team1[i].health
    
    sum_health_team2 = 0
    for i in range(0,3):
        sum_health_team2 += team2[i].health

    print(f"\n\033[1;33;40mHealth of {name1} = {sum_health_team1}")
    print(f"Health of {name2} = {sum_health_team2}\033[1;37;40m")

    if sum_health_team1 > sum_health_team2:
        print(f"\n\t\tGame Over : \N{grinning face} \033[1;36;41m *** {name1} Vectory ***\033[1;37;40m\N{grinning face}\n\n")
    else:
        print(f"\n\n\t\tGame Over : \N{grinning face} \033[1;36;41m *** {name2} Vectory ***\033[1;37;40m\N{grinning face}\n\n")


if __name__ == "__main__":
    print('\n\n\n\t\t\t\033[1;34;40m-----------------------------------')
    print('\t\t\t|\033[1;33;40m A new BoT game has been started \033[1;34;40m|')
    print('\t\t\t-----------------------------------\n\n\033[1;37;40m')
    
    # team 1 : get ready
    print(f"\033[1;35;40m{name1} Vectory\033[1;37;40m")
    warrior1 = Warrior('W1',100,20,50,0)
    medic1 = Medic('M1',100,20,50)
    explorer1 = Explorer('E1',100,20,50)

    # team 2 : get ready
    print(f"\033[1;35;40m{name2} Vectory\033[1;37;40m")
    warrior2 = Warrior('W2',100,20,0,50)
    medic2 = Medic('M2',100,20,50)
    explorer2 = Explorer('E2',100,20,50)
    
    #charactars list contain the characters of team 1
    chars1 = [warrior1,medic1,explorer1]
    #charactars list contain the characters of team 2
    chars2 = [warrior2,medic2,explorer2]
    
    for i in range(0,5):
        #chech if there is a die char
        check_death(name1, name2, chars1, chars2)

        choose_character(name1, chars1, chars2)
        round += 1
        choose_character(name2, chars2, chars1)

    chech_winner(name1, name2, chars1, chars2)