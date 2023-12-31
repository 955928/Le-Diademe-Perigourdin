class Hero:

    def __init__(self, name, health, potions = 3, has_tiara = False, dead_flag = False):
        
        self.name = name
        self.health = health
        self.potions = potions
        self.has_tiara = has_tiara
        self.dead_flag = dead_flag

    def use_attack(self, monster, attack = 10):
        monster.health -= attack

        print (f"{self.name} attacks the monster and removes {attack} health points")

    def use_potion(self, potion_health = 50):
        self.health = self.health + potion_health
        self.potions = self.potions - 1
        print (f"{self.name} drinks a potion and recovers for {potion_health} health points - He has now {self.health} health")

    def is_dead(self):
        if self.health > 0:
            print (f"{self.name} has {self.health} health points - He is alive and can fight the monster")
        else:
            print(f"{self.name} is dead... game over!")
            self.dead_flag = True
            #break
        
            

    def play(self, monster):
        print (f"Press 1 if you want to launch an attack \n    Press 2 if you want to drink a potion \n    For your information, the number of potions you have left is {self.potions}")

        
        action = input(": ")
    def play(self, monster):
        print (f"Press 1 if you want to launch an attack \n    Press 2 if you want to drink a potion \n    For your information, the number of potions you have left is {self.potions}")

        
        action = input(": ")

        if action == "1":
            self.use_attack(monster)
        elif action == "2":
            self.use_potion()  
        else:
            print("You should choose between 1 or 2")
