from itertools import *
import random

from PIL import Image

import colorDistinction


# Dictionnaire ASCIII customs:
OHOUIIIIIIIIIIII = {' ': '1010110', 'e': '0110011', 't': '0100111', 'n': '0000111', 's': '0100011', 'i': '1010001', 'a': '0011011', 'r': '1100011', 'u': '1110000', 'o': '0011101', 'l': '0001110', 'd': '0110101', 'c': '1010101', 'p': '0101011', 'm': '0011001', 'é': '1100001', 'q': '0110100', 'v': '0111000', '.': '0111001', 'f': '1111000', 'g': '1011100', 'h': '1001001', ',': '1100100', 'b': '0110010', 'è': '1000101', 'x': '1001011', 'à': '1001110', 'y': '0001111', '1': '1101000', 'L': '1011000', '-': '0011110', 'C': '0111100', '2': '1101100', '0': '1110001', '/': '0100101', 'j': '0010111', 'E': '1110100', 'P': '1101001', 'I': '1100101', 'z': '0011010', 'S': '1000111', '5': '1011010', '4': '0100110', '3': '0111010', 'k': '1010010', '[': '1001010', ']': '0010101', 'D': '1110010', 'w': '1100010', '9': '1000110', 'U': '1001100', 'T': '0101101', ':': '1010100', 'B': '0001011', '6': '1001101', '8': '1010011', 'M': '0110110', 'A': '1101010', 'W': '0010110', 'G': '1000011', 'F': '0010011', '7': '0110001', 'O': '0101001', 'ù': '0101100', 'Q': '0001101', 'R': '1011001', '?': '1100110', 'H': '0101110', 'V': '0011100', 'N': '0101010', '(': '0000011', ')': '0000101', '=': '0000110', 'Y': '0001001', 'J': '0001010', '%': '0001100', 'X': '0010001', 'K': '0010010', 'Z': '0010100', '+': '0011000', '!': '0011111', '"': '0100001', '#': '0100010', '$': '0100100', '&': '0101000', "'": '0101111', '*': '0110000', ';': '0110111', '<': '0111011', '>': '0111101', '@': '0111110', '\\': '1000001', '^': '1000010', '_': '1000100', '`': '1001000', '{': '1001111', '|': '1010000', '}': '1010111', '~': '1011011', 'Ç': '1011101', 'ü': '1011110', 'â': '1100000', 'ä': '1100111', 'ç': '1101011', 'ê': '1101101', 'ë': '1101110', 'ï': '1110011', 'î': '1110101', 'ì': '1110110', '\n': '1111001', 'É': '1111010', 'ô': '1111100', 'ö': '0000001', 'ò': '0000010', 'û': '0000100', 'Ö': '0001000', 'Ü': '0010000', 'ø': '0100000', '£': '0111111', '±': '1000000', '§': '1011111', '÷': '1101111', '°': '1110111', 'ß': '1111011', 'Ô': '1111101', 'È': '1111110', 'µ': '0000000', '’': '1111111'}
OHNOOOOOOOOONNNN = {'1010110': ' ', '0110011': 'e', '0100111': 't', '0000111': 'n', '0100011': 's', '1010001': 'i', '0011011': 'a', '1100011': 'r', '1110000': 'u', '0011101': 'o', '0001110': 'l', '0110101': 'd', '1010101': 'c', '0101011': 'p', '0011001': 'm', '1100001': 'é', '0110100': 'q', '0111000': 'v', '0111001': '.', '1111000': 'f', '1011100': 'g', '1001001': 'h', '1100100': ',', '0110010': 'b', '1000101': 'è', '1001011': 'x', '1001110': 'à', '0001111': 'y', '1101000': '1', '1011000': 'L', '0011110': '-', '0111100': 'C', '1101100': '2', '1110001': '0', '0100101': '/', '0010111': 'j', '1110100': 'E', '1101001': 'P', '1100101': 'I', '0011010': 'z', '1000111': 'S', '1011010': '5', '0100110': '4', '0111010': '3', '1010010': 'k', '1001010': '[', '0010101': ']', '1110010': 'D', '1100010': 'w', '1000110': '9', '1001100': 'U', '0101101': 'T', '1010100': ':', '0001011': 'B', '1001101': '6', '1010011': '8', '0110110': 'M', '1101010': 'A', '0010110': 'W', '1000011': 'G', '0010011': 'F', '0110001': '7', '0101001': 'O', '0101100': 'ù', '0001101': 'Q', '1011001': 'R', '1100110': '?', '0101110': 'H', '0011100': 'V', '0101010': 'N', '0000011': '(', '0000101': ')', '0000110': '=', '0001001': 'Y', '0001010': 'J', '0001100': '%', '0010001': 'X', '0010010': 'K', '0010100': 'Z', '0011000': '+', '0011111': '!', '0100001': '"', '0100010': '#', '0100100': '$', '0101000': '&', '0101111': "'", '0110000': '*', '0110111': ';', '0111011': '<', '0111101': '>', '0111110': '@', '1000001': '\\', '1000010': '^', '1000100': '_', '1001000': '`', '1001111': '{', '1010000': '|', '1010111': '}', '1011011': '~', '1011101': 'Ç', '1011110': 'ü', '1100000': 'â', '1100111': 'ä', '1101011': 'ç', '1101101': 'ê', '1101110': 'ë', '1110011': 'ï', '1110101': 'î', '1110110': 'ì', '1111001': '\n', '1111010': 'É', '1111100': 'ô', '0000001': 'ö', '0000010': 'ò', '0000100': 'û', '0001000': 'Ö', '0010000': 'Ü', '0100000': 'ø', '0111111': '£', '1000000': '±', '1011111': '§', '1101111': '÷', '1110111': '°', '1111011': 'ß', '1111101': 'Ô', '1111110': 'È', '0000000': 'µ', '1111111': '’'}

def translateBinary(message:str) -> list:
    """
        message textuel ==> liste de valeurs binaires
        
        Fonction servant à passer d'un message lettré à un message binaire
    """
    
    binaryList = [
        int(bit) 
        for char in message 
        if char in OHOUIIIIIIIIIIII 
        for bit in f"{OHOUIIIIIIIIIIII[char]}1"
        
    ]
    
    return binaryList

def translateAlphabetical(binaryList:list) -> str:
    """
        liste de valeurs binaires ==> message textuel
        
        Fonction servant à passer d'un message binaire à un message lettré
    """
    
    binaryList = [binaryList[i:i+8] for i in range(0, len(binaryList)-len(binaryList)%8, 8)] # Division en tronçons de 8 bits
    
    message = "".join(
        OHNOOOOOOOOONNNN["".join(str(int(value)) for value in binary[:7])]
        for binary in binaryList
        if binary[-1] # Si le dernier bit indique qu'il faut lire le charactère
    )
    
    return message

class cubeImage():
    """
        Classe contenant l'image d'encryption ainsi que toutes les méthodes y étant affiliées:
            -> encrypt()\n
            -> decrypt()\n
            -> getSquares()\n
            -> setSquare()\n
            -> checkSquare()
    """
    
    ################
    ### METHODES ###
    ################
    
    
    def _incrementColor(self,pixelColors:list,targetColor:int):
        """
            [PRIVEE]
            
            ==============================
            
            informations du pixel [list[int]]; couleur ciblée [int in [0,2]]
            
            -> incrémente de 1 la couleur ciblée (cas RGB > 255 compris)
            
            ==============================
            
            Si la valeur dépasse 255, on soustrait 1 au lieu d'ajouter 1
        """
        
        pixelColors[targetColor] += 1  - 2 * (pixelColors[targetColor]>=255)
        
        return pixelColors
    
    def _incrementRandomPixel(self,square:list,targetColor:int) -> list:
        """
            [PRIVEE]
            
            ==============================
            
            square ciblé; couleur ciblée
            
            -> incrémente de 1 un pixel aléatoire de la couleur ciblée du square; retourne le square sans ce pixel
            
            ==============================
            
            On met un pixel à une coordonnée aléatoire dont incrémente à la couleur voulue
        """
        
        randomCoord = random.choice(square)
        
        self.source.putpixel(randomCoord,tuple(self._incrementColor(list(self.source.getpixel(randomCoord)),targetColor)))
        squareCopy = square.copy()
        squareCopy.remove(randomCoord)
        
        return squareCopy
    
    def _getSquares(self) -> list:
        """
            [PRIVEE]
            Divise l'image en carrés de 2x2 pixels.
        """
        
        squares = [
            [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            for y, x  in product(
                range(0, self.source.width, 2), range(0, self.source.height, 2)
            )
        ]
        
        return squares
    
    ##################
    ### ENCRYPTION ###
    ##################
    
    def _checkSquare(self,square:list,targetColor:int) -> bool:
        """
            [PRIVATE]
            
            Verifies if a square has an equal number of even and uneven values on the targeted color
            
            ==============================
            
            Foreach one of the four pixels, we add 1 if the targeted value is uneven, otherwhise 0, and then we verify that the sum of the values is really 2
        """
        
        return int(sum(self.source.getpixel(pixel)[targetColor]%2 for pixel in square) == 2)
    
    def _checkCube(self,square:list) -> bool:
        """
            [PRIVATE]
            
            Checks the value of a square, taking into aconsideratiion the three color layers
            
            ==============================
            
            Adds up the bools of each color (r,g,b) in checkSquare, and the result of the three layers will be the majority of bools of the layers (T,T,F) -> T
        """
        
        return int(sum(self._checkSquare(square, i) for i in range(3)) >= 2)
    
    def _setSquare(self,square:list,expectedValue:int,targetColor:int,actualValue:list = None):
        """
            [PRIVATE]
            
            Changes the value of a square to the desired one
            
            ==============================
            
            For each one of the four pixels, we
            Pour chacun des quatres pixels, on additionne 1 si la couleur ciblée à une valeur impaire, sinon 0, et ensuite on vérifie si il y a bien deux nombres impairs et deux nombre pairs
        """
        
        if actualValue is None: # Si la valeur actual est nulle
            
            actualValue = self._checkSquare(square, targetColor) # On transfère actual value en temps normal, pour éviter les doubles calculs
        
        if actualValue != expectedValue:
            
            if expectedValue == False:
                
                self._incrementRandomPixel(square,targetColor)
            
            else: # expectedValue == True
                
                # Sortie de tuples (sous forme liste)
                pixelValues = [list(self.source.getpixel(pixel)) for pixel in square] 
                transformPixelValues = [value[targetColor]%2 for value in pixelValues]
                
                pixelCount = transformPixelValues.count(1)
                
                while pixelCount != 2:
                    
                    transformPixelValues[random.randint(0,2)] = (pixelCount < 2) # Nils peut optimiser
                    pixelCount = transformPixelValues.count(1)
                
                for i,(transformColor,actualColor) in enumerate(zip(transformPixelValues,pixelValues)):
                    
                    if transformColor != list(map(lambda x: x%2,actualColor)):
                        
                        actualColor[targetColor] = actualColor[targetColor] - actualColor[targetColor]%2 + transformColor
                        
                        self.source.putpixel(square[i],tuple(actualColor))
    
    def _setCube(self,square:list,expectedValue:bool):
        """
            [PRIVEE]
            
            Vérifie la valeur d'un square, en prenant en compte toutes les couleurs, et inverse en fonction du board
            
            ==============================
            
            Additionne les bool de chaque couleur checkSquare et la bool du square sera équivalent à la majorité de bool des couleurs (T,T,F) -> T
            Puis applique les modifications d'inversion en fonction du checker board.
        """
        
        actualValue = [self._checkSquare(square, i) for i in range(3)]
        transformValue = actualValue.copy()
        
        while transformValue.count(int(expectedValue)) < 2:
            transformValue[random.randint(0,2)] = int(expectedValue) # Peut optimiser par recherche de 0 [NILS]
        
        for i,value in enumerate(transformValue):
            
            self._setSquare(square,value,i,actualValue[i])
    
    #############################
    ### FONCTIONS UTILISATEUR ###
    #############################
    
    def __init__(self, sourcePath:str):
        
        self.source = Image.open(sourcePath)
        self.squares = self._getSquares()
    
    def encrypt(self, message:str):
        """
            message <- message à encrypter dans l'image
            
            Cette fonction sert à encrypter un message dans une image à l'aide de la méthode Stéganosaure
        """
        
        message = translateBinary(message)
        
        for square,instruction in zip(self.squares,message):
            
            self._setCube(square,instruction) # Pour chaque cube, modifie les couleurs pour obtenir l'instruction voulue (True/False)
    
    def decrypt(self) -> str:
        """
            return message <- message décrypté depuis l'image
            
            Cette fonction ser à décrypter le message dans l'image assignée à l'aide de la méthode Stéganosaure
        """
        
        message = translateAlphabetical([self._checkCube(square) for square in self.squares])
        
        return message

def tempGetSquaresMoche(squareCoords:list):
    
    squares = [
        [(pos[0], pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
        for pos  in squareCoords
    ]
    
    return squares

mask = colorDistinction.colorMask(Image.open("Steganosaurus/kenan.jpeg"))

def encryptMessage(message:str,sourcePath:str,returnPath:str,colorGradient:bool = False):

    image = cubeImage(sourcePath)
    if colorGradient:
        image.squares = tempGetSquaresMoche(sorted(list(mask.getColorRange(lengthOfMessage = 8 * len(message))), key=lambda x: (x[0], x[1])))
    image.encrypt(message)
    image.source.save(returnPath)
    
    if colorGradient:
        print("RESULTS")

def decryptMessage(sourcePath:str,colorPick:tuple = None, tolerance:int = None) -> str:

    image = cubeImage(sourcePath)
    
    if colorPick and tolerance:
        image.squares = tempGetSquaresMoche(sorted(list(colorDistinction.getColorRange(targetColor = mask.targetColor, tolerance = mask.tolerance))))
    
    message = image.decrypt()
    return message


encryptMessage("Hello","Steganosaurus/kenan.jpeg","Steganosaurus/kkkeeennnaaannn.png",True)
msg = decryptMessage()
print(msg)