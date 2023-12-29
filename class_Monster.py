class Monster:
    def __init__(self,name, health, level):
        self.name = name
        self.health = health
        self.level = level
       
        if level >= 5:
            self.has_tiara == True
        else:
            self.has_tiara == False
        
        
    def get_attack(self,attack):
        self.attack = attack
        return f"You have suffered{self.attack}"
        
    def get_damage(self):
        self.health -= self.attack
        return f"After having suffered {self.attack} you now have {self.health} points in health"
    
    
class Goblin(Monster): 
    level = 1
       
    def get_attack(self, ):
        
        self.attack = 5      
    pass    
 
class Minotaur(Monster):
    level = 5
    
    def get_attack(self):
        
        self.attack = 15
        00
    pass    

class Titan(Monster):
    level = 10
    
    def get_attack(self,attack):
        self.attack = 40
    pass
           