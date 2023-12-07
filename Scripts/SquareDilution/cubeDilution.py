"""
    Méthode de stéganographie basée sur l'assignation des cubes, dont on altère les valeurs pour encrypter un message.
"""

import itertools

from PIL import Image
import random

import ohoui

import os
import sys
base_directory = os.getcwd()
pathColorDistinction = os.path.join(base_directory, 'ColorDistinction')
sys.path.append(pathColorDistinction)
import colorDistinction

class cubeImage():

    listeactual = []

    listecontole = []

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



    def checkBoard(self,square:list) -> bool:
        """
            Si les deux coordonnées sont paires, retourne True
            
            ==============================
            
            Regarde si l'addition des deux coordonnées modulo 2 donne 0 (Sinon donnerait 1 ou 2)

        """

        return ((square[0][0]/2)%2+(square[0][1]/2)%2)%2

    def checkCube(self,square:list) -> bool:
        """
            Vérifie la valeur d'un square, en prenant en compte toutes les couleurs, et inverse en fonction du board
            
            ==============================
            
            Additionne les bool de chaque couleur checkSquare et la bool du square sera équivalent à la majorité de bool des couleurs (T,T,F) -> T
            Puis applique les modifications d'inversion en fonction du checker board.
        """
        
        actualCubeValue = sum(self.checkSquare(square, i) for i in range(3)) <= 1
        
        return (actualCubeValue + (1 + self.checkBoard(square)))%2

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
            if random.randint(0,99) <= 69: #%
                
                fictiveValue[random.randint(0,2)] += 1
            
            if expectedValue != self.checkBoard(square):

                # Inverse les booléens
                fictiveValue = list(map(lambda x: not x,fictiveValue))
            
            for i in range(3):
                
                self.setSquareColor(square,bool(fictiveValue[i]),i)

    
    def __init__(self, sourcePath:str):
        
        self.source = Image.open(sourcePath)
        self.squares = self.getSquares()
        
        self.message = ""
    
    def encrypt(self,message:str):
        
        messageInstruction = ohoui.translateBinary(message)

        for i, (square, instruction) in enumerate(zip(self.squares,messageInstruction)):
            
            self.setCube(square,instruction)

    
    def decrypt(self):
        
        binaryList = [self.checkCube(square) for square in self.squares]
        
        decryptedMessage = ohoui.translateAlphabetical(binaryList)
        
        return decryptedMessage


def tempGetSquaresMoche(squareCoords:list):
    
    squares = [
        [(pos[0], pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
        for pos  in squareCoords
    ]
    
    return squares

def encryptMessage(message:str,sourcePath:str,returnpath:str,colorGradient:bool = False):

    image = cubeImage(sourcePath)
    if colorGradient:
        result = colorDistinction.getColorRange(colorRepartition = colorDistinction.getColorRepartition(),lengthOfMessage = 8 * len(message))
        image.squares = tempGetSquaresMoche(sorted(list(result[0]), key=lambda x: (x[0], x[1])))
    print(image.squares)
    image.encrypt(message)
    image.source.save(returnpath)
    
    if colorGradient:
        print("RESULTS",result[1],result[2])
        return result[1],result[2]

def decryptMessage(sourcePath:str,colorPick:tuple = None, tolerance:int = None) -> str:

    image = cubeImage(sourcePath)
    
    if colorPick and tolerance:
        image.squares = tempGetSquaresMoche(sorted(list(colorDistinction.getColorRange(colorRepartition = colorDistinction.getColorRepartition(), targetColor = colorPick, tolerance = tolerance)[0]), key=lambda x: (x[0], x[1])))
    
    message = image.decrypt()
    return message








