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