from Door import *


class MazeGame:
    def __init__(self):
        self.__name = "Labyrinthe"
        self.__isStarted = False
        self.__optionAneedToBePressed = False
        self.__currentDoor = ""
        self.__passwordHistory = ""
        self.__thisPathHistory = []
        self.__completePathHistory = []

    # replace l’agent face à la première porte et réinitialise toutes les structures de données interne afin d’entamer un nouveau parcours du labyrinthe. Il garde toutefois en tête le chemin parcouru jusqu’à maintenant.
    def restartFromDoorOne(self):
        self.__currentDoor = Door("Porte1")
        self.__thisPathHistory = []
        self.__passwordHistory = []
        self.__optionAneedToBePressed = False
        self.ouvrirPorte()
        return

    # permet de lire un fichier représentant une porte (ou le boss, le cas échéant) accessible à partir de l’emplacement courant, de déterminer l’automate relié à ce fichier et de déterminer les actions suivantes possibles par l’agent. Tant que l’option (a) n’a pas été choisie, l’option (b) ne peut pas être choisie. Il se peut qu’après l’exécution de l’option (b), on ne puisse plus exécuter l’option (b) parce que l’agent est tombé dans un gouffre ou a affronté le boss et qu’on doive choisir l’option (a) à nouveau.
    # Après avoir sélectionné l’option (b), l’agent affiche à la console le contenu du dernier événement (Porte ou Boss) tel que demandé dans l’annexe.
    def ouvrirPorte(self):
        if self.__optionAneedToBePressed == False:

            nextDoor = self.__currentDoor.ouvrirPorte(self.__thisPathHistory, self.__completePathHistory, self.__passwordHistory)
            self.__currentDoor = Door(nextDoor)

            if nextDoor == "PorteGouffre":
                self.__optionAneedToBePressed = True
            else:
                self.__optionAneedToBePressed = False
        else:
            print("\nTant que l’option (a) n’a pas été choisie, l’option (b) ne peut pas être choisie.\n")

    # Todo
    # L’option (c) permet d’afficher un récapitulatif des choix effectués par l’agent en détaillant les éléments indiqués au requis C4.
    def afficherLeCheminParccouru(self):
        print("".join(self.__completePathHistory))
        return

    def getName(self):
        return self.__name

    def start(self):
        self.__isStarted = True

    def end(self):
        self.__isStarted = False

    def isStared(self):
        return self.__isStarted
