#!/usr/bin/env python3
"""
Developpez votre projet de TP automates finis dans ce fichier.
"""
import sys
import os.path
from automaton import *
from utils import *
from determinize import determizeStates

def execute(a, s):
    if is_determinstic(a) == False:
        return "ERROR"
    currentState = a.initial

    while (s != ""):
        transitions = getTransitionOfState(a, currentState)
        currentLetter = s[0]
        isBlockingLetter = True
        for (source, letter, target) in transitions:
            if letter == currentLetter:
                currentState = target
                isBlockingLetter = False
        if (isBlockingLetter == True):
            return False
        s = s[1:]

    finalState = a.get_final()

    if currentState in finalState:
        return True
    return False
        


def complete(a):
    for state in a.get_states():
        letters = getLeftTransitionLetter(a, state)
        addTransitionOfTrashState(a,state, letters)

    for letter in a.get_alphabet():
        a.add_transition("trash", letter, "trash")


def determinize(a,b):
    b.make_copy(a)
    remove_espilon(b)
    determizeStates(b)
    return b




if __name__ == "__main__": # If the module is run from command line, test it

    
    a=Automaton("aut2")
    b=Automaton("auth3")
    
    a.set_initial("0")
    a.add_transition("0", "a", "1")

    a.add_transition("0", "b", "0")

    a.add_transition("1", "a", "2")


    a.add_transition("2", "a", "3")
    a.add_transition("2", "b", "2")
    a.add_transition("1", EPSILON, "2")
    a.add_transition("1", EPSILON, "3")
    a.add_transition("3", "b", "1")
    a.add_transition("3", "a","1" )
 

    a.make_final("3")

    print(determinize(a,b))
    print("cc")




