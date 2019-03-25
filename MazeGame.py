from Door import *


class MazeGame:
    def __init__(self):
        self.__name = "Labyrinthe"
        self.__isStarted = False
        self.__pathHistory = []

    # Todo
    # replace l’agent face à la première porte et réinitialise toutes les structures de données interne afin d’entamer un nouveau parcours du labyrinthe. Il garde toutefois en tête le chemin parcouru jusqu’à maintenant.
    def restartFromDoorOne(self):
        self.__currentDoor = Door("Porte1")
        return

    # Todo
    # permet de lire un fichier représentant une porte (ou le boss, le cas échéant) accessible à partir de l’emplacement courant, de déterminer l’automate relié à ce fichier et de déterminer les actions suivantes possibles par l’agent. Tant que l’option (a) n’a pas été choisie, l’option (b) ne peut pas être choisie. Il se peut qu’après l’exécution de l’option (b), on ne puisse plus exécuter l’option (b) parce que l’agent est tombé dans un gouffre ou a affronté le boss et qu’on doive choisir l’option (a) à nouveau.
    # Après avoir sélectionné l’option (b), l’agent affiche à la console le contenu du dernier événement (Porte ou Boss) tel que demandé dans l’annexe.
    def ouvrirPorte(self):
        self.__currentDoor.ouvrirPorte()

    # Todo
    # L’option (c) permet d’afficher un récapitulatif des choix effectués par l’agent en détaillant les éléments indiqués au requis C4.
    def afficherLeCheminParccouru(self):
        print(self.__pathHistory[-1])
        return

    def getName(self):
        return self.__name

    def start(self):
        self.__isStarted = True

    def end(self):
        self.__isStarted = False

    def isStared(self):
        return self.__isStarted
