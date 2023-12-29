class Hero:

    def __init__(self, name, health, potions = 3, has_tiara = False, dead_flag = False):
        
        self.name = name
        self.health = health
        self.potions = potions
        self.has_tiara = has_tiara
        self.dead_flag = dead_flag

    def use_attack(self, attack = 10):
        self.attack = attack
        print (f"{self.name} attacks the monster and removes {self.attack} health points")

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

    def play(self):
        print (f"Chose an action : 1 : attack or 2 : drink a potion ; info --> potions left : {self.potions}")
        action = input()
        if action == "1":
            self.use_attack()
        elif action == "2":
            self.use_potion()
        else:
            print("You should choose between 1 or 2")
    
 

sami = Hero("Sami", 100)

print(sami.health)


        
sami.play()

# sami.use_attack()
# # sami.use_potion()
# # sami.use_potion()
# sami.is_dead()
# print(sami.dead_flag)