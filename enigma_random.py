import sys
sys.path.append('../../Helper')

import random
import letters

def random_reflector():
    return random.choice(["UKW-C", "UKW-B"])

def random_rotors():
    return random.sample(set(["I", "II", "III", "IV", "V"]), 3)

def random_start_positions():
    return [letters.random_upper_letter() for i in range(3)]

def random_ring_settings():
    return [letters.random_upper_letter() for i in range(3)]

def random_plugboard():
    alpha_list = list(letters.ALPHABET_UPPER)
    random.shuffle(alpha_list)

    i = iter(alpha_list[:20]) # Historically 10 pairs of plugs
    return ' '.join(a+b for a,b in zip(i, i))

def test_random_settings():
    print(f'Reflector: {random_reflector()}')
    print(f'Rotors: {random_rotors()}')
    print(f'Start positions: {random_start_positions()}')
    print(f'Ring settings: {random_ring_settings()}')
    print(f'Random plugboard: {random_plugboard()}')    

if __name__ == "__main__":
    test_random_settings()