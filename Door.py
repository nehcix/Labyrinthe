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

    # Todo
    def ouvrirPorte(self, pathHistory, passwordHistory):
        if self.__name == "PorteBoss":
            self.__bossKiller = BossKiller()
            self.__bossKiller.affronterBoss(pathHistory, passwordHistory)
            return "PorteBoss"
        else:
            if self.__name == "PorteGouffre":
                return "PorteGouffre"
            else:
                pathHistory.append(self.__name)
                print("\nEvenement Porte")
                print("a . ", end='')
                outputSting = ""
                for each in pathHistory:
                    outputSting += each + ", "
                print(outputSting[:-2])

                self.__automataGenerator = AutomataGenerator(self.__doorProductions, self.__doorPasswords)
                self.__automataGenerator.genererAutomate()
                return "Porte" + self.__automataGenerator.findDoorWithGoodPassword(passwordHistory)

    def getProduction(self):
        return self.__doorProductions
