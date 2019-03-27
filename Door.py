from BossKiller import *
from AutomataGenerator import *


class Door:
    def __init__(self, name):
        self.__name = name
        if self.__name != "PorteBoss" and self.__name != "PorteGouffre":
            # read .txt and replace all space by nothing, separated by line break into a list
            doorParts = open(self.__name + ".txt", 'r').read().replace(" ", "").split('\n')
            self.__doorProductions = doorParts[1].split(',')
            self.__doorPasswords = doorParts[3:]

    def getName(self):
        return self.__name

    def ouvrirPorte(self, thisPathHistory, completeEventsHistory, passwordHistory):
        if self.__name == "PorteBoss":
            self.__bossKiller = BossKiller()
            self.__bossKiller.affronterBoss(thisPathHistory, completeEventsHistory, passwordHistory)
            return "PorteGouffre"
        elif self.__name == "PorteGouffre":
            return "PorteGouffre"
        else:
            thisPathHistory.append(self.__name)
            stringToPrint = ""
            stringToPrint += "\nEvenement Porte\n"
            stringToPrint += "a . "
            for each in thisPathHistory:
                stringToPrint += each + ", "
            print(stringToPrint[:-2])
            completeEventsHistory += stringToPrint[:-2] + "\n"

            self.__automataGenerator = AutomataGenerator(self.__doorProductions, self.__doorPasswords)
            self.__automataGenerator.genererAutomate()
            return "Porte" + self.__automataGenerator.findDoorWithGoodPassword(passwordHistory, completeEventsHistory)

    def getProduction(self):
        return self.__doorProductions
