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
            #break
        
            

    def play(self):
        print (f"Welcome to The Legend of Perigordian Diadem, \n The search of Perigordian Diadem is getting complicated, help Jack to defeat monsters and to recover the Diadem ! \n    Press 1 if you want to launch an attack \n    Press 2 if you want to drink a potion \n    For your information, the number of potions you have left is {self.potions}")

        while True: 
            action = input(": ")

            if action == "1":
                self.use_attack()
            elif action == "2":
                self.use_potion()
                
            else:
                print("You should choose between 1 or 2")

            #Code pour alterner un tour chacun entre héro et monstre
                
    
 

jack = Hero("Jack", 100)

print(jack.health)


        
jack.play()

# jack.use_attack()
# # jack.use_potion()
# # jack.use_potion()
# jack.is_dead()
# print(jack.dead_flag)