from itertools import *

from PIL import Image
import random
import time

startTime = time.time()

source = Image.open("SquareDilution/kenan.jpeg")

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

def getColorRange(colorRepartition:dict = None,lengthOfMessage:int = None,targetColor:tuple = None,tolerance:int = None,whiteNoise:int = 0) -> set:
    """
        Donne un ensemble de toutes les couleurs dans lesquelles on pourra crypter de l'information
        
        ==============================
        
        On prend une couleur aléatoire, et ensuite on vérifie quel ±x il faut mettre à la couleur pour pouvoir crypter l'intégralité du message, où le whiteNoise est la quantité de charactères intuiles qu'on installera pour brouiller le lecteur
    """
    
    if targetColor is None:
        targetColor = random.choice(list(colorRepartition))
    
    toleranceSet = set()
    avoisinnantsOld = set()
    
    # ENCRYPTION
    
    if lengthOfMessage is not None:
        
        toleranceLength = len(colorRepartition[targetColor])
        toleranceIndicator = 0
        
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
    
    else:
        
        for toleranceIndicator in range(tolerance + 1):
            
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
                    
                    for element in colorRepartition[color]:
                        
                        toleranceSet.add(element)
            
            avoisinnantsOld = avoisinnants
    
    print(targetColor, toleranceIndicator)
    
    return toleranceSet,targetColor,toleranceIndicator

# toleranceSet = getColorRange(getColorRepartition(),80)
# toleranceList = sorted(list(toleranceSet), key=lambda x: (x[0], x[1]))
# print(toleranceList)


# exampleSet = getColorRange(colorRepartition = getColorRepartition(), targetColor = (209,228,139), tolerance = 4)[0]
# exampleList = sorted(list(exampleSet), key=lambda x: (x[0], x[1]))
# print(exampleList)
# print(len(exampleList))
# print(len([(240, 554), (260, 600), (368, 602), (530, 772), (548, 804), (548, 826), (566, 776), (568, 832), (574, 770), (580, 746), (586, 708), (602, 814), (604, 916), (658, 494), (702, 468), (728, 608), (736, 540), (744, 362), (746, 360), (746, 414), (752, 626), (766, 588), (790, 568), (800, 476), (822, 298), (824, 570), (824, 572), (836, 10), (838, 102), (860, 454), (862, 454), (872, 538), (916, 510), (926, 112), (948, 64), (950, 464), (952, 64), (958, 496), (960, 554), (968, 482), (976, 494), (998, 126), (1000, 234), (1022, 518), (1032, 172), (1056, 186), (1084, 438), (1108, 62), (1124, 332), (1136, 68), (1154, 124), (1154, 254), (1162, 250), (1162, 324), (1200, 330), (1230, 156), (1250, 202), (1260, 276), (1282, 84), (1286, 80), (1292, 156), (1312, 150), (1380, 104), (1568, 62), (1572, 64), (1582, 42), (1696, 12), (2134, 12), (2134, 20), (2208, 88), (2214, 78), (2236, 32), (2286, 112), (2294, 122), (2324, 80), (2332, 96), (2366, 552), (2398, 76), (2402, 112), (2410, 196), (2442, 114), (2446, 82), (2448, 106), (2478, 72), (2488, 168), (2508, 120), (2512, 96), (2534, 54), (2546, 162), (2562, 68), (2586, 70), (2588, 22), (2612, 344), (2616, 374), (2628, 510), (2634, 38), (2636, 94), (2640, 32), (2644, 38), (2644, 146), (2660, 662), (2676, 34), (2676, 46), (2678, 156), (2680, 32), (2682, 302), (2688, 478), (2706, 16), (2726, 40), (2730, 386), (2732, 6), (2752, 138), (2760, 216), (2764, 40), (2798, 92), (2802, 20), (2802, 146), (2804, 700), (2808, 6), (2830, 2), (2830, 16), (2840, 20), (2878, 110), (2968, 4), (2972, 80), (3040, 98), (3174, 272)]))

# print("TOLERANCE LENGTH",len(toleranceSet))

# comparativeImage = Image.new("RGB",(source.width,source.height),(0,0,0))

# for position in toleranceSet:
    
#     comparativeImage.putpixel(position,(255,0,0))

# comparativeImage.save("ColorDistinction/experiment2.jpg")

# endTime = time.time()

# print("TASKED FINISHED IN",endTime-startTime,"s")