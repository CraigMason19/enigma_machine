#-------------------------------------------------------------------------------
# Name:        enigma_test.py
#
# Notes:       A test for various Enigma configurations
#
# Links:       https://cryptii.com/pipes/enigma-machine
#
# TODO:        
#-------------------------------------------------------------------------------

import unittest
import enigma_machine

class TestLetters(unittest.TestCase):
    #---------------------------------------------------------------------------
    # setUpClass and tearDownClass run before and after all tests, called once
    # NOTE - the camelCase syntax. Important that they are named this way.
    #---------------------------------------------------------------------------
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------
    def test_01(self):
        reflector = "UKW-B"
        rotors = ["I", "II", "III"]
        positions = ["A", "A", "A"]
        rings = ["A", "A", "A"]
        plugs = ""

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions, rings)
        em.set_plugboard(plugs)
        
        result, expected = em.encode_message('aaaaa'), 'BDZGO'
        self.assertEqual(result, expected)

    def test_02(self):
        reflector = "UKW-C"
        rotors = ["IV", "V", "I"]
        positions = ["A", "B", "C"]
        rings = ["Z", "Y", "X"]
        plugs = "Ab Cd Ef Gh Ij Kl Mn Op Qr St Uv Wx Yz" # Only use 10 pairs

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions, rings)
        em.set_plugboard(plugs)
        
        result, expected = em.encode_message('hElLo'), 'ZZOTE'
        self.assertEqual(result, expected)

    def test_single_step_01(self):
        reflector = "UKW-B"
        rotors = ["I", "II", "III"]
        positions = ["A", "A", "T"]

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions)
        
        expected, result = ['AAU', 'AAV', 'ABW', 'ABX'], []
        for _ in range(len(expected)):
            # Doesn't matter what is encoded, we are checking the rotor steps
            em.encode_letter('x') 
            result.append(''.join([rotor.current_letter for rotor in em.rotors]))

        self.assertEqual(result, expected)

    def test_double_step_01(self):
        reflector = "UKW-B"
        rotors = ["I", "II", "III"]
        positions = ["A", "D", "T"]

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions)
        
        expected, result = ['ADU', 'ADV', 'AEW', 'BFX', 'BFY'], []
        for _ in range(len(expected)):
            # Doesn't matter what is encoded, we are checking the rotor steps
            em.encode_letter('x') 
            result.append(''.join([rotor.current_letter for rotor in em.rotors]))

        self.assertEqual(result, expected)

    def test_double_step_02(self):
        reflector = "UKW-B"
        rotors = ["III", "II", "I"]
        positions = ["K", "D", "N"]

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions)
        
        expected, result = ['KDO', 'KDP', 'KDQ', 'KER', 'LFS', 'LFT', 'LFU'], []
        for _ in range(len(expected)):
            # Doesn't matter what is encoded, we are checking the rotor steps
            em.encode_letter('x') 
            result.append(''.join([rotor.current_letter for rotor in em.rotors]))

        self.assertEqual(result, expected)

    def test_double_step_03(self):
        reflector = "UKW-B"
        rotors = ["III", "II", "I"]
        positions = ["A", "D", "N"]

        em = enigma_machine.M3EnigmaMachine(reflector, rotors)
        em.set_rotors(positions)
        
        expected, result = ['ADO', 'ADP', 'ADQ', 'AER', 'BFS', 'BFT', 'BFU'], []
        for _ in range(len(expected)):
            # Doesn't matter what is encoded, we are checking the rotor steps
            em.encode_letter('x') 
            result.append(''.join([rotor.current_letter for rotor in em.rotors]))

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()