import random

class Monster:
    def __init__(self, health, level):

        self.monster = random.choice(["Goblin", "Minotaur", "Titan"])
        self.health = health
        self.level = level
        

        random.choice(self.monster)
        
      
        
        if self.monster == "Titan":
            self.level = 10
            self.attack = 40
            self.has_tiara = True
            print("Oh tremble in the presence of the notorius Titan")
    
            
            if self.health == 0:
                print("The TiTan has left behind the infamous Tiara of Perigourdin ")
    
            else:
                print("Good luck little one!Try again")

            
        
        elif self.monster == "Minotaur":
            self.level = 5
            self.attack = 15
            self.has_tiara = False
            print("The Minotaur has arisen!Beware of his might!")
        
        else:
            self.level = 1
            self.attack = 5
            self.has_tiara = False
            print("You are now facing a Goblin")
             
        
    def get_attack(self,attack):
        
        self.attack = attack
        print(f"The {self.monster} has inflicted{self.attack} points in damages")
    
        
    def get_damage(self):
        
        self.health -= self.attack
        
        if self.health > 0:
            print(f"After having suffered {self.attack} the {self.monster} now has {self.health} points in health")
        
        else:
            print(f"After having suffered {self.attack} the {self.monster} now has {self.health} points in health")
            print(f"Victory!The {self.monster} has been defeated")
            
            

monster_1 = Monster(100, 1)
print(monster_1.monster)
print(monster_1.health)
print(monster_1.level)
print(monster_1.has_tiara)