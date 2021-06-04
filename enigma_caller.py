#-------------------------------------------------------------------------------
# Name:        enigma_caller.py
#
# Notes:       Caller to scramble or unscramble messages from a WW2 M3 Enigma
#              machine.
#
# Links:       https://cryptii.com/pipes/enigma-machine
#
# TODO:
#-------------------------------------------------------------------------------

import re
from textwrap import wrap

from enigma_machine import M3EnigmaMachine
import enigma_random as er

def clean_message(message):
    ''' Cleans a message of non alphabetic characters and returns the result '''
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', message)

def format_message(message, grouping=5):
    ''' Formats a message by spliting it into blocks for easier reading '''
    return ' '.join(wrap(message, grouping))
    
# Let's setup the machine! 
def create_machine():
    ''' Insert the reflector and rotor combinations, align the wheels and setup
        the plugboard '''
    em = M3EnigmaMachine("UKW-B", ["I", "II", "III"])
    em.set_rotor_positions(["A", "A", "A"])
    em.set_plugboard('bq cr di ej kw mt os px uz gh')
    
    return em

def create_random_machine():
    ''' Setup random settings for the entire machine (reflector, rotors, ring 
        settings and plugboard) '''
    rem = M3EnigmaMachine(er.random_reflector(), er.random_rotors())
    rem.set_rotor_positions(er.random_start_positions(), er.random_ring_settings())
    rem.set_plugboard(er.random_plugboard())
    
    return rem

def main():
    # em = create_machine()
    em = create_random_machine()

    print("Enigma Machine State...")
    print(em)
    print(em.rotors)
    print(em.reflector)
    print(em.plugboard)
    print()

    message_text = ('ggggggggggggggggggggggggggggggggggggggggggggggggg'
                    'ggggggggggggggggggggggggggggggggggggggggggggggggg'
                    '123nkihklglglg lg lgu lg 1')
    clean_text = clean_message(message_text)
    encrypted_text = em.encode_message(clean_text)

    print(f'Original: {message_text}')
    print(f'Clean: {format_message(clean_text)}')
    print(f'Encrypted: {format_message(encrypted_text)}\n')

    print("Enigma Machine State...")
    print(em)
    
if __name__ == '__main__':
    main()