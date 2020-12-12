from game_character import GameCharacter
from random import randint
from explorer import Explorer
from time import sleep


class Warrior(GameCharacter):

    def __init__(self, name, health, attack_max, magic,popularity):     

        super().__init__(name, health, attack_max, magic)

        print(f"\033[1;33;40m{self.name}\033[1;37;40m is ready to fight! ")

        self.popularity = popularity        


# This method issues a command to buy armor for a given team member.
# A random shield value between 0% - 20% is returned
    def buy_armor(self, explorer, member):

        if member.health<100: 
            if explorer.get_gold() > 0:     
                shield = randint(0,20)              
                member.health = member.health + shield     
                self.popularity += 1
                explorer.set_gold(-1)
            else:
                print("\nsorry, there is no gold with explorer :( \nChoose another ability\n")
        else:
            member.health = 100
            member.set_strength(member.get_strength()+5)
            print(f"The strength of {member.name} increased to {member.get_strength()}\n")
        
#increases the explorer's foresight level by 1/10th of the warrior's popularity level
    def share_intelligence(self,member):
        print(f"The foresight level of the '{member.name}' increased from ({member.foresight}) to ({member.foresight+self.popularity * 0.1})\n")
        member.increase_foresight(self.popularity * 0.1)

#stun opponent and increase team healths
    def stun_opponents(self, team1, name):
        print(f"\nStun opponents for 10 sec, and increase {name} health by 5.")
        sleep(10)
        for i in range(0,3):
            team1[i].health += 5
        for i in range(0,3):
            print(f"health of ({team1[i].name}) = {team1[i].health}")
        print("")