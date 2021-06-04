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

    def test_03(self):
        pass

if __name__ == '__main__':
    unittest.main()