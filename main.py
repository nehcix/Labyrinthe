from MazeGame import *


def main():
    mazeGame = MazeGame()

    mazeGame.start()
    optionAneedToBePressed = True

    while(mazeGame.isStared()):
        userInput = input(
            "(a) Entrer dans le labyrinthe.\n(b) Ouvrir une porte.\n(c) Afficher le chemin parcouru.\n(d) Quitter.\n-> ")

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
