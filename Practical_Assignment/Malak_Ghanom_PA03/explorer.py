from game_character import GameCharacter
from time import sleep

class Explorer(GameCharacter):

    def __init__(self, name, health, attack_max, magic):

        super().__init__(name, health, attack_max, magic)

        print(f"Commander \033[1;33;40m'{self.name}'\033[1;37;40m at your service.\n")

        self.gold = 50
        self.foresight = 0

    
    def set_gold(self,number):
        self.gold += number

    def get_gold(self):
        return self.gold

    def set_foresight_level(self,number):
        self.foresight += number

    def get_foresight_level(self):
        return self.foresight    

#search for gold for a given map (go_on_quest)
    def go_on_quest(self, map, position, team1):

        #if the foresight level is zero -> can't search
        if self.foresight == 0:
            print("\n\033[1;31;40msorry, Explorer can't search for gold right now.\n\033[1;37;40m")
        else:
            #replace the random position with 'E'            
            print(f"\n\033[1;33;40m{team1[2].name} is now searching for gold in the following map:\033[1;37;40m\n")
            map[position[0]][position[1]]='E'
            for row in map:
                print(row)
            #Delay for searching
            for second in range(5):
                sleep(1)
                print('\033[1;33;40m. ', end="")
            #counting the number of gold in a random map
            count=0
            for row in map:
                for colm in row:
                    if colm == '$':
                        count += 1
            print(f'process completed (found {count} peices of gold)\033[1;37;40m\n') 
            #decrease number of foresight level
            self.set_foresight_level(-1)
               


        