from BossKiller import *
from AutomataGenerator import *


class Door:
    def __init__(self):
        self.__name = "door"
        self.__bossKiller = BossKiller()
        self.__automataGenerator = AutomataGenerator()

    def getName(self):
        return self.__name

    def ouvrirPorte(self):
        if self.__name == "Boss":
            self.__bossKiller.affronterBoss()
        else:
            elf.__automataGenerator.genererAutomate()
        return
