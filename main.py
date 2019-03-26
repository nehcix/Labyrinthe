from MazeGame import *


def main():
    mazeGame = MazeGame()

    mazeGame.start()
    optionAneedToBePressed = True

    while(mazeGame.isStared()):
        userInput = input(
            "(a) Entrer dans le labyrinth.\n(b) Ouvrir une porte.\n(c) Afficher le chemin parcouru.\n(d) Quitter.\n-> ")

        if userInput == 'a':
            mazeGame.restartFromDoorOne()
            optionAneedToBePressed = mazeGame.isOptionAneedToBePressed()
        elif userInput == 'b':
            if optionAneedToBePressed == False:
                mazeGame.ouvrirPorte()
                optionAneedToBePressed = mazeGame.isOptionAneedToBePressed()
            else:
                print(
                    "\nTant que l’option (a) n’a pas été choisie, l’option (b) ne peut pas être choisie.\n")
        elif userInput == 'c':
            mazeGame.afficherLeCheminParccouru()
        elif userInput == 'd':
            mazeGame.end()
        else:
            print("\nEntrée invalide!\n")


main()
