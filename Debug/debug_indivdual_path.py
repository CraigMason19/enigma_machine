import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

from collections import namedtuple
import enigma_rotor
import enigma_reflector

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Position = namedtuple("Position", "letter index")

r = [enigma_rotor.ROTORS['I'], enigma_rotor.ROTORS['II'], enigma_rotor.ROTORS['III']]
rf = enigma_reflector.REFLECTORS['UKW-B']

def smallpath(letter, positions = ''):
    r[0].configure(positions[0])
    r[1].configure(positions[1])
    r[2].configure(positions[2])

    x = Position(letter, ALPHABET.index(letter))
    print(f'Start --->', x)

    # Left to right rotors
    for i in reversed(range(3)):
        x = r[i].redirect(x.index)
        print(f'{r[i].id} --->', x)

    # REFLECT
    x = rf.reflect(x.index)
    print('REFLECT --->', x)

    for i in range(3):
        x = r[i].redirect(x.index, True)
        print(f'{r[i].id} --->', x)

    x = Position(ALPHABET[x.index], x.index)
    print('Final --->', x)


smallpath('G', 'AAA')