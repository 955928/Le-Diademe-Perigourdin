from hero import *
from class_Monster import *

# on met un message de bienvenue dans le jeu
print(f"Welcome to The Legend of Perigordian Diadem, \nThe search of Perigordian Diadem is getting complicated, help Jack to defeat monsters and to recover the Diadem !")
# on instancie un heros : hero = Hero(entrer les paramètres, health = 100)
hero_1 = Hero("Jack", 100)

# on instancie un monstre du niveau du monde 1 : monster = Monster(level = 1 = niveau du monde, heatlh = 100)
monster_1 = Monster()

# on mets un message pour indiquer la vie du héros et la vie du monstre
print (f"{hero_1.name} has {hero_1.health} health")
print (f"{monster_1.monster} has {monster_1.health} health")
print (f"{hero_1.name} starts first")

while hero_1.health > 0 and monster_1.health > 0:
# on démarre la boucle while avec les arguments suivants : vie du héros <= 0 ou vie du monstre <= 0

# le héros commence


# TOUR DU HEROS (INPUT)

# on propose au héros un choix (1 : attaquer ou 2: potion) --> méthode play
    hero_1.is_dead()
    hero_1.play(monster_1)
    print(hero_1.health)
    print(monster_1.health)
    monster_1.get_attack(hero_1)
# le heros fait son choix dans le terminal

    # si il fait 1 : on retire de la vie au monstre correspondant à l'attaque du héros --> méthode use_attack
        # coder dans le fichier main un truc du genre monster.health = monster.health - hero.attack

    # si il fait 2 : on ajoute de la vie au héros correspondant à la vie rendue par la potion --> méthode use_potion
    # si il fait une autre option : erreur choisir entre 1 et 2
hero_1.is_dead()
monster_1.is_dead()
# TOUR DU MONSTRE (AUTOMATIQUE)

# quand le joueur(héros) à finit son tour, le monstre contre attaque en retirant la vie au héros

        # coder dans le fichier main un truc du genre hero.health = hero.health - monster.attack

# on recommence