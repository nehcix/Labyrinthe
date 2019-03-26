class Boss:
    def __init__(self):
        self.__name = "Boss"
        self.__rightPath = doorParts = open(
            "Boss.txt", 'r').read().split(' ')[:-1]
        self.__productions = []

    def getRightPath(self):
        return self.__rightPath

    def getProductions(self):
        counter = 0
        for eachDoor in self.__rightPath:

            if eachDoor != "Boss":
                counter += 1

                # read .txt and replace all space by nothing, separated by line break into a list
                doorParts = open(eachDoor + ".txt", 'r').read().replace(" ", "").replace("S", "S" + str(counter)).split('\n')
                tmpProductions = []

                # e.g. if we have S-> and A->aS, A->a will be added to doorProductions
                for eachProduction in doorParts[1].split(','):
                    tmpProductions.append(eachProduction.split("->"))

                for eachProduction in tmpProductions:
                    # if there is nothing after ->
                    if len(eachProduction[1]) == 0:
                        eachProduction[1] = "S" + str(counter+1)
                        # search in a new copie of array
                        for eachProduction2 in tmpProductions:
                            if len(eachProduction2[1]) == 3:
                                if eachProduction[0] in eachProduction2[1]:
                                    # add A->a to doorProductions
                                    tmpProductions.append(
                                        [eachProduction2[0], eachProduction2[1][0]])
                    if len(eachProduction[1]) == 1:
                        eachProduction[1] += "S" + str(counter+1)
                self.__productions += tmpProductions

        for eachProduction in self.__productions:
            if len(eachProduction[1]) == 3 and int(eachProduction[1][2]) == counter + 1:
                eachProduction[1] = eachProduction[1][:-2] + "Boss"

        return self.__productions

    def getRawProductions(self):
        productionsToReturn = []

        for eachDoor in self.__rightPath:
            if eachDoor != "Boss":

                # read .txt and replace all space by nothing, separated by line break into a list
                doorParts = open(eachDoor + ".txt", 'r').read().replace(" ", "").split('\n')
                productionsToReturn.append(doorParts[1])

        return "".join(productionsToReturn).split(',')
