#/***********************************************************************************************
#Nom du fichier: BossKiller.py
#Auteurs: Nanor Janjikian - 1901777
#		 Xi Chen Shen - 1930285
#		 Hakim Payman - 1938609
#Date: 2 avril 2019
#Description: fichier contenant la declaration et l'implementation de la classe
#BossKiller.
#*********************************************************************************************/

from Boss import *
from AutomataGenerator import *


class BossKiller:
    def __init__(self):
        self.__boss = Boss()
        self.__name = "BossKiller"

    def affronterBoss(self, thisPathHistory, completeEventsHistory, passwordHistory):
        stringToPrint = ""
        stringToPrint += "\nÉvènement Boss\n"

        stringToPrint += "a . "
        for each in self.__boss.getRightPath():
            stringToPrint += each + ", "
        stringToPrint = stringToPrint[:-2]

        stringToPrint += "\nb . " + "".join(passwordHistory) + " P={"

        if self.__boss.getRightPath() == thisPathHistory:

            self.__boss.genererAutomate()

            if self.__boss.thisPasswordIsValid((''.join(passwordHistory) + "PorteBoss").split("Porte")[0]):
                for each in self.__boss.getProductions():
                    if "Boss" in each[1]:
                        stringToPrint += each[0] + "->" + each[1][:-4] + ", "
                    else:
                        stringToPrint += each[0] + "->" + each[1] + ", "
                stringToPrint = stringToPrint[:-2] + "}"
                stringToPrint += "\nc . L'agent vainc le Boss .\n"
            else:
                stringToPrint += "...}"
                stringToPrint += "\nc . Le Boss vainc l'agent . Retour a la Porte1 .\n"

        else:
            stringToPrint += "...}"
            stringToPrint += "\nc . Le Boss vainc l'agent . Retour a la Porte1 .\n"

        print(stringToPrint)
        completeEventsHistory += stringToPrint
