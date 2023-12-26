from itertools import *

from PIL import Image
import random
import time

class colorMask():
    
    def __init__(self,source:Image):
        
        self.source = source
        # self.colorRepartition = self.getColorRepartition()
        self.colorRepartition = self.getColorRepartition()
        self.colorSet = set()
        self.colorPixelSet = {} # Dictionnaire des pixels compris dans le masque
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
    
    def _getRoundStep(self,numberOfBits:int) -> int:
        """
            [INTERNAL]
            
            Function that gives an int which will be used as roundStep in the rounding of the color dictionnary
            
            ==============================
            
            y = x // 10 + 1
        """
        
        return numberOfBits//10+1
    
    def _roundColorValue(self, reference:int, component:int, roundStep:int):
        """
            [INTERNAL]
            
            Round the value of a colour according to a roundStep, which will then be used in the rounded colorDictionnary
            
            ==============================
            
            Résultat -> 
            couleur                     # Target color
            - couleur mod(roundStep)    # We take only the rounded rest
            + reference%roundStep       # We take it to the closest rounded value of the target color
            ( - roundStep)              # If it's bigger than the reference component, take it down of a notch
        """
        
        result = component + (reference-component)%roundStep
        result -= roundStep * (result > component)
        
        return result
    
    def _roundColor(self,pixelColor:tuple,targetColor:tuple,roundStep:int) -> tuple:
        """
            [INTERNAL]
            
            Function that rounds every r,g,b value of a colour
            
            ==============================
            
            -
        """
        
        roundedColor = [
            self._roundColorValue(reference, component, roundStep)
            for reference, component in zip(targetColor, pixelColor)
        ]
        
        return tuple(roundedColor)
    
    def _customColorRepartition(self,targetColor:tuple,roundStep:int) -> dict:
        """
            [INTERNAL]
            
            Creates a dictionnary where the colours are grouped by rounding factor (thus decreasing the number of keys)
            
            ==============================
            
            -
        """
        
        print("ROUNDSTEP :",roundStep)
        
        repartition = {}
        
        print("SECURITY CHECK CCR :",len(self.colorRepartition))
        
        for color in self.colorRepartition:
            
            roundedColor = self._roundColor(color,targetColor,roundStep)
            
            if roundedColor not in repartition:
                
                repartition[roundedColor] = [self.colorRepartition[color]]
            
            else:
                
                repartition[roundedColor].append(self.colorRepartition[color])
        
        return repartition
    
    def _createRange(self,numberOfBits:int):
        """
            [INTERNAL]
            
            Calculates the range of colour which will be used to encrypt information
            
            ==============================
            
            -
        """
        
        targetColor = random.choice(list(self.colorRepartition))
        tolerance = 0
        toleranceIndicator = 0
        roundStep = self._getRoundStep(numberOfBits)
        
        actualColorRepartition = self._customColorRepartition(targetColor,roundStep)
        
        print("CUSTOMCOLORREPARTITION START :",len(actualColorRepartition))
        
        colorSet = {targetColor}
        
        containedBits = len(self.colorRepartition[targetColor])
        
        while containedBits < numberOfBits:
            
            tolerance += roundStep
            toleranceIndicator += 1

            print("LOOP WORK CHECK",toleranceIndicator)
                        
            voisins = {
                (
                    targetColor[0] + sign*(tolerance * i),
                    targetColor[1] + sign*(tolerance * j),
                    targetColor[2] + sign*(tolerance * k),
                )
                for sign, i, j, k in product(
                    (-1,1), (0,1), (0,1), (0,1)
                )
            }
            
            for color in voisins:
                
                if color in actualColorRepartition:
                    
                    containedBits += len(actualColorRepartition[color])
                    colorSet.add(color)
        
        colorPixelSet = {
            pixel
            for key in colorSet
            for pix in actualColorRepartition[key]
            for pixel in pix
        }
        
        print("PIXELS (REAL REFERENTIAL) #01 :",len(colorPixelSet),",",list(colorPixelSet)[0])
        
        self.colorSet = colorSet
        self.targetColor = targetColor
        self.tolerance = tolerance
        self.toleranceIndicator = toleranceIndicator
        self.colorPixelSet = colorPixelSet
        
        return colorPixelSet
    
    def _loadRange(self,targetColor:tuple,tolerance:int):
        """
            [INTERNAL]
            
            Reads the color range from a target color and a tolerance
            
            ==============================
            
            y = x // 10 + 1
        """
        
        print("TOLERANCE INDICATOR:",self.toleranceIndicator)
        
        roundStep = tolerance//self.toleranceIndicator
        
        actualColorRepartition = self._customColorRepartition(targetColor, roundStep)
        
        print("SELF TOLERANCE",roundStep)
        
        print("CUSTOMCOLORREPARTITION END :",len(actualColorRepartition))
        
        colorPixelSet = set()
        
        voisins = {
            (
                targetColor[0] + sign*(tolerance * i),
                targetColor[1] + sign*(tolerance * j),
                targetColor[2] + sign*(tolerance * k),
            )
            for sign, i, j, k in product(
                (-1,1), range(self.toleranceIndicator+1), range(self.toleranceIndicator+1), range(self.toleranceIndicator+1)
            )
        }
        
        for color in voisins:
            
            if color in actualColorRepartition:
            
                for pixel in actualColorRepartition[color]:
                    
                    for pix in pixel:
                        
                        colorPixelSet.add(pix)
        
        print("PIXELS (REAL REFERENTIAL) #02 :",len(colorPixelSet),",",list(colorPixelSet)[0])
        
        return colorPixelSet
    
    def getColorRange(self,lengthOfMessage:int = None,targetColor:tuple = None, tolerance:int = None, whiteNoise:int = 0) -> set:
        """
            Donne un ensemble de toutes les couleurs dans lesquelles on pourra crypter de l'information
            
            ==============================
            
            On prend une couleur aléatoire, et ensuite on vérifie quel ±x il faut mettre à la couleur pour pouvoir crypter l'intégralité du message, où le whiteNoise est la quantité de charactères intuiles qu'on installera pour brouiller le lecteur
        """
        
        if lengthOfMessage: # Si le message a une longueur = désir d'encryption (dans le cas contraire la longueur du message voulue serait inconnue)
            
            return self._createRange(lengthOfMessage + whiteNoise)
        
        else:
            
            return self._loadRange(targetColor,tolerance)


# myMask = colorMask(Image.open("Steganosaurus/kenan.jpeg"))
# # print(len(myMask.colorRepartition))
# # print(len(myMask._customColorRepartition((245,163,26),100)))
# print("\n######################\n##### ENCRYPTION #####\n######################\n")
# range1 = myMask.getColorRange(lengthOfMessage = 100)
# print(f"100 [expected] vs {(myMask.tolerance)} [given]")
# print("TARGET COLOR:", myMask.targetColor,"\n")
# print("######################\n##### DECRYPTION #####\n######################\n")
# range2 = myMask.getColorRange(targetColor = myMask.targetColor, tolerance = myMask.tolerance)
# print(" ")