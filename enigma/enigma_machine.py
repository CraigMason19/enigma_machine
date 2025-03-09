#-------------------------------------------------------------------------------
# Name:        enigma_machine.py
#
# Notes:       A M3 Enigma machine implementation to encrypt / decrypt messages
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
# Links:       See the accompanying text file
#
# TODO:
#-------------------------------------------------------------------------------

from collections import namedtuple
from copy import deepcopy

from enigma import letters

from enigma import enigma_reflector
from enigma import enigma_rotor
from enigma import enigma_plugboard

Position = namedtuple("Position", "letter index")

class M3EnigmaMachine:
    """Represents a M3 1940 era Enigma machine to encrypt/decrypt messages. 

    Attributes:
        reflector:
            A single Reflector class found in enigma_reflector.py
        rotors:
            A list of 3 Rotor classes found in enigma_rotors.py. 
        plugboard:
            A single Plugboard class found in enigma_plugboard.py.

    Methods:
        __init__(reflectorID, rotorIDs):
            Creates a new machine configuration, reflector and rotors don't 
            change once encryption begins.
        set_rotors(start_positions, ring_settings=['A','A','A']):
            Sets up the rotors configuration. If the ring settings are not set 
            they have no effect on the machine.
        set_plugboard(plugs):
            Sets up a plugboard with a minimum of 0 and a maximum of 10 plugs.
        _advance_state():
            Everytime a new letter is pressed, adjust the machine's rotor
            positions.
        encode_letter(letter, print_path=False):
            Only advance the machine once, can opt to show the letters path 
            if wanted.
        encode_message(message):
            Encrypts and returns a whole string.
        __repr__():
            Returns a string containg the machines relector, rotor id's, 
            position and ring states. Will NOT print the plugboard.
            [UKW-C, IV:G:L, I:H:Y, V:X:B]
    """
    def __init__(self, reflector_id, rotor_ids):
        """Creates a machine based just upon the reflector and rotors passed in. 
           Rotors will be set by default to the 'A' position Also creates
           an empty plugboard.

        Args:
            reflectorID.
                A string ID to load from the reflector global dictionary.
            rotorIDs
                A list of strings to load from the rotor global dictionary. 
                (set-up left to right, the right-most rotor is the fast rotor).

        Returns:
            None.
        """  
        self.reflector = enigma_reflector.REFLECTORS[reflector_id]
        self.rotors = [deepcopy(enigma_rotor.ROTORS[id]) for id in rotor_ids]
        self.plugboard = enigma_plugboard.Plugboard()

        self.set_rotors(['A','A','A'])

    def set_rotors(self, start_positions, ring_settings=['A','A','A']):
        """Rotate the wheels to the correct letter position. Also set's up the ring
           settings if they are pased in, if not, then the ring settings do nothing.

        Args:
            start_positions.
                A list of three letters to rotate each wheel too. Also known as the 
                Grundstellung (Ground Setting).
            ring_settings
                A list of three letters to indicate each wheels ring_setting. Also
                known as the Ringstellung (Ring Setting). Changes the internal
                wiring relative to the rotor.

        Returns:
            None.
        """  
        self.rotors[2].configure(start_positions[2], ring_settings[2])
        self.rotors[1].configure(start_positions[1], ring_settings[1])
        self.rotors[0].configure(start_positions[0], ring_settings[0])

    def set_plugboard(self, plugs):
        """Sets up multiple plugs from a string in the format 'xx xx xx...' 
           E.g. 'bq cr di ej kw mt os px uz gh' Note: Up to 10 connections 
           can be made.

        Args:
            plugs:
                A string containing the pairs of plugs to connect.

        Returns:
            None.
        """  
        plugs = str.split(plugs)

        if len(plugs) == 0:
            self.plugboard.reset()
            return

        for plug in plugs:
            if len(plug) == 2: # Has to be a paired connection
                self.plugboard.add_plug(plug[0], plug[1])

    def _advance_state(self):
        """After a letter has been input to the machine change the machine by
           rotating the wheel on the right. This then potentially affects the
           rotor to it's left based upon it's notch and so on. The left most 
           wheel doesn't rotate the reflector as the reflector is fixed. 

        Args:
            None.

        Returns:
            None.
        """  
        # The right-most or 'fast' wheel will always turn
        self.rotors[2].rotate()
        
        # If the fast rotor turns and the middle rotor is in the notch position 
        # then it will 'double step'
        if self.rotors[2].is_in_post_notch_position() or self.rotors[1].is_in_notch_position():
            self.rotors[1].rotate()
            # Normal turn of the middle wheel
            if self.rotors[1].is_in_post_notch_position():
                 self.rotors[0].rotate()

    def encode_letter(self, letter, print_path=False):
        """Trace the path for a single letter. The rotors are advanced before 
           each letter is encripted. E.g. if you start the with the rotors set
           at AAZ then when the first letter of the message is encrypted the          
           rightmost rotor will have already rotated into the A position. 

        Args:
            letter:
                The letter to be encrypted.
            print_path=False:
                Whether or not you wish to follow the route of the letter.

        Returns:
            The letter after encryption. Encrypted as below
            letter -> 
                plugboard ->
                    right, middle, left rotors ->
                        reflector ->
                            left, middle, right rotors
                                plugboard ->
                                    encrypted_letter
        """ 
        self._advance_state()

        # Convert to uppercase just to be safe  
        path = [letter.upper()] 

        # If there are plugs set, the plugboard is translated through before
        # and after the rotor stages
        letter = self.plugboard.reroute_letter(letter)
        pos = Position(letter, letters.letter_to_index(letter))
        path.append(pos.letter)

        # Go through the ROTORS right to left
        for rotor in reversed(self.rotors):
            pos = rotor.redirect(pos.index)
            path.append(pos.letter)

        # Reflect
        pos = self.reflector.reflect(pos.index)
        path.append(pos.letter)

        # Go back left to right through the inverse wiring
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
        """Encrypts a whole message of alphabetic characters. 

        Args:
            message:
                A string containing the message to be encrypted.

        Returns:
            A string containing the encoded message.
        """  
        encrypted_message = ''.join([self.encode_letter(letter) for letter in message])
        return encrypted_message
        
    def __repr__(self):
        """Returns a string showing the reflector and rotor states (id, position,
           ring settings). Will NOT print the plugboard.
           E.G. [UKW-C, IV:G:L, I:H:Y, V:X:B] 

        Args:
            None.

        Returns:
            A string showing the current state.
        """  
        return "[%s, %s:%s:%s, %s:%s:%s, %s:%s:%s %s]" % (self.reflector.id,
            self.rotors[0].id, self.rotors[0].current_letter, self.rotors[0].ring_setting,
            self.rotors[1].id, self.rotors[1].current_letter, self.rotors[1].ring_setting,
            self.rotors[2].id, self.rotors[2].current_letter, self.rotors[2].ring_setting, 
            self.plugboard)
