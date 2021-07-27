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

unittest.TestLoader.sortTestMethodsUsing = None

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
    def test_00(self):
        em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
        em.set_rotors(["A", "A", "A"])
        em.set_plugboard("")
        
        result, expected = em.encode_message('aaaaa'), 'BDZGO'
        self.assertEqual(result, expected)

    def test_01(self):        
        em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
        em.set_rotors(["A", "A", "A"])

        result, expected = em.encode_message('bdzgo'), 'AAAAA'
        self.assertEqual(result, expected)





    # TODO Bug???
    def test_encrypt(self):
        em2 = enigma_machine.M3EnigmaMachine("UKW-C", ["IV", "V", "I"])
        em2.set_rotors(["A", "B", "C"], ["Z", "Y", "X"])
        em2.set_plugboard("Ab Cd Ef Gh Ij Kl Mn Op Qr St")
        
        result, expected = em2.encode_message('hElLo'), 'ZZOTE'
        self.assertEqual(result, expected)

    def test_decrypt(self):
        em = enigma_machine.M3EnigmaMachine("UKW-C", ["IV", "V", "I"])
        em.set_rotors(["A", "B", "C"], ["Z", "Y", "X"])
        em.set_plugboard("Ab Cd Ef Gh Ij Kl Mn Op Qr St")
        
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