import sys
sys.path.append('C:/Users/Craig/Google Drive/Programming & Tech/Python/Python Experiments/Enigma Machine')

import unittest
import enigma_machine

unittest.TestLoader.sortTestMethodsUsing = None
class TestBug(unittest.TestCase):
    #---------------------------------------------------------------------------
    # Tests
    #---------------------------------------------------------------------------
    def test_01(self):
        em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
        em.set_rotors(["A", "A", "A"])
        em.set_plugboard("")
        expected, result = "AAAAA", em.encode_message('BDZGO') 
        self.assertEqual(expected, result)

    def test_02(self):
        em = enigma_machine.M3EnigmaMachine("UKW-B", ["I", "II", "III"])
        em.set_rotors(["A", "A", "A"])
        em.set_plugboard("")
        expected, result = "BDZGO", em.encode_message('AAAAA') 
        self.assertEqual(expected, result)

    def test_encrypt(self):
        em = enigma_machine.M3EnigmaMachine("UKW-C", ["IV", "V", "I"])
        em.set_rotors(["A", "B", "C"], ["Z", "Y", "X"])
        em.set_plugboard("Ab Cd Ef Gh Ij Kl Mn Op Qr St")
        
        result, expected = em.encode_message('hElLo'), 'ZZOTE'
        self.assertEqual(result, expected)

    def test_decrypt(self):
        em = enigma_machine.M3EnigmaMachine("UKW-C", ["IV", "V", "I"])
        em.set_rotors(["A", "B", "C"], ["Z", "Y", "X"])
        em.set_plugboard("Ab Cd Ef Gh Ij Kl Mn Op Qr St")
        
        result, expected = em.encode_message('zzote'), 'HELLO'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()