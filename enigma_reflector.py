#-------------------------------------------------------------------------------
# Name:        enigma_reflector.py
#
# Notes:       Represents the reflector at the end of the rotors which reverses 
#              the signal and sends it back through the rotors
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import string
from collections import namedtuple

ReflectedPosition = namedtuple("ReflectedPosition", "letter index")

class Reflector:
    ''' Represents a reflector, which doesn't rotate but sends the encoding back
        through the ROTORS once again '''
    def __init__(self, id, writing):
        self.id, self.writing = id, writing

    def reflect(self, input_index):
        ''' Once we have gone through the ROTORS, we go through a reflection wiring
            and go back through the inverse ROTORS '''        
        reflected_letter = self.writing[input_index]
        reflected_index = string.ascii_uppercase.index(reflected_letter) # Alphabet

        return ReflectedPosition(reflected_letter, reflected_index)

    #TODO remove?
    # def __str__(self):
    #     return "%s" % (self.writing)

    def __repr__(self):
        return "[%s, %s]" % (self.id, self.writing)

REFLECTORS = {
    "UKW-B": Reflector("UKW-B", "YRUHQSLDPXNGOKMIEBFZCWVJATI"),
    "UKW-C": Reflector("UKW-C", "FVPJIAOYEDRZXWGCTKUQSBNMHL"),
}