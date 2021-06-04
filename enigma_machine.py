#-------------------------------------------------------------------------------
# Name:        enigma_machine.py
#
# Notes:       A M3 Enigma machine implementation to encrypt / decrypt messages
#
#              I'd like to offer special mention to Mr. Elllis (hero) & my
#              Grandfather's 1948 Hamburg story he told me after taking me to
#              my first opera. Ariadne auf Naxos, Op. 60, by Richard Strauss
#
#              "Wehrmacht" was the unified armed forces of Germany from 1935 to
#              1945. It consisted of the Heer (army), the Kriegsmarine (navy)
#              and the Luftwaffe (air force).
#
#              The M3 was used by the army and the navy. Originally there were 
#              only 3 rotors but that was increased to a pool of 5 to choose 3
#              from. Later versions of the navys machine used more rotors
#              (4 rotors, from a selection of 8, and also featured double
#              notches).
#
#              Even though this device caused a lot of pain, it has an complexity,
#              simplicity and fascination that is wonderful. It's not the machines
#              fault.
#  
# Links:       See the accompanying text file
#
# TODO:
#-------------------------------------------------------------------------------

import sys
from collections import namedtuple

sys.path.append('../../Helper')
import letters

import enigma_reflector
import enigma_rotor
import enigma_plugboard

Position = namedtuple("Position", "letter index")

class M3EnigmaMachine:
    ''' Represents a M3 1940 era Enigma machine '''
    def __init__(self, reflectorID, rotorIDs = []):
        self.reflector = enigma_reflector.REFLECTORS[reflectorID]
        self.rotors = [enigma_rotor.ROTORS[id] for id in rotorIDs]
        self.plugboard = enigma_plugboard.Plugboard()

    def set_rotors(self, start_positions, ring_settings=['A','A','A']):
        ''' Also known as the Grundstellung (Ground Setting). Enigma machines 
            need to be in the right startup position in order to work (set-up right to left)'''
            #''also known as the rinsterlu
        self.rotors[2].configure(start_positions[2], ring_settings[2])
        self.rotors[1].configure(start_positions[1], ring_settings[1])
        self.rotors[0].configure(start_positions[0], ring_settings[0])

    def set_plugboard(self, plugs):
        ''' Sets up multiple plugs from a string in the format 'xx xx xx...' 
            E.g. 'bq cr di ej kw mt os px uz gh'
            Note: how many plugs are added is controlled by the plugboard module
        '''
        plugs = str.split(plugs)

        if len(plugs) == 0:
            self.plugboard.reset()
            return

        for plug in plugs:
            if len(plug) == 2:
                self.plugboard.add_plug(plug[0], plug[1])

    # keypress, move, change, alter, adjust
    def advance_state(self):
        ''' After a letter input change the machine by rotating the wheel on the right. This 
            then affects the rotor to it's left and so on. The left most wheel doesn't affect 
            the reflector 
            
            Notch turns rotor after encrypting '''
        self.rotors[2].rotate()
        if self.rotors[2].is_in_post_notch_position():
            self.rotors[1].rotate()
            if self.rotors[1].is_in_post_notch_position():
                 self.rotors[0].rotate()

    def encode_letter(self, letter, print_path=False):
        ''' Trace the path for a single letter. The rotors are advanced before 
            each letter is encripted. E.g. if you start the with the rotors set
            at AAZ then when the first letter of the message is encrypted the          
            rightmost rotor Z will have already rotated into the A position '''
        self.advance_state()

        path = [letter.upper()] # Convert to uppercase just to be safe
        # If there are plugs set, the plugboard is translated through before and after
        # the rotor stages
        letter = self.plugboard.reroute_letter(letter)
        pos = Position(letter, letters.letter_to_index(letter))
        path.append(pos.letter)

        # Go through the ROTORS right to left, this is how the historical machine worked
        for rotor in reversed(self.rotors):
            pos = rotor.redirect(pos.index)
            path.append(pos.letter)

        # Reflect
        pos = self.reflector.reflect(pos.index)
        path.append(pos.letter)

        # Go back left to right
        for rotor in self.rotors:
            pos = rotor.redirect(pos.index, True)
            path.append(pos.letter)

        # Final redirect into the lampboard
        pos = Position(letters.index_to_letter(pos.index), pos.index)
        path.append(pos.letter)

        # Go back through the plugboard
        letter = self.plugboard.reroute_letter(pos.letter)
        pos = Position(letter, letters.letter_to_index(letter))
        path.append(pos.letter)

        if print_path:
            print(path)          

        return pos.letter   

    def encode_message(self, message):
        ''' Encrypts a whole message '''
        encrypted_message = ''

        for letter in message:
            encrypted_message += self.encode_letter(letter)
            
        #TODO - for single line pythonesque 
        # return str([self.encode_letter(letter) for letter in message])
        return encrypted_message
        
    def __repr__(self):
        # TODO - add ring settings
        ''' No need to define str as the repr method is good enough '''
        return "[%s, %s:%s:%s, %s:%s:%s, %s:%s:%s]" % (self.reflector.id,
            self.rotors[0].id, self.rotors[0].current_letter, self.rotors[0].ring_setting,
            self.rotors[1].id, self.rotors[1].current_letter, self.rotors[1].ring_setting,
            self.rotors[2].id, self.rotors[2].current_letter, self.rotors[2].ring_setting)