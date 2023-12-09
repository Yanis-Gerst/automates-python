from utils import *
from tpAutomates import complete
from automaton import EPSILON

def complement(a, b):
    if (is_determinstic(a) == False):
        return "ERROR"
    
    b.make_copy(a)
    complete(b)

    finals = b.get_final()
    for state in b.get_states():
        if state in finals:
             b.unmake_final(state)
        else:
            b.make_final(state)
       
    return b

def intersection(a,b,c):
    a.make_copy(c)

    for state in c.get_final():
        c.add_transition(state, EPSILON, b.initial + "bis")
    
    for (source, letter, target) in b.get_transitions():
        c.add_transition(source + "bis", letter, target + "bis")
    
    return c

def test_equality(a, b):
    if is_determinstic(a) == False or is_determinstic(b) == False:
        return "ERROR"

    return test_emptiness(intersection(a, complement(b, b))) and  test_emptiness(intersection(b, complement(a, a)))
