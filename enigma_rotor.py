#-------------------------------------------------------------------------------
# Name:        enigma_rotor.py
#
# Notes:       Represents a rotor of the machine. Rotors had a fixed internal 
#              wiring and could be swapped out to allow various configurations.
#              The right most rotor would increment after each key press. If a
#              special notch letter was triggererd it would rotate the rotor to 
#              it's left
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
    ''' Represents a rotor of the machine. ROTORS had a fixed internal wiring and
        could be swapped out to allow various configurations. The right most rotor
        would increment after each key press. If a special notch letter was 
        triggererd it would rotate the rotor to it's left '''
    def __init__(self, id, writing, notch):
        self.id, self.writing, self.notch = id, writing, notch
        
        self.current_letter = 'A'
        self.alphabet = letters.ALPHABET_UPPER

    def is_in_notch_position(self):
        return (self.current_letter == self.notch)

    def is_in_post_notch_position(self):
        #TODO return (self.current_letter == letters.next_letter(self.notch))
        return self.current_letter == letters.shift_letter_up(self.notch, 1)

    def configure(self, letter, ring_setting='A'):
        # Rotate until we are in the desired letter position 
        while self.current_letter != letter:
            self.rotate()

        self.ring_setting = ring_setting

        # If the ring setting is 'A' it has no effect on the rotor's letter
        # redirection
        if ring_setting == "a" or ring_setting == "A":
            return
        else:
            # self.dot_position = letters.next_letter(self.dot_position) # TODO do I need the dot position
            


            # Shift all the letters in the wiring up based upon the ring setting's index
            shift_factor = letters.letter_to_index(self.ring_setting)
            shifted_alphabet = letters.shift_alphabet(shift_factor, True)
            shifted_writing = ''.join([letters.shift_letter_up(c, shift_factor) for c in self.writing])

            
            # create tuple of the new writing, take the second
            tmp = sorted([(shifted_alphabet[x], shifted_writing[x]) for x in range(26)])
            y = ''.join([letter[1] for letter in tmp])

            
            


            self.writing = y






    def rotate(self):
        ''' A rotor is a circular disc with so will always loop '''
        self.alphabet = self.alphabet[1:] + self.alphabet[:1]
        self.writing = self.writing[1:] + self.writing[:1]
        self.current_letter = self.alphabet[0]

    def redirect(self, input_index, reverse=False):
        # Have we hit the reflector?
        if reverse:
            redirected_letter = self.alphabet[input_index]
            redirected_index = self.writing.index(redirected_letter)
        else:
            redirected_letter = self.writing[input_index]
            redirected_index = self.alphabet.index(redirected_letter)

        return RedirectedPosition(redirected_letter, redirected_index)

    def __str__(self):
        return "%s" % (self.writing)

    def __repr__(self):
        return "[%s, %s, notch=%s, letter=%s, ring=%s]" % (self.id, 
            self.writing, self.notch, self.current_letter, self.ring_setting)

ROTORS = { 
    "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
}