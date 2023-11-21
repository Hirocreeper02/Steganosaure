"""
    Méthode de stéganographie basée sur l'assignation des cubes, dont on altère les valeurs pour encrypter un message.
"""

import itertools

from PIL import Image
import random

import ohoui

class cubeImage():

    ### METHODS ###

    def incrementColor(self,pixelColors:list,targetColor:int):
        """
            Incrémente de 1 la valeur de la couleur ciblée, afin d'éviter une valeur RGB > 255

            ==============================

            Si la valeur dépasse 255, on soustrait 1 au lieu d'ajouter 1
        """

        pixelColors[targetColor] += (1 - 2 *(pixelColors[targetColor]>=255))
        
        return pixelColors

    def incrementRandomPixel(self,square:list,targetColor:int) -> list:
        """
        Rend un pixel aléatoire de square impair (et retourne le square sans ce pixel)
        
        ==============================
        
        On met un pixel à une coordonnée aléatoire dont incrémente à la couleur voulue
        """
        
        # print("LEN SQUARE",len(square),square)
        randomCoord = random.choice(square)
        
        self.source.putpixel(randomCoord,tuple(self.incrementColor(list(self.source.getpixel(randomCoord)),targetColor)))
        squareCopy = square.copy()
        squareCopy.remove(randomCoord)

        return squareCopy

    ### ENCRYPTION METHODS ###

    def getSquares(self) -> list:
        """
            Divise l'image en carrés de 2x2 pixels.
        """
        
        squares = [
            [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            for y, x  in itertools.product(
                range(0, self.source.width, 2), range(0, self.source.height, 2)
            )
        ]
        
        return squares

    def checkSquare(self,square:list,targetColor:int) -> bool:
        """
            Vérifie si un carré a un nombre égal de valeurs paires et impaires sur la couleur souhaitée
            
            ==============================
            
            Pour chacun des quatres pixels, on additionne 1 si la couleur ciblée à une valeur impaire, sinon 0, et ensuite on vérifie si il y a bien deux nombres impairs et deux nombre pairs
        """

        return sum(self.source.getpixel(square[i])[targetColor]%2 for i in range(4)) == 2

    def setSquareColor(self,square:list,expectedValue:bool,targetColor:int):
        """
            Change la valeur d'un carré à la valeur voulue
            
            ==============================
            
            Pour chacun des quatres pixels, on additionne 1 si la couleur ciblée à une valeur impaire, sinon 0, et ensuite on vérifie si il y a bien deux nombres impairs et deux nombre pairs
        """
        
        actualValue = self.checkSquare(square,targetColor)
        
        if actualValue != expectedValue:
            
            if expectedValue == False:
                
                self.incrementRandomPixel(square,targetColor)
            
            else: # expectedValue == True
                
                for coord in square:
                    
                    pixelColor = list(self.source.getpixel(coord))
                    pixelColor[targetColor] -= pixelColor[targetColor]%2
                    self.source.putpixel(coord,tuple(pixelColor))
                
                self.incrementRandomPixel(self.incrementRandomPixel(square,targetColor),targetColor)

    def checkBoard(square:list) -> bool:
        """
            Si les deux coordonnées sont paires, retourne True si c'est le cas
            
            ==============================
            
            Regarde si l'addition des deux coordonnées modulo 2 donne 0 (Sinon donnerait 1 ou 2)
        """
        
        return sum((square[0][i]/2)%2 for i in range(2))%2 == 0

    def checkCube(self,square:list) -> bool:
        """
            Vérifie la valeur d'un square, en prenant en compte toutes les couleurs, et inverse en fonction du board
            
            ==============================
            
            Additionne les bool de chaque couleur checkSquare et la bool du square sera équivalent à la majorité de bool des couleurs (T,T,F) -> T
            Puis applique les modifications d'inversion en fonction du checker board.
        """
        
        actualCubeValue = sum(self.checkSquare(square, i) for i in range(3)) <= 2
        
        return (actualCubeValue + (1 - self.checkBoard(square)))%2

    def setCube(self,square:list,expectedValue:bool):
        """
            Vérifie la valeur d'un square, en prenant en compte toutes les couleurs, et inverse en fonction du board
            
            ==============================
            
            Additionne les bool de chaque couleur checkSquare et la bool du square sera équivalent à la majorité de bool des couleurs (T,T,F) -> T
            Puis applique les modifications d'inversion en fonction du checker board.
        """
        
        actualValue = self.checkCube(square)
        
        if actualValue != expectedValue:
            
            fictiveValue = [0,0,0]
            
            # Change un élément random pour ajouter du SWAG
            if random.randint(0,100) <= 70: #%
                
                fictiveValue[random.randint(0,2)] += 1
            
            print("SQUARRRREL",square,": [",fictiveValue,"]",expectedValue != self.checkBoard(square))

            if expectedValue != self.checkBoard(square):
                
                # Inverse les booléens
                fictiveValue = map(lambda x: not x,fictiveValue)
                print(fictiveValue,"DA FICTIVE VALUE")
            
            for i in range(3):
                
                print(bool(fictiveValue[i]),"iter",i)
                self.setSquareColor(square,bool(fictiveValue[i]),i)

    def __init__(self, sourcePath:str):

        self.source = Image.open(sourcePath)
        self.squares = self.getSquares()

        self.message = ""
        
    def encrypt(self,message:str):

        messageInstruction = ohoui.translateBinary(message)

        for i,instruction in enumerate(messageInstruction):

            self.setCube(self.squares[i],instruction)


def encryptMessage(message:list,sourcePath:str):

    image = cubeImage(sourcePath)
    image.encrypt(message)
    image.source.save("kenan.jpg")




# for i in range(10):

#     print("START | ", checkCube(squares[i]), ":", squares[i])

# for i,boolean in enumerate([True,False,True,False,True,False,True,False,True,False]):
#     setCube(squares[i],boolean)
#     print(i,"Iteration",squares[i],"\n       then",squares[i+1],"\n")

# for i in range(10):

#     print("END | ", checkCube(squares[i]), ":", squares[i])


