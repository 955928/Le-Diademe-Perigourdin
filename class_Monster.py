import random

class Monster:
    def __init__(self,):

        self.monster = random.choice(["Goblin", "Minotaur", "Titan"])


        if self.monster == "Titan":
            self.level = 10
            self.health = 200
            self.attack = 40
            self.has_tiara = True
            print("Oh tremble in the presence of the notorius Titan")



        elif self.monster == "Minotaur":
            self.health = 150
            self.level = 5
            self.attack = 15
            self.has_tiara = False
            print("The Minotaur has arisen!Beware of his might!")

        else:
            self.health = 30
            self.level = 1
            self.attack = 5
            self.has_tiara = False
            print("You are now facing a Goblin")


    def get_attack(self,attack):

        self.attack = attack
        print(f"The {self.monster} has inflicted{self.attack} points in damages")


    def get_damage(self):

        self.health -= self.attack
        
        if self.health == 0:
            print(f"After having suffered {self.attack} the {self.monster} now has {self.health} points in health")
            print(f"Victory!The {self.monster} has been defeated")
            
            
            if "Titan" in self.monster == 0:
                print("The Titan has left behind the infamous Tiara of Perigourdin")
                
            else:
                print("Goodluck little one")
            

        else:
            print(f"After having suffered {self.attack} the {self.monster} now has {self.health} points in health")
            
    



monster_1 = Monster(150,10)



print(monster_1.monster)
print(monster_1.health)
print(monster_1.level)
print(monster_1.has_tiara)



    