import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

import enigma_machine
import enigma_random as er

def GetRandomMachine():
    reflector = er.random_reflector()
    rotors = er.random_rotors()
    # positions = er.random_start_positions()
    positions = ["A", "A", "A"]
    rings = er.random_ring_settings()
    plugs = er.random_plugboard()

    em = enigma_machine.M3EnigmaMachine(reflector, rotors)
    em.set_rotors(positions, rings)
    em.set_plugboard(plugs)

    return em
# rotors = er.random_rotors()
# start_positions = er.random_start_positions()
# ring_settings = er.random_ring_settings()
# plugs = er.random_plugboard()

def GetExactMachine():
    reflector = "UKW-B"
    rotors = ["IV", "III", "II"]
    positions = ["A", "A", "A"]
    rings = ["G", "I", "T"]
    plugs = "bt ep fh qn sv yi lc dm aj kr"

    em = enigma_machine.M3EnigmaMachine(reflector, rotors)
    em.set_rotors(positions, rings)
    em.set_plugboard(plugs)

    return em

em = GetRandomMachine()
# em = GetExactMachine()


print("Enigma Machine State...")
print(em)
print(em.rotors)
print(em.plugboard)
print()

x = em.encode_message('ggg')
print(x)