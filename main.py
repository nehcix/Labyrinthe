from MazeGame import *


def main():
    mazeGame = MazeGame()

    mazeGame.start()

    while(mazeGame.isStared()):
        userInput = input(
            "(a) Entrer dans le labyrinth.\n(b) Ouvrir une porte.\n(c) Afficher le chemin parcouru.\n(d) Quitter.\n-> ")

        if userInput == 'a':
            mazeGame.restartFromDoorOne()
        elif userInput == 'b':
            mazeGame.ouvrirPorte()
        elif userInput == 'c':
            mazeGame.afficherLeCheminParccouru()
        elif userInput == 'd':
            mazeGame.end()

    print("hi")


main()
