#-------------------------------------------------------------------------------
# Name:        enigma_rotor.py
#
# Notes:       Represents a single rotor of the machine. Rotors had a fixed 
#              internal wiring and could be swapped out to allow various
#              configurations. The right most rotor would increment after each
#              key press. If a special notch letter was triggererd it would 
#              rotate the rotor to it's left.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

import sys
sys.path.append('../../Helper')

from collections import namedtuple
import string

import letters

RedirectedPosition = namedtuple("RedirectedPosition", "letter index")

class Rotor:
    """Represents a rotor of the machine. If a special notch letter was triggererd 
       it would rotate the rotor to it's left.
    
    Attributes:
        id:
            A string representing the name of a rotor in roman numerals. 
            E.G. IV
        notch:
            A letter representing the notch or 'turnover' position. 
        writing:
            A string representing the internal wiring.
        current_letter:
            A letter representing the rotor's current position.
        alphabet:
            A string.

    Methods:
        __init__(id, writing, notch):
            Constructs the rotor.
        is_in_notch_position():
            Determines if the rotor has reached it's notch position.
        is_in_post_notch_position():
            Determines if the rotor has just passed it's notch position.
        configure(letter, ring_setting='A'):
            Sets up a rotor by turning it to the correct position, also sets the 
            rotor's ring setting if provided, sets it to the 'A' position if not.
        rotate():
            Rotates the rotor wheel ONE position.
        redirect(input_index, reverse=False):
            Passes a letter left or right through the rotor based on the reversed flag.
        __str__():
            Returns a upper case string containing the current rotors wiring position.
            E.G. SUCAYWJLNPRTKXZBFDHVGMQEOI
        __repr__():
            Returns a string in the format [id, writing, notch=X, letter=X, ring=X].
            E.G. [III, SUCAYWJLNPRTKXZBFDHVGMQEOI, notch=V, letter=C, ring=I]
    """
    def __init__(self, id, writing, notch):
        """Creates a rotor that can be placed anywhere in the machine.

        Args:
            id:
                A string representing the name of a rotor in roman numerals up to 5. 
                E.G. IV
            writing:
                A string representing the internal wiring. 
            notch:
                A letter representing when the rotor is in position to turn the rotor
                to it's left.

        Returns:
            None.
        """  
        self.id, self.writing, self.notch = id, writing, notch
        
        self.current_letter = 'A'
        self.alphabet = letters.ALPHABET_UPPER

    def is_in_notch_position(self):
        """Returns true if the rotor's position is in the notch position, false otherwise.

        Args:
            None. 

        Returns:
            A bool.
        """   
        return (self.current_letter == self.notch)

    def is_in_post_notch_position(self):
        """Returns true if the rotor's position is one place higher than the notch
           position, false otherwise.

        Args:
            None. 

        Returns:
            A bool.
        """   
        return (self.current_letter == letters.shift_letter_up(self.notch, 1))

    def configure(self, letter, ring_setting='A'):
        """Sets up the rotor by turning it to the correct position, also sets the 
           rotor's ring setting if provided, sets it to the 'A' position if not. In the
           'A' position it has no effect on the machine.

        Args:
            letter:
                The letter that the rotor is set to in the machine. 
            ring_setting:
                (Also known as the Ringstellung). A letter showing the ring setting to be 
                used.

        Returns:
            None.
        """   
        while self.current_letter != letter:
            self.rotate()

        self.ring_setting = ring_setting

        # If the ring setting is 'A' it has no effect on the rotor's letter
        # redirection
        if ring_setting == "a" or ring_setting == "A":
            return
        else:
            # Shift all the letters in the wiring up based upon the ring setting's index
            shift_factor = letters.letter_to_index(self.ring_setting)
            shifted_alphabet = letters.shift_alphabet(shift_factor, True)
            shifted_writing = ''.join([letters.shift_letter_up(c, shift_factor) for c in self.writing])

            # Create a list of tuples pairing up the shifted alphabet and writing. Then sort
            # alphabetically.
            tmp = sorted([(shifted_alphabet[x], shifted_writing[x]) for x in range(26)])
            # Finally, alter the state of the internal wiring
            self.writing = ''.join([letter[1] for letter in tmp]) 

    def rotate(self):
        """Turn the rotor once. A rotor is a circular disc and so will always 
           be able to turn.

        Args:
            None. 

        Returns:
            None.
        """   
        self.alphabet = self.alphabet[1:] + self.alphabet[:1]
        self.writing = self.writing[1:] + self.writing[:1]
        self.current_letter = self.alphabet[0]

    def redirect(self, input_index, reverse=False):
        """Redirect a letter through the rotor.

        Args:
            input_index:
                The index of the letter to be redirected.
            reverse=False:
                A bool to determine which way (left or right) we are going 
                through the rotor.

        Returns:
            A namedtuple containing a redirected letter and it's position in either
            the alphabet or rotor wiring. 
        """   
        if reverse:
            redirected_letter = self.alphabet[input_index]
            redirected_index = self.writing.index(redirected_letter)
        else:
            redirected_letter = self.writing[input_index]
            redirected_index = self.alphabet.index(redirected_letter)

        return RedirectedPosition(redirected_letter, redirected_index)

    def __str__(self):
        """Returns a upper case string containing the current rotors wiring position
           E.G. SUCAYWJLNPRTKXZBFDHVGMQEOI

        Args:
            None.

        Returns:
            A string.
        """  
        return "%s" % (self.writing)

    def __repr__(self):
        """Returns a string in the format [id, writing, notch=X, letter=X, ring=X]
           E.G. [III, SUCAYWJLNPRTKXZBFDHVGMQEOI, notch=V, letter=C, ring=I]

        Args:
            None.

        Returns:
            A string.
        """  
        return "[%s, %s, notch=%s, letter=%s, ring=%s]" % (self.id, 
            self.writing, self.notch, self.current_letter, self.ring_setting)

ROTORS = { 
    "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
}