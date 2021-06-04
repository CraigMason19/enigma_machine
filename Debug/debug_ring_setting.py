import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

import enigma_machine
import enigma_random as er

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

em = er.CreateRandomMachine()
# em = GetExactMachine()

print("Enigma Machine State...")
print(em)
print(em.rotors)
print(em.plugboard)
print()

x = em.encode_message('ggg')
print(x)