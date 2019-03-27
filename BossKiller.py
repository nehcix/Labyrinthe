from Boss import *
from AutomataGenerator import *


class BossKiller:
    def __init__(self):
        self.__boss = Boss()
        self.__name = "BossKiller"
        self.__doorProductions = []
        self.__doorPasswords = []
        self.__N = []
        self.__T = []
        self.__initialState = 'S1'
        self.__finalStates = []
        self.__states = []
        self.__transition = {}
        self.__goodDoors = []
        self.__badDoors = []

    def affronterBoss(self, thisPathHistory, completeEventsHistory, passwordHistory):
        stringToPrint = ""
        stringToPrint += "\nEvenement Boss\n"

        stringToPrint += "a . "
        for each in thisPathHistory:
            stringToPrint += each + ", "
        stringToPrint = stringToPrint[:-2]

        stringToPrint += "\nb . " + "".join(passwordHistory) + ", P ="

        if self.__boss.getRightPath() == thisPathHistory:

            self.__doorProductions = self.__boss.getProductions()
            self.__doorPasswords = ''.join(passwordHistory) + "Porte99"

            # add element to N, T, and finalStates
            for eachProduction in self.__doorProductions:

                # add element to N
                if eachProduction[0] not in self.__N:
                    self.__N.append(eachProduction[0])

                # add element to T
                if len(eachProduction[1]) == 1 and eachProduction[1] not in self.__T:
                    self.__T.append(eachProduction[1])
                 # add element to T
                if len(eachProduction[1]) == 3 and eachProduction[1][0] not in self.__T:
                    self.__T.append(eachProduction[1][0])

                # add element to finalStates
                if len(eachProduction[1]) == 1 and not eachProduction[1].isupper() and eachProduction[1] not in self.__finalStates:
                    self.__finalStates.append(eachProduction[1])

            self.__states = self.__finalStates + self.__N

            # creation of the transition function with empty data
            for state in self.__states:
                self.__transition[state] = {}
                for eachT in self.__T:
                    self.__transition[state][eachT] = [""]

            # add data to transition function
            for eachProduction in self.__doorProductions:
                # if there are 2 elements after ->
                if len(eachProduction[1]) == 3:
                    # if the data is empty
                    if self.__transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]] = [eachProduction[1][1:3]]
                    elif eachProduction[1][1:3] not in self.__transition[eachProduction[0]][eachProduction[1][0]]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]].append(
                            eachProduction[1][1:3])

                if len(eachProduction[1]) == 2 and not eachProduction[1][0].isupper():
                    # if the data is empty
                    if self.__transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]] = [eachProduction[1][1]]
                    elif eachProduction[1][1] not in self.__transition[eachProduction[0]][eachProduction[1][0]]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]].append(
                            eachProduction[1][1])

                # if there is only 1 element after ->
                if len(eachProduction[1]) == 1:
                    # if the data is empty
                    if self.__transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]] = [eachProduction[1][0]]
                    elif eachProduction[1][0] not in self.__transition[eachProduction[0]][eachProduction[1]]:
                        self.__transition[eachProduction[0]][eachProduction[1][0]].append(
                            eachProduction[1][0])

                # if there is only 5 element after ->
                if len(eachProduction[1]) == 5:
                    self.__transition[eachProduction[0]][eachProduction[1][0]] = eachProduction[1][1:]

            if self.thisPasswordIsValid(self.__doorPasswords.split("Porte")[0], self.__initialState):
                print("{", end='')
                for each in self.__boss.getRawProductions():
                    stringToPrint += each + ", "
                stringToPrint = stringToPrint[:-2]
                stringToPrint += "\nc . L'agent vainc le Boss .\n"
            else:
                stringToPrint += "{...}"
                stringToPrint += "\nc . Le Boss vainc l'agent . Retour a la Porte1 .\n"

        else:
            stringToPrint += "{...}"
            stringToPrint += "\nc . Le Boss vainc l'agent . Retour a la Porte1 .\n"

        print(stringToPrint)
        completeEventsHistory += stringToPrint

    def thisPasswordIsValid(self, password, currentState):
            # check for each possibility
        if currentState not in self.__states:
            return False
        if len(password) != 0 and password[0] not in self.__transition[currentState]:
            return False

        isGoodPassword = False
        if len(password) == 0:
            return isGoodPassword
        else:
            if len(password) == 1 and self.__transition[currentState][password] == "Boss":
                isGoodPassword = True
                return isGoodPassword
            for each in self.__transition[currentState][password[0]]:
                # move further only if you are at non-hypothetical currentState
                if each != '':
                    currentState = each
                    if len(password) == 1:
                        # last symbol is read and currentState lies in the set of final states
                        if (currentState in self.__finalStates):
                            isGoodPassword = True
                        else:
                            isGoodPassword = False
                    # inputString string for next transition is inputString[i+1:]
                    isGoodPassword = self.thisPasswordIsValid(password[1:], currentState)
            if isGoodPassword == False and len(currentState) == 2 and [currentState, "S" + str(int(currentState[1]) + 1)] in self.__doorProductions:
                currentState = "S" + str(int(currentState[1]) + 1)
                isGoodPassword = self.thisPasswordIsValid(password, currentState)

        return isGoodPassword
