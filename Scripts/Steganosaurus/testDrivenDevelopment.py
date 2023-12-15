import unittest
import sys
import cubeDilution




class Alphabet(unittest.TestCase):

    def setUp(self):

        self.message = "Hello World"

        self.messageCoder = cubeDilution.translateBinary(self.message)

        self.messageDecoder = cubeDilution.translateAlphabetical(self.messageCoder)
    
    def test_translateBinary(self):

        self.assertIsInstance(self.messageCoder, list)

        for car in self.messageCoder:

            self.assertLess(car, 2)

    def test_translateAlphabetical(self):

        self.assertIsInstance(self.messageDecoder, str)

        self.assertEqual(self.messageDecoder, self.message)







if __name__ == "__main__":
    unittest.main()
