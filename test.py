import sys


def runnnn():
    doorNumber = input("Door number is : ")
    door = open("Porte" + doorNumber + ".txt", 'r')
    doorParts = door.read().replace(" ", "").split('\n')
    doorProductions = doorParts[1].split(',')
    doorPasswords = doorParts[3:]

    N = []
    T = []
    finalStates = []

    # e.g. if we have S-> and A->aS, A->a will be added to doorProductions
    for eachProduction in doorProductions:
        eachProduction = eachProduction.split("->")
        # if there is nothing after ->
        if len(eachProduction[1]) == 0:
            # search in a new copie of array
            for eachProduction2 in doorProductions:
                eachProduction2 = eachProduction2.split("->")
                if len(eachProduction2[1]) == 2:
                    if eachProduction[0] in eachProduction2[1]:
                        # add A->a to doorProductions
                        doorProductions.append(
                            eachProduction2[0] + "->" + eachProduction2[1][0])

    # add element to N, T, and finalStates
    for eachProduction in doorProductions:
        eachProduction = eachProduction.split("->")
        # add element to N
        if eachProduction[0] not in N:
            N.append(eachProduction[0])
        # add element to T
        for eachLetter in eachProduction[1]:
            if not eachLetter.isupper() and eachLetter not in T:
                T.append(eachLetter)
        # add element to finalStates
        if len(eachProduction[1]) == 1 and not eachProduction[1].isupper() and eachProduction[1] not in finalStates:
            finalStates.append(eachProduction[1])

    print("N: ", N)
    print("T: ", T)
    print("finalStates: ", finalStates)

    states = finalStates + N
    transition = {}

    # creation of the transition function with empty data
    for state in states:
        transition[state] = {}
        for eachT in T:
            transition[state][eachT] = [""]

    # add data to transition function
    for eachProduction in doorProductions:
        eachProduction = eachProduction.split("->")
        # if there are 2 elements after ->
        if len(eachProduction[1]) == 2:
            # if the data is empty
            if transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                transition[eachProduction[0]][eachProduction[1][0]] = [
                    eachProduction[1][1]]
            else:
                transition[eachProduction[0]][eachProduction[1]
                                              [0]].append(eachProduction[1][1])
        # if there is only 1 element after ->
        if len(eachProduction[1]) == 1:
            # if the data is empty
            if transition[eachProduction[0]][eachProduction[1][0]] == [""]:
                transition[eachProduction[0]][eachProduction[1][0]] = [
                    eachProduction[1][0]]
            else:
                transition[eachProduction[0]][eachProduction[1]
                                              [0]].append(eachProduction[1][0])

    for eachPassword in doorPasswords:
        eachPassword = eachPassword.split("Porte")

    print(transition)

    # if the input is null, check if the initial state is a final state
    inputString = input("enter the string: ").replace(" ", "")
    if inputString == "":
        for eachProduction in doorProductions:
            eachProduction = eachProduction.split("->")
            if eachProduction[0] == 'S' and eachProduction[1] == '':
                print("valide par absence")
                sys.exit()

    # copy the inputString in list because python strings are immutable and thus can't be changed directly
    inputString = list(inputString)

    # set of final states
    initialState = 'S'

    checkValidity(transition, inputString, finalStates, initialState, states)
    print("invalide")


def checkValidity(transition, inputString, finalStates, currentState, states):
    # check for each possibility
    if currentState not in states:
        print("invalide par WTF currentState")
        sys.exit()
    if inputString[0] not in transition[currentState]:
        print("invalide par WTF inputString")
        sys.exit()

    for each in transition[currentState][inputString[0]]:
        # move further only if you are at non-hypothetical currentState
        if each != '':
            currentState = each
            if len(inputString) == 1:
                # last symbol is read and currentState lies in the set of final states
                if (currentState in finalStates):
                    print("valide")
                    sys.exit()
                else:
                    continue
            # inputString string for next transition is inputString[i+1:]
            checkValidity(
                transition, inputString[1:], finalStates, currentState, states)


runnnn()
