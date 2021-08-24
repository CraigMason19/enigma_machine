#-------------------------------------------------------------------------------
# Name:        enigma_random.py
#
# Notes:       A helpful set of functions to test random enigma configurations. 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('../../Helper')

import random
import letters
from enigma_machine import M3EnigmaMachine

def random_reflector():
    """Returns a random reflector id

    Args:
        None.

    Returns:
        A string containing a random Reflector ID.
    """ 
    return random.choice(["UKW-C", "UKW-B"])

def random_rotors():
    """Returns a random list of 3 rotor id's (Roman numerals) from a set of 5 

    Args:
        None.

    Returns:
        A list of 3 strings in Roman numeral form.
    """ 
    return random.sample(set(["I", "II", "III", "IV", "V"]), 3)

def random_start_positions():
    """Returns a random list of 3 letters representing where the wheels are 
       rotated too.

    Args:
        None.

    Returns:
        A list of 3 letters.
    """ 
    return [letters.random_upper_letter() for i in range(3)]

def random_ring_settings():
    """Returns a random list of 3 letters representing the ring settings 

    Args:
        None.

    Returns:
        A list of 3 letters.
    """ 
    return [letters.random_upper_letter() for i in range(3)]

def random_plugboard():
    """Returns a random string of 10 plug combinations in the format
       'XX XX XX XX...'.

    Args:
        None.

    Returns:
        A string representing the plug combinations.
    """ 
    alphabet_list = list(letters.ALPHABET_UPPER)
    random.shuffle(alphabet_list)

    i = iter(alphabet_list[:20]) # Historically 10 pairs of plugs were used
    return ' '.join(a+b for a,b in zip(i, i))

def create_random_machine():
    """Returns a completely random Enigma machine setup, including reflector,
       rotors, positions, ring settings and plug combinations.

    Args:
        None.

    Returns:
        A M3EnigmaMachine class.
    """ 
    reflector = random_reflector()
    rotors = random_rotors()
    positions = random_start_positions()
    rings = random_ring_settings()
    plugs = random_plugboard()

    em = M3EnigmaMachine(reflector, rotors)
    em.set_rotors(positions, rings)
    em.set_plugboard(plugs)

    return em

def print_random_settings():
    """Prints completely random Enigma components.

    Args:
        None.

    Returns:
        None.
    """ 
    print(f'Reflector: {random_reflector()}')
    print(f'Rotors: {random_rotors()}')
    print(f'Start positions: {random_start_positions()}')
    print(f'Ring settings: {random_ring_settings()}')
    print(f'Random plugboard: {random_plugboard()}')    

if __name__ == "__main__":
    print_random_settings()