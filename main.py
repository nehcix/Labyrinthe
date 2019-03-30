from MazeGame import *


def main():
    mazeGame = MazeGame()

    mazeGame.start()
    optionAneedToBePressed = True

    while(mazeGame.isStared()):
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
            mazeGame.ouvrirPorte()
        elif userInput == 'c':
            mazeGame.afficherLeCheminParccouru()
        elif userInput == 'd':
            mazeGame.end()
        else:
            print("\nEntrée invalide!\n")


main()
