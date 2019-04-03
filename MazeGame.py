#/***********************************************************************************************
#Nom du fichier: MazeGame.py
#Auteurs: Nanor Janjikian - 1901777
#		 Xi Chen Shen - 1930285
#		 Hakim Payman - 1938609
#Date: 2 avril 2019
#Description: fichier contenant la declaration et l'implementation de la classe
#MazeGame.
#*********************************************************************************************/

from Door import *


class MazeGame:
    def __init__(self):
        self.__name = "Labyrinthe"
        self.__isStarted = False
        self.__optionAneedToBePressed = True
        self.__currentDoor = ""
        self.__passwordHistory = ""
        self.__thisPathHistory = []
        self.__completeEventsHistory = []

    # Restarts the player position to door 1 and resets all data structures 
    # except for the completeEventsHistory used before calling this method.
    def restartFromDoorOne(self):
        self.__currentDoor = Door("Porte1")
        self.__thisPathHistory = []
        self.__passwordHistory = []
        self.__optionAneedToBePressed = False
        print("\nVous etes maintenant devant la porte 1 du labyrinthe.\n")
        return

    # Reads a text file representing a door or the boss, creates the
    # automata accordingly and displays the information about the current event. 
    # This method cannot be called before restartFromDoorOne.
    def openCurrentDoor(self):
        if self.__optionAneedToBePressed == False:

            nextDoor = self.__currentDoor.ouvrirPorte(self.__thisPathHistory, self.__completeEventsHistory, self.__passwordHistory)
            self.__currentDoor = Door(nextDoor)

            if nextDoor == "PorteGouffre":
                self.__optionAneedToBePressed = True
            else:
                self.__optionAneedToBePressed = False
        else:
            print("\nTant que l’option (a) n’a pas été choisie, l’option (b) ne peut pas être choisie.\n")

    # Displays a recap of all the events that occured before calling 
    # this method
    def afficherLeCheminParcouru(self):
        print("".join(self.__completeEventsHistory))
        return

    def getName(self):
        return self.__name

    def start(self):
        self.__isStarted = True

    def end(self):
        self.__isStarted = False

    def isStarted(self):
        return self.__isStarted
