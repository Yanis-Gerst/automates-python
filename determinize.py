from utils import *

def determizeStates(a):
    newStates = []
    initalStates = a.get_states()
    for state in a.get_states():
        doubleTransitions = getDoubleTransitionsByLetter(a, state)
        newStates.extend(cleanDoubleTransitions(a, state, doubleTransitions))


    processedStates = newStates.copy()
    for state in initalStates:
        processedStates.append([state])

    
    while len(newStates) > 0:
        currentDecomposeState = newStates[0]
        allTargets = assignTransitionToDecomposeState(a, currentDecomposeState)
       
        appendStateIfNotProccesed(processedStates, newStates, allTargets)
        newStates.pop(0)
    

       

def assignTransitionToDecomposeState(a, decomposeState):

    for letter in a.get_alphabet():
        targets = []
        for state in decomposeState:
            transitions = getTransitionsOfStatesByLetter(a, state, letter)
            currentTarget = get_transitions_target(transitions)
    
            if currentTarget != []:
                    targets.extend(getTargetOfTransitions(transitions))

        a.add_transition(proccedStateName(decomposeState),letter, proccedStateName(targets))
        
    return targets


def getDoubleTransitionsByLetter(a, state):
    transitions = getTransitionOfState(a, state)
    transitionByLetter = {letter: [] for letter in a.get_alphabet()}
    for transition in transitions:
        letter = transition[1]
        transitionByLetter[letter].append(transition)
    for letter in a.get_alphabet():
        if len(transitionByLetter[letter]) <= 1:
            del transitionByLetter[letter]
    return transitionByLetter


def cleanDoubleTransitions(a,state,transitionByLetter):
    newStates = []
    for letter in transitionByLetter.keys():
        if len(transitionByLetter[letter]) > 1:
            targetsOfLetter = getTargetOfTransitions(transitionByLetter[letter])
            removeTransitions(a, transitionByLetter[letter])
            a.add_transition(state, letter,proccedStateName(targetsOfLetter))
            appendNewState(newStates, targetsOfLetter)
    return newStates

def getTargetOfTransitions(transitions):
    targets = []
    for (source,letter, target) in transitions:
        targets.append(target)
    return targets
    
def removeTransitions(a, transitions):
    for (source, letter, target) in transitions:
        a.remove_transition(source,letter, target)


def proccedStateName(states):
    string = "".join(states)
    stateName = list(set(string))
    stateName.sort()
    return "".join(stateName)
def appendNewState(newStatesList, decomposeState):
    for newState in newStatesList:
        if newState.sort() == decomposeState.sort():
            return
    newStatesList.append(decomposeState)

def appendStateIfNotProccesed(proccesedStates, newStatesList, decomposeState):
    if (decomposeState == None or decomposeState == []):
        return

    for proccesedState in proccesedStates:
        if isEqualArray(proccesedState, decomposeState):
            return

    newStatesList.append(decomposeState)
    proccesedStates.append(decomposeState)
    

