import itertools

from PIL import Image
import random

import string

#characters = list(string.printable)[]

source = Image.open("farouk.jpeg")

print(source.getpixel((10,10)))

color = 0

def getSquares():

    squares = [
        [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
        for x, y in itertools.product(
            range(0, source.width, 2), range(0, source.height, 2)
        )
    ]
    return squares

def checkSquare(square:list) -> bool:
    """
        Vérifie si un carré a un nombre égal de nombre pairs et impairs
    """
    
    counter = 0
    
    for i in range(4):
        if source.getpixel(square[i])[color]%2 == 0:
            
            counter += 1    
    
    if counter == 2:
        return True
    else: 
        return False

def addColorValue(pixelColor:list) -> list:
    pixelColor[color] += (1 - 2 *(pixelColor[color]==255))
    return pixelColor

def turnSquareValue(square:list,expectedValue:bool):
    
    print("PIPI",len(square))

    actualValue = checkSquare(square)
    
    if actualValue != expectedValue:
        
        if expectedValue == False:
            
            randomCoord = random.choice(square)
            pixelColor = list(source.getpixel(randomCoord))
            source.putpixel(randomCoord,tuple(addColorValue(pixelColor)))

        elif expectedValue == True:

            for coord in square:
                
                pixelColor = list(source.getpixel(coord))
                pixelColor[color] -= pixelColor[color]%2
                source.putpixel(coord,tuple(pixelColor))

            randomCoord1 = random.choice(square)
            pixelColor = list(source.getpixel(randomCoord1))
            source.putpixel(randomCoord1,tuple(addColorValue(pixelColor)))
            square.remove(randomCoord1)

            print(randomCoord1, ":", square)

            randomCoord2 = random.choice(square)
            pixelColor = list(source.getpixel(randomCoord2))
            source.putpixel(randomCoord2,tuple(addColorValue(pixelColor)))

            square.append(randomCoord2)




squares = getSquares()

for i in range(10):

    print("START | ", checkSquare(squares[i]), ":", squares[i])

for i,boolean in enumerate([True,False,True,False,True,False,True,False,True,False]):
    turnSquareValue(squares[i],boolean)

for i in range(10):

    print("END | ", checkSquare(squares[i]), ":", squares[i])



print("LONGUEUR:", list(string.printable))

print(len(squares))

#Image.new("RGB",256,256,(0,0,0))