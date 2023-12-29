import random

class Monster:
    def __init__(self,monster, health, level):
        
        self.monster = "Goblin" or "Minotaur" or "Titan"
        self.health = health
        self.level = level
        self.has_tiara 
        

        random.choice(self.monster)
        
        if self.level == 10:
            self.has_tiara = True
             
        else:
            self.has_tiara = False
        
        if self.monster == "Titan":
            self.level = 10
            self.attack = 40
            print("Oh tremble in the presence of the notorius Titan")
            
            if self.health == 0:
                print("The TiTan has left behind the infamous Tiara of Perigourdin ")
    
            else:
                print("Good luck little one!Try again")

            
        
        elif self.monster == "Minotaur":
            self.level = 5
            self.attack = 15
            print("The Minotaur has arisen!Beware of his might!")
        
        else:
            self.level = 1
            self.attack = 5
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
            
            

    
    