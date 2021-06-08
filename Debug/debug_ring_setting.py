import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

import enigma_machine
import enigma_random as er

def GetExactMachine():
    reflector = "UKW-C"
    rotors = ["IV", "I", "V"]
    positions = ["G", "H", "X"]
    rings = ["L", "Y", "B"]
    plugs = "tk vf ag du bq jh ow sc nr py"

    em = enigma_machine.M3EnigmaMachine(reflector, rotors)
    em.set_rotors(positions, rings)
    em.set_plugboard(plugs)

    return em

# TODO - BUG??? MACHINE ROTORS ARE DIFFERENT
# em = er.create_random_machine()
em = GetExactMachine()

print("Enigma Machine State...")
print(em)
print(em.rotors)
print(em.plugboard)
print()

x = em.encode_message('randomtext')
print(x)