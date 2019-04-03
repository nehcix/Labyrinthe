#/***********************************************************************************************
#Nom du fichier: main.py
#Auteurs: Nanor Janjikian - 1901777
#		 Xi Chen Shen - 1930285
#		 Hakim Payman - 1938609
#Date: 2 avril 2019
#Description: fichier contenant le programme principal.
#*********************************************************************************************/

from MazeGame import *


def main():
    mazeGame = MazeGame()

    mazeGame.start()
    optionAneedToBePressed = True

    while(mazeGame.isStarted()):
        print('''
                 +----------------------------------+
                 | (a) Entrer dans le labyrinthe.   | 
                 | (b) Ouvrir une porte.            | 
                 | (c) Afficher le chemin parcouru. | 
                 | (d) Quitter.                     |
                 +----------------------------------+
                 ''')
        userInput = input("-> ")

        if userInput == 'a':
            mazeGame.restartFromDoorOne()
        elif userInput == 'b':
            mazeGame.openCurrentDoor()
        elif userInput == 'c':
            mazeGame.afficherLeCheminParcouru()
        elif userInput == 'd':
            mazeGame.end()
        else:
            print("\nEntrée invalide!\n")


main()
