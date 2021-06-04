import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

import enigma_machine

def normal_sequence():
    em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
    em.set_rotors(["A", "A", "U"])

    print("single step")

    for _ in range(4):
        print(f'\t{em}')
        em.encode_letter('X')

def test_single_notch():
    em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
    em.set_rotors(["A", "A", "U"])

    print("single notch")

    for _ in range(4):
        print(f'\t{em}')
        em.encode_letter('X')

def double_step_sequence():
    em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
    em.set_rotors(["A", "D", "U"])

    print("double step")

    for _ in range(5):
        print(f'\t{em}')
        em.encode_letter('X')


normal_sequence()
double_step_sequence()