"""
    Méthode de Distinction par Colorimétrie
    
    Ce module crée un masque de couleurs, dans lequel on cachera le message voulant être encrypté dans une image. Un masque de couleurs est un objet contenant la liste des squares (c.f. cubeDilution) dont la couleur du premier pixel est comprise dans l'intervalle (r±t, g±t, b±t), où r,g,b sont les valeurs d'une couleur arbitrairement choisie parmis celles de l'image dans laquelle on souhaite encrypter le message, et t est la tolérance vis-à-vis de cette couleur.
        
        EX: (r,g,b) = (116,72,227) ; t = 10 => Toutes les couleurs des pixels supérieurs gauches des squares de l'image comprises dans l'intervalle ([106;126];[62;82];[217;237]) feront partie du masque de couleurs
        
    Notons que t dépend de la taille du message voulant être encrypté (plus le message est gros, plus il faudra de pixels pour le cacher).
"""

from itertools import *

from PIL import Image
import random
import time

class colorMask():
    
    def __init__(self,source:Image):
        """
            Attribus par argument:
            - Source: image dans laquelle on va cacher le message

            Attributs autogénérés:
            - colorRepartition: dicitionnaire classant les pixels supérieurs gauche des squares par couleur
            - colorSet: ensemble qui contiendra l'ensembles des pixels faisant partie de la sélection du masque de couleurs
            - targetColor: couleur (r,g,b) arbitraire de l'image servant de point d'origine au masque
            - tolerance: tolerance t qui indique quel interval sera toléré autour de la targetColor (r,g,b)
        """
        
        self.source = source
        self.colorRepartition = self.getColorRepartition()
        self.colorSet = set()
        self.colorPixelSet = {} # Dictionnaire des pixels compris dans le masque
        self.targetColor = None
        self.tolerance = None 
    
    def getColorRepartition(self) -> dict:
        """
            Crée un dicitionnaire classant les pixels supérieurs gauche des squares par couleur
            
            => dictionnaire {(r,g,b):[pixel1,pixel2,...]}
        """
        
        colorRepartition = {}
        
        for x,y in product(range(0,self.source.width,2),range(0,self.source.height-2,2)):
            
            tempColor = self.source.getpixel((x, y))
            
            if tempColor not in colorRepartition:
                
                colorRepartition[tempColor] = [(x, y)]
            
            else:
                
                colorRepartition[tempColor].append((x, y))
        
        return colorRepartition
    
    ### ARRONDI DE DICTIONNAIRES ###
    """
        Cette partie sert à regrouper les pixels de ColorRerpartition en ensemble similaires, afin de grandement réduire la taille du dictionnaire à parcourir pour les longs messages
    """
    
    def _getRoundStep(self,numberOfBits:int) -> int:
        """
            [FONCTION PRIVEE]
            
            Sert à trouver le facteur d'arrondissement nécessaire à la colorRepartition en fonction de la taille du message voulant être encrypté (plus le message est gros, plus on arrondira les valeurs)
        """
        
        return numberOfBits//10+1
    
    def _roundColorValue(self, reference:int, component:int, roundStep:int):
        """
            [FONCTION PRIVEE]
            
            Sert à arrondir une couleur (r,g,b) donnée en une des clefs du dictionnaire aux couleurs arrondies, en prenant en compte le facteur d'arrondissement et le reste de la division de la TargetColor.
            
            V
            
            Résultat -> 
            couleur                     # Target color
            - couleur mod(roundStep)    # On ne prend que le reste arrondi
            + reference%roundStep       # On l'amène à la valeur la plus proche de la TargetColor
            ( - roundStep)              # Si la valeur est plus grande, on la décend d'un chouïa
            
            => int arrondi en fontion du roundtep
        """
        
        result = component + (reference-component)%roundStep
        result -= roundStep * (result > component)
        
        return result
    
    def _roundColor(self,pixelColor:tuple,targetColor:tuple,roundStep:int) -> tuple:
        """
            [FONCTION PRIVEE]
            
            Sert à arondir les trois valeurs colorimétriques d'une couleur (r,g,b) en utilisant la fonction _roundColorValue (qui elle n'arrondit qu'une seule des valeurs)
            
            => tuple (r,g,b) arrondi
        """
        
        roundedColor = [
            self._roundColorValue(reference, component, roundStep)
            for reference, component in zip(targetColor, pixelColor)
        ]
        
        return tuple(roundedColor)
    
    def _customColorRepartition(self,targetColor:tuple,roundStep:int) -> dict:
        """
            [FONCTION PRIVEE]
            
            Crée un dictionnaire où les différents clefs de ColorRepartition sont réunies par similitudes, avec un arrondi de plus en plus tolérant en fonction de la taille du message encrypté, réduisant ainsi grandement le parcours à effectuer dans ColorRepartition dans les futures fonctions d'encryption (ceci est donc une méthode d'optimisation majeure).
            
            => dictionnaire {(r,g,b):[pixel1,pixel2,...]}
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
            [FONCTION PRIVEE]
            
            Calcule l'intervalle de couleur nécessaire pour cacher l'image et en rend les différentes informations. Le return et simplement l'ensemble de tous les pixels faisant partie du colorMask.
            
            => colorSet = ((x,y),(x',y'),(x'',y''),...)
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
            [FONCTION PRIVEE]
            
            Redonne l'ensemble des pixels faisant partie d'un masque en fonction d'une couleur d'origine et une tolérance (servant ainsi à la décryption du masque).
            
            => colorSet = ((x,y),(x',y'),(x'',y''),...)

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
            Fonction gérant le désir de création ou de décryption d'un intervalle de couleur définissant le masque.
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
