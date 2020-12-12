from game_character import GameCharacter
from datetime import datetime
from time import sleep
import random

class Medic(GameCharacter):

    def __init__(self, name, health, heal, magic):

        super().__init__(name, health, heal, magic)

        print(f"Your medic \033[1;33;40m{self.name}\033[1;37;40m, to the rescue!")

        self.nanobots = 10
        self.nanobots_accuracy_level = 0

#heal
    def heal(self, character):
        heal_value = (random.randrange(self.strength - 10 , self.strength + 10)/10)
        print(f"> {self.name} is healing {character.name}. {(heal_value)}\n")

        if character.get_health() + heal_value > character.max_health:
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)

        return heal_value
#attack
    def attack(self, character):
        self.heal(character)

#The medic travels in time to retrieve advanced nanobots that help the medic heal other characters more efficiently
    def back_to_the_future(self,future):
        sleep(0.214565)
        today = datetime.now()
        micro = today.microsecond
        print(f"\nThe nanobots available to heal increased from ({self.nanobots})", end="")
        self.nanobots += abs(micro-future)
        self.nanobots_accuracy_level += 1
        print(f" to ({self.nanobots})\nAccuracy level for nanobots = {self.nanobots_accuracy_level}\n")

#stun opponent and decrease their healths
    def stun_opponents(self, team1, team2, name):
        print(f"\nStun opponents for 10 sec, and decrease {name}'s health.")
        sleep(10)
        for i in range(0,3):
            team1[1].attack(team2[i])
        
        print(f"\n\033[1;33;40mHealths of opponents after the stun is:\033[1;37;40m")
        for i in range(0,3):
            print(f"({team2[i].name}) = {team2[i].health}")
        print("")
        