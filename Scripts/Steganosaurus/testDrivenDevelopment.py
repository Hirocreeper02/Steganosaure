import unittest
import PIL
import os
import cubeDilution


# chemin de base du dossier
base_directory = os.getcwd()


class TestAlphabet(unittest.TestCase):



    def setUp(self):

        self.message = "Hello World"

        self.message_coder = cubeDilution.translateBinary(self.message)

        self.message_decoder = cubeDilution.translateAlphabetical(self.message_coder)

        cubeDilution.encryptMessage(self.message,os.path.join(base_directory,"kenan.jpeg"),os.path.join(base_directory,"farouk.png"))

        self.message_decrypter = cubeDilution.decryptMessage(os.path.join(base_directory,"farouk.png"))



    def test_translateBinary(self):

        self.assertIsInstance(self.message_coder, list)

        for car in self.message_coder:

            self.assertLess(car, 2)



    def test_translateAlphabetical(self):

        self.assertIsInstance(self.message_decoder, str)

        self.assertEqual(self.message_decoder, self.message)



    def test_encryptMessage(self):

        self.assertTrue(os.path.join(base_directory,"farouk.png"))

        image1 = PIL.Image.open(os.path.join(base_directory,"kenan.jpeg"))
        image2 = PIL.Image.open(os.path.join(base_directory,"farouk.png"))

        self.assertEqual(image1.size, image2.size)

        differences_found = False

        for x in range(image1.width):
            for y in range(image1.height):
                pixel1 = image1.getpixel((x, y))
                pixel2 = image2.getpixel((x, y))
                if pixel1 != pixel2:
                    differences_found = True

        self.assertTrue(differences_found)



    def test_decryptMessage(self):

        self.assertIsInstance(self.message_decoder, str)

        self.assertEqual(self.message_decrypter[:len(self.message)], self.message)










if __name__ == "__main__":
    unittest.main()
