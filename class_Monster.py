import random

class Monster:
    
    def __init__(self):

        self.monster = random.choice(["Goblin", "Minotaur", "Titan"])


        if self.monster == "Titan":
            self.level = 10
            self.health = 200
            self.attack = 20
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
            self.attack = 10
            self.has_tiara = False
            print("You are now facing a Goblin")



    def get_attack(self, name):

    def get_attack(self, hero):


        hero.health -= self.attack
        
        print(f"The {self.monster} has inflicted{self.attack} points in damages")


    def get_damage(self, name):
       

        self.health -= name.attack
        
        
        if self.health == 0:
            if self.health in "Titan" in self.monster:
                print("The Titan has left behind the infamous Tiara of Perigourdin")
                
            else:
                print("Goodluck little one")
            
            print(f"After having suffered {name.attack} points in damages, the {self.monster} now has {self.health} points in health")
            print(f"Victory!The {self.monster} has been defeated")
            


        else:
            
            print(f"After having suffered {self.attack} the {self.monster} now has {self.health} points in health")
            
    def is_dead(self):
        if self.health > 0:
            print (f"{self.monster} has {self.health} health points - He is alive and can fight back Jake")
        else:
            print(f"{self.monster} is dead... Jake is the best")



monster_1 = Monster()




# print(monster_1.monster)
# print(monster_1.health)
# print(monster_1.level)
# print(monster_1.has_tiara)



    