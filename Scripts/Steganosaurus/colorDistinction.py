from itertools import *

from PIL import Image
import random
import time

class colorMask():
    
    def __init__(self,source:Image):
        
        self.source = source
        # self.colorRepartition = self.getColorRepartition()
        self.colorRepartition = self.getColorRepartition()
        self._actualColorRepartition = {}
        self.colorSet = set()
        self.targetColor = None
        self.tolerance = None 
    
    def getColorRepartition(self) -> dict:
        """
            Donne la liste de toutes les couleurs représentées dans l'image dans les clefs, et leur quantité dans les valeurs
            
            ==============================
            
            Pour chaque pixel, on ajoute 1 à la valeur associée à la clef portant le nom de la couleur
        """
        
        colorRepartition = {}
        
        for x,y in product(range(0,self.source.width,2),range(0,self.source.height,2)):
            
            tempColor = self.source.getpixel((x, y))
            
            if tempColor not in colorRepartition:
                
                colorRepartition[tempColor] = [(x, y)]
            
            else:
                
                colorRepartition[tempColor].append((x, y))
        
        return colorRepartition
    
    def _customColorRepartition(self,targetColor:tuple,numberOfBits:int) -> dict:
        
        repartition = {}
        roundStep = numberOfBits//10+1
        
        for color in self.colorRepartition:
            
            roundedColor = []
            
            for reference, component in zip(targetColor,color):
                
                result = component - component%roundStep + reference%roundStep
                result -= roundStep*(result >= component)
                
                roundedColor.append(result)
            
            roundedColor = tuple(roundedColor)
            
            if roundedColor not in repartition:
                
                repartition[roundedColor] = [self.colorRepartition[color]]
            
            else:
                
                repartition[roundedColor].append(self.colorRepartition[color])
        
        return repartition
    
    def _createRange(self,numberOfBits:int):
        
        # _actualColorRepartition = self._customColorRepartition(numberOfBits)
        
        targetColor = random.choice(list(self.colorRepartition))
        tolerance = 0
        
        colorSet = {targetColor}
        
        containedBits = len(self.colorRepartition[targetColor])
        
        while containedBits < numberOfBits:
            
            tolerance += 1
            
            voisins = {
                (
                    targetColor[0] + sign*(tolerance - i),
                    targetColor[1] + sign*(tolerance - j),
                    targetColor[2] + sign*(tolerance - k),
                )
                for sign, i, j, k in product(
                    range(-1,2,2), range(2), range(2), range(2)
                )
            }
            
            for color in voisins:
                
                if color in self.colorRepartition:
                    
                    containedBits += len(self.colorRepartition[color])
                    
                    for element in self.colorRepartition[color]:
                        
                        colorSet.add(element)
        
        self.colorSet = colorSet
        self.targetColor = targetColor
        self.tolerance = tolerance
    
    def _loadRange(self,targetColor:tuple,tolerance:int):
        
        print("La flemme, pas encore fait...")
    
    def getColorRange(self,lengthOfMessage:int = None,targetColor:tuple = None, tolerance:int = None, whiteNoise:int = 0) -> set:
        """
            Donne un ensemble de toutes les couleurs dans lesquelles on pourra crypter de l'information
            
            ==============================
            
            On prend une couleur aléatoire, et ensuite on vérifie quel ±x il faut mettre à la couleur pour pouvoir crypter l'intégralité du message, où le whiteNoise est la quantité de charactères intuiles qu'on installera pour brouiller le lecteur
        """
        
        if lengthOfMessage: # Si le message a une longueur = désir d'encryption (dans le cas contraire la longueur du message voulue serait inconnue)
            
            
            
            # toleranceLength = len(self.colorRepartition)
            
            self._createRange(lengthOfMessage + whiteNoise)
        
        else:
            
            self._loadRange(targetColor,tolerance)


myMask = colorMask(Image.open("Steganosaurus/bus.jpg"))
print(len(myMask.colorRepartition))
print(len(myMask._customColorRepartition((245,163,26),100)))
# myMask.getColorRange(8)

# print(myMask.colorSet)
# print(len(myMask.colorSet))

# for _ in range(10):
    
#     startTime = time.time(Image.open("Steganosaurus/jpg_wouhou.png"))
    
#     myMask = colorMask(Image.open("Steganosaurus/jpg_wouhou.png"))
    
#     endTime = time.time()
    
#     print("EXECUTION TIME:",endTime-startTime)