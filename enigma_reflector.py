#-------------------------------------------------------------------------------
# Name:        enigma_reflector.py
#
# Notes:       The reflector which reverses the electrical signal and sends it
#              back through the rotors.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import string
from collections import namedtuple

ReflectedPosition = namedtuple("ReflectedPosition", "letter index")

class Reflector:
    """ Represents a reflector wheel (to the left of the rotors) which doesn't 
        rotate, which reverses the signal and sends it back through the rotors
        again.
    
        Attributes:
            id:
               A string representing the name of a reflector. 
               E.G. UKW-B
            writting:
               A string representing the internal wiring. 

        Methods:
            __init__(self, id, writing):
                Takes two strings to construct the reflector
            reflect():
                Takes the letter being encrypted from the left-most wheel and 
                looks up it's corresponding connection.
            __repr__():
                Returns a string in the format ['name', 'writting']
                E.G. [UKW-B, YRUHQSLDPXNGOKMIEBFZCWVJATI]
    """
    def __init__(self, id, writing):
        """Creates a reflector containing an id and reflection wiring. The 
           reflector is to the left of all the rotors and doesn't ever move.

        Args:
            id:
                A string representing the name of a reflector. 
                E.G. UKW-B
            writting:
                A string representing the internal wiring. 

        Returns:
            None.
        """  
        self.id, self.writing = id, writing

    def reflect(self, input_index):
        """Once we have gone through the rotors, we go through a reflection 
           wiring and go back through the inverse wiring of the rotors.

        Args:
            input_index:
                The letter index obtained by going through the three rotors.

        Returns:
            A namedtuple containing a reflected letter and it's position in the 
            alphabet.
        """        
        reflected_letter = self.writing[input_index]
        reflected_index = string.ascii_uppercase.index(reflected_letter) 

        return ReflectedPosition(reflected_letter, reflected_index)

    def __repr__(self):
        """Returns a string in the format ['name', 'writting']
           E.G. [UKW-B, YRUHQSLDPXNGOKMIEBFZCWVJATI]

        Args:
            None.

        Returns:
            A string.
        """  
        return "[%s, %s]" % (self.id, self.writing)

REFLECTORS = {
    "UKW-B": Reflector("UKW-B", "YRUHQSLDPXNGOKMIEBFZCWVJATI"),
    "UKW-C": Reflector("UKW-C", "FVPJIAOYEDRZXWGCTKUQSBNMHL"),
}