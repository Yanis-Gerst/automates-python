from automaton import EPSILON

def getLeftTransitionLetter(a, state):
    alphabet = a.get_alphabet()
    transitions = getTransitionOfState(a, state)
    for (source, letter, target) in transitions:
        alphabet.remove(letter)

    return alphabet

def addTransitionOfTrashState(a,state, letters):
    trashState = "trash"
    for letter in letters:
        a.add_transition(state, letter, trashState)



def getTransitionOfState(a, state):
    transitions = []
    for transition in a.get_transitions():
        if (transition[0] == state):
            transitions.append(transition)
    return transitions



def is_accessible(state, a):
    
    if state == a.initial:
        return True
    
    for (source, letter, target) in a.get_transitions():
        if target == state:
            return is_accessible(source,a)
        
    return False


def get_accessible(a):
    accessibleState = []

    for state in a.get_states():
        if a.initial == state:
            accessibleState.append(state)
        if (is_accessible(state, a.initial)):
            accessibleState.append(state)

    return accessibleState


def test_emptiness(a):
    accessibleState = get_accessible(a)
    finalStates = a.get_final()

    for state in finalStates:
        if finalStates in accessibleState:
            return False

    return True



def is_determinstic(a):
    sourceLetter = {}
    for (source, letter, target) in a.get_transitions():
        if letter == EPSILON:
            return False
        if (sourceLetter.get(source + letter) == letter): 
            return False
        
        sourceLetter[source + letter] = letter
        
    return True


def remove_espilon(a):
    for state in a.get_states():
        remove_espilon_of_state(a, state)

def remove_espilon_of_state(a, state):
    epsilonTransitions = get_epsilon_transition(a, state)
    for (source, letter, target) in epsilonTransitions:
        a.remove_transition(source, letter, target)

    targetStates = get_transitions_target(epsilonTransitions)
    for targetState in targetStates:
        epsilonTransitionOfTargetState = get_epsilon_transition(a, targetState)
        if (len(epsilonTransitionOfTargetState) > 0):
            remove_espilon_of_state(a, targetState)
        assign_transitions(a, targetState, state)

def get_epsilon_transition(a, state):
    transitions = getTransitionOfState(a, state)
    epsilonTransitions = []
    for transition in transitions:
        letter = transition[1]
        if letter == EPSILON:
            epsilonTransitions.append(transition)
    return epsilonTransitions

def get_transitions_target(transitions):
    targetState = []
    for (source, letter, target) in transitions:
        targetState.append(target)
    return targetState

def assign_transitions(a, state, stateToAssign):
    transitionsToAssign = getTransitionOfState(a,state)
    finalState = a.get_final()
    for (source, letter, target) in transitionsToAssign:
        a.add_transition(stateToAssign, letter, target if target != source else stateToAssign)
    
    if state in finalState:
        a.make_final(stateToAssign)
        


def isEqualArray(arr1, arr2):
    if (len(arr1) != len(arr2)):
        return False
    
    arr1.sort()
    arr2.sort()

    for i in range(0, len(arr1)):
        if(arr1[i] != arr2[i]):
            return False
    return True


def getTransitionsOfStatesByLetter(a, stateToFind, letter):
    transitions = []
    for transition in a.get_transitions():
        source = transition[0]
        currentLetter = transition[1]
        if source == stateToFind and currentLetter == letter:
            transitions.append(transition)

    return transitions

