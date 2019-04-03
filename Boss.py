#/***********************************************************************************************
#Nom du fichier: Boss.py
#Auteurs: Nanor Janjikian - 1901777
#		 Xi Chen Shen - 1930285
#		 Hakim Payman - 1938609
#Date: 2 avril 2019
#Description: fichier contenant la declaration et l'implementation de la classe
#Boss.
#*********************************************************************************************/

class Boss:
    def __init__(self):
        self.__name = "Boss"
        self.__rightPath = doorParts = open(
            "Boss.txt", 'r').read().split(' ')[:-1]
        self.__productions = []
        self.__N = []
        self.__T = []
        self.__finalStates = ['Boss']
        self.__states = []
        self.__transition = {}

    def getRightPath(self):
        return self.__rightPath

    def prepareProductions(self):
        counter = 0
        for eachDoor in self.__rightPath:

            if eachDoor != "Boss":
                counter += 1

                # read .txt and replace all space by nothing, separated by line break into a list
                doorParts = open(eachDoor + ".txt", 'r').read().replace(" ", "").split('\n')
                tmpProductions = []

                # add an identifier to each Upper Letter in each door
                for eachProduction in doorParts[1].split(','):
                    eachProduction = list(eachProduction)
                    for i in range(0, len(eachProduction)):
                        if eachProduction[i].isupper():
                            eachProduction[i] += str(counter)
                    tmpProductions.append("".join(eachProduction).split("->"))

                
                tmpPasswords = doorParts[3:]
                for eachPassword in tmpPasswords:
                    if len(eachPassword) > 0 and eachPassword[0].isupper():
                        self.__productions += [["S" + str(counter), "S" + str(counter+1)]]

                # e.g. if we have S-> and A->aS, A->a will be added to productions
                for eachProduction in tmpProductions:
                    # if there is nothing after ->
                    if len(eachProduction[1]) == 0:

                        # tmpProductions += [["S" + str(counter), "S" + str(counter+1)]]

                        tmpProductions.remove(eachProduction)
                        # search in a new copy of array
                        for eachProduction2 in tmpProductions:
                            if len(eachProduction2[1]) == 3:
                                if eachProduction[0] in eachProduction2[1]:
                                    # add A->a to productions
                                    tmpProductions.append(
                                        [eachProduction2[0], eachProduction2[1][0]])
                    if len(eachProduction[1]) == 1:
                        eachProduction[1] += "S" + str(counter+1)
                self.__productions += tmpProductions

        for eachProduction in self.__productions:
            if len(eachProduction[1]) == 3 and int(eachProduction[1][2]) == counter + 1:
                eachProduction[1] = eachProduction[1][:-2] + "Boss"

        for counter in range(20, 0, -1):
            if ['S' + str(counter - 1), 'S' + str(counter)] in self.__productions:
                # self.__productions.remove(['S' + str(counter - 1), 'S' + str(counter)])
                for eachProduction in self.__productions:
                    if ('S' + str(counter)) in eachProduction[0] and 'S' in eachProduction[1] and len(eachProduction[1]) != 2:
                        self.__productions += [[('S' + str(counter-1)), eachProduction[1]]]

    def fillTransitions(self):
        # creation of the transition function with empty data
        for state in self.__states:
            self.__transition[state] = {}
            for eachT in self.__T:
                self.__transition[state][eachT] = [""]

        # add data to transition function
        for eachProduction in self.__productions:
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

    def genererAutomate(self):
        self.prepareProductions()

        # add element to N, T, and finalStates
        for eachProduction in self.__productions:

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

        self.__states = self.__N

        self.fillTransitions()

    def thisPasswordIsValid(self, password, currentState='S1'):
            # check for each possibility
        if currentState not in self.__states:
            return False
        if len(password) != 0 and password[0] not in self.__transition[currentState]:
            return False

        isGoodPassword = False
        if len(password) == 0:
            return isGoodPassword
        else:
            if len(password) == 1 and self.__transition[currentState][password] in self.__finalStates:
                isGoodPassword = True
                return isGoodPassword
            for each in self.__transition[currentState][password[0]]:
                # move further only if you are at a non-hypothetical currentState
                if isGoodPassword:
                    break
                elif each != '':
                    currentState = each
                    isGoodPassword = self.thisPasswordIsValid(password[1:], currentState)

        return isGoodPassword

    def getProductions(self):
        return self.__productions
