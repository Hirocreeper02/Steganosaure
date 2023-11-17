from itertools import *

from PIL import Image
import random
import time

startTime = time.time()

source = Image.open("ColorDistinction/bus_go_brrr.jpg")

def getColorRepartition() -> dict:
    """
        Donne la liste de toutes les couleurs représentées dans l'image dans les clefs, et leur quantité dans les valeurs
        
        ==============================
        
        Pour chaque pixel, on ajoute 1 à la valeur associée à la clef portant le nom de la couleur
    """
    
    colorRepartition = {}
    
    for x, y in product(range(0,source.width,2),range(0,source.height,2)):
        
        tempColor = source.getpixel((x,y))
        
        if tempColor not in colorRepartition:
            
            colorRepartition[tempColor] = [(x,y)]
        
        else:
            
            colorRepartition[tempColor].append((x,y))
    
    return colorRepartition

def getColorRange(colorRepartition:dict,lengthOfMessage:int,whiteNoise:int = 0) -> set:
    """
        Donne un ensemble de toutes les couleurs dans lesquelles on pourra crypter de l'information
        
        ==============================
        
        On prend une couleur aléatoire, et ensuite on vérifie quel ±x il faut mettre à la couleur pour pouvoir crypter l'intégralité du message, où le whiteNoise est la quantité de charactères intuiles qu'on installera pour brouiller le lecteur
    """
    
    targetColor = random.choice(list(colorRepartition))

    toleranceIndicator = 0
    toleranceLength = len(colorRepartition[targetColor])
    toleranceSet = set()
    avoisinnantsOld = set()

    while toleranceLength <= lengthOfMessage + whiteNoise:
        
        toleranceIndicator += 1
        
        avoisinnants = set(
            product(
                range(
                    targetColor[0] - toleranceIndicator,
                    targetColor[0] + toleranceIndicator,
                ),
                range(
                    targetColor[1] - toleranceIndicator,
                    targetColor[1] + toleranceIndicator,
                ),
                range(
                    targetColor[2] - toleranceIndicator,
                    targetColor[2] + toleranceIndicator,
                ),
            )
        )
        
        for color in avoisinnants.difference(avoisinnantsOld):
            
            if color in colorRepartition:
                
                toleranceLength += len(colorRepartition[color])
                
                for element in colorRepartition[color]:
                    
                    toleranceSet.add(element)
        
        avoisinnantsOld = avoisinnants
    
    return toleranceSet

toleranceSet = getColorRange(getColorRepartition(),80)

print("TOLERANCE LENGTH",len(toleranceSet))

comparativeImage = Image.new("RGB",(source.width,source.height),(0,0,0))

for position in toleranceSet:
    
    comparativeImage.putpixel(position,(255,0,0))

comparativeImage.save("ColorDistinction/experiment2.jpg")

endTime = time.time()

print("TASKED FINISHED IN",endTime-startTime,"s")