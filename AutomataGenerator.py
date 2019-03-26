import random


class AutomataGenerator:
    def __init__(self, doorProductions, doorPasswords):
        self.__name = "AutomataGenerator"
        self.__doorProductions = doorProductions
        self.__doorPasswords = doorPasswords
        self.__N = []
        self.__T = []
        self.__initialState = 'S'
        self.__finalStates = []
        self.__states = []
        self.__transition = {}
        self.__goodDoors = []
        self.__badDoors = []

    # Todo
    def genererAutomate(self):
        # e.g. if we have S-> and A->aS, A->a will be added to doorProductions
        for eachProduction in self.__doorProductions:
            eachProduction = eachProduction.split("->")
            # if there is nothing after ->
            if len(eachProduction[1]) == 0:
                # search in a new copie of array
                for eachProduction2 in self.__doorProductions:
                    eachProduction2 = eachProduction2.split("->")
                    if len(eachProduction2[1]) == 2:
                        if eachProduction[0] in eachProduction2[1]:
                            # add A->a to doorProductions
                            self.__doorProductions.append(
                                eachProduction2[0] + "->" + eachProduction2[1][0])

        # add element to N, T, and finalStates
        for eachProduction in self.__doorProductions:
            eachProduction = eachProduction.split("->")
            # add element to N
            if eachProduction[0] not in self.__N:
                self.__N.append(eachProduction[0])
            # add element to T
            for eachLetter in eachProduction[1]:
                if not eachLetter.isupper() and eachLetter not in self.__T:
                    self.__T.append(eachLetter)
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
            eachProduction = eachProduction.split("->")
            # if there are 2 elements after ->
            if len(eachProduction[1]) == 2:
                # if the data is empty
                if self.__transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                    self.__transition[eachProduction[0]][eachProduction[1][0]] = [eachProduction[1][1]]
                else:
                    self.__transition[eachProduction[0]][eachProduction[1][0]].append(
                        eachProduction[1][1])
            # if there is only 1 element after ->
            if len(eachProduction[1]) == 1:
                # if the data is empty
                if self.__transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                    self.__transition[eachProduction[0]][eachProduction[1][0]] = [eachProduction[1][0]]
                else:
                    self.__transition[eachProduction[0]][eachProduction[1][0]].append(
                        eachProduction[1][0])

        # print("N: ", self.__N)
        # print("T: ", self.__T)
        # print("finalStates: ", self.__finalStates)
        # print(self.__transition)

        return

    def findDoorWithGoodPassword(self, passwordHistory):
        print("b . ", end='')
        outputString = ""
        for eachPassword in self.__doorPasswords:
            if "Boss" in eachPassword:
                eachPassword = eachPassword.split("Boss")

                if eachPassword[0] == "":
                    # if there is a S-> in doorProductions
                    for eachProduction in self.__doorProductions:
                        eachProduction = eachProduction.split("->")
                        if eachProduction[0] == 'S' and eachProduction[1] == '':
                            outputString += ("{" + eachPassword[0] + ", Boss" + ", valide" + "}, ")
                            self.__goodDoors = ["Boss"] + self.__goodDoors

                else:
                    if self.thisPasswordIsValid(eachPassword[0], self.__initialState):
                        outputString += ("{" + eachPassword[0] + ", Boss" + ", valide" + "}, ")
                        self.__goodDoors = ["Boss"] + self.__goodDoors
                    else:
                        outputString += ("{" + eachPassword[0] + ", Boss" + ", invalide" + "}, ")
                        self.__badDoors = ["Boss"] + self.__badDoors

            elif "Porte" not in eachPassword:
                break
            else:
                eachPassword = eachPassword.split("Porte")

                if eachPassword[0] == "":
                    # if there is a S-> in doorProductions
                    for eachProduction in self.__doorProductions:
                        eachProduction = eachProduction.split("->")
                        if eachProduction[0] == 'S' and eachProduction[1] == '':
                            outputString += ("{" + eachPassword[0] + ", Porte" + eachPassword[1] + ", valide" + "}, ")
                            self.__goodDoors.append(eachPassword[1])
                else:
                    if self.thisPasswordIsValid(eachPassword[0], self.__initialState):
                        outputString += ("{" + eachPassword[0] + ", Porte" + eachPassword[1] + ", valide" + "}, ")
                        self.__goodDoors.append(eachPassword[1])
                    else:
                        outputString += ("{" + eachPassword[0] + ", Porte" + eachPassword[1] + ", invalide" + "}, ")
                        self.__badDoors.append(eachPassword[1])

        print(outputString[:-2])

        if len(self.__goodDoors) == 0:
            print("c . Cette porte est un gouffre, retour à Porte1 .\n")
            return "Gouffre"
        else:
            #! return random door
            print("c . Cette porte n ' est pas un gouffre .\n")

            doorToReturn = random.choice(self.__goodDoors)
            # doorToReturn = self.__goodDoors[0]

            for eachPassword in self.__doorPasswords:
                if "Boss" in eachPassword:
                    eachPassword = eachPassword.split("Boss")
                    if doorToReturn == "Boss":
                        passwordHistory += (eachPassword[0])

                elif "Porte" not in eachPassword:
                    break
                else:
                    eachPassword = eachPassword.split("Porte")
                    if doorToReturn == eachPassword[1]:
                        passwordHistory += (eachPassword[0])

            return random.choice(self.__goodDoors)
            # return(self.__goodDoors[0])

    def thisPasswordIsValid(self, password, currentState):
        # check for each possibility
        if currentState not in self.__states:
            return False
        if password[0] not in self.__transition[currentState]:
            return False

        isGoodPassword = False
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
                    continue
                # inputString string for next transition is inputString[i+1:]
                self.thisPasswordIsValid(password[1:], currentState)
        return isGoodPassword
