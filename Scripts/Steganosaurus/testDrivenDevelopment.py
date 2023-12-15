import unittest
import PIL
import os
import cubeDilution


# chemin de base du dossier
base_directory = os.getcwd()
pathFarouk = os.path.join(base_directory,"farouk.png")
pathKenan = os.path.join(base_directory,"kenan.jpeg")


class TestCodeAndCrypte(unittest.TestCase):



    def setUp(self):

        self.message = "Hello World"

        self.message_coder = cubeDilution.translateBinary(self.message)

        self.message_decoder = cubeDilution.translateAlphabetical(self.message_coder)

        cubeDilution.encryptMessage(self.message,pathKenan,pathFarouk)

        self.message_decrypter = cubeDilution.decryptMessage(pathFarouk)



    def test_translateBinary(self):

        self.assertIsInstance(self.message_coder, list)

        for car in self.message_coder:

            self.assertLess(car, 2)



    def test_translateAlphabetical(self):

        self.assertIsInstance(self.message_decoder, str)

        self.assertEqual(self.message_decoder, self.message)



    def test_encryptMessage(self):

        self.assertTrue(pathFarouk)

        image1 = PIL.Image.open(pathKenan)
        image2 = PIL.Image.open(pathFarouk)

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



class TestCubeImage(unittest.TestCase):



    def setUp(self):

        self.Farouk = cubeDilution.cubeImage(pathFarouk)

        self.squares = self.Farouk._getSquares()

    #    self.imageorigine = PIL.Image.open(os.path.join(base_directory,"kenan.jpeg"))

        self.imageFarouk = PIL.Image.open(pathFarouk)

    def test_getSquares(self):

        self.assertIsInstance(self.squares, list)

        for i, square in enumerate(self.squares):

            self.assertEqual(self.squares[i][0][0] % 2, 0)

            self.assertEqual(self.squares[i][3][0] % 2, 1)


    def test_incrementColor(self):

        valeurTest = [53,0,255]

        for i in range(3):
            valeurTest = self.Farouk._incrementColor(valeurTest,i)
            

        self.assertIsInstance(valeurTest, list)

        self.assertEqual(valeurTest[0],54)

        self.assertEqual(valeurTest[1],1)

        self.assertEqual(valeurTest[2],254)


    def test_incrementRandomPixel(self):

        squareColor = []

        squareColorMod = []

        for i,square in enumerate(self.squares[0]):

            squareColor.append(self.imageFarouk.getpixel((self.squares[0][i])))

        listeReste = self.Farouk._incrementRandomPixel(self.squares[0],0)

        for i,square in enumerate(self.squares[0]):

            squareColorMod.append(self.imageFarouk.getpixel((self.squares[0][i])))

        self.assertIsInstance(listeReste, list)

        self.assertEqual(len(listeReste), 3)

        #print(self.squares[0],listeReste)
        a = int(str(set(self.squares[0]) - set(listeReste))[2])

        b = int(str(set(self.squares[0]) - set(listeReste))[-3])

        f = (a,b)

        print(squareColor, squareColorMod)

        #print((self.imageFarouk.getpixel(f)[0]+1,self.imageFarouk.getpixel(f)[1],self.imageFarouk.getpixel(f)[2]),squareColorMod)

        #self.assertIn(self.imageFarouk.getpixel(f)[0]+1, squareColorMod)











        








if __name__ == "__main__":
    unittest.main()
