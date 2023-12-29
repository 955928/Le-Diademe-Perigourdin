import hero
import class_Monster

# on met un message de bienvenue dans le jeu

# on instancie un heros : hero = Hero(entrer les paramètres, health = 100)

# on entre dans le monde niveau 1

# on instancie un monstre du niveau du monde 1 : monster = Monster(level = 1 = niveau du monde, heatlh = 100)

# on mets un message pour indiquer la vie du héros et la vie du monstre

# on démarre la boucle while avec les arguments suivants : vie du héros <= 0 ou vie du monstre <= 0

# le héros commence



# TOUR DU HEROS (INPUT)



# on propose au héros un choix (1 : attaquer ou 2: potion) --> méthode play

# le heros fait son choix dans le terminal

    # si il fait 1 : on retire de la vie au monstre correspondant à l'attaque du héros --> méthode use_attack

        # coder dans le fichier main un truc du genre monster.health = monster.health - hero.attack

    # si il fait 2 : on ajoute de la vie au héros correspondant à la vie rendue par la potion --> méthode use_potion
    # si il fait une autre option : erreur choisir entre 1 et 2

# TOUR DU MONSTRE (AUTOMATIQUE)

# quand le joueur(héros) à finit son tour, le monstre contre attaque en retirant la vie au héros

        # coder dans le fichier main un truc du genre hero.health = hero.health - monster.attack

# on recommence



