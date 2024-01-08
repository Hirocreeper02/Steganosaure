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
        self.colorSet = set()
        self.colorPixelSet = {} # Dictionnaire des pixels compris dans le masque
        self.targetColor = None
        self.tolerance = None
        self.forbidden = [(x, self.source.height - 2) for x in range(0,self.source.width-2,2)]
        self.colorRepartition = self.getColorRepartition()
    
    def getColorRepartition(self) -> dict:
        """
            Crée un dicitionnaire classant les pixels supérieurs gauche des squares par couleur
            
            => dictionnaire {(r,g,b):[pixel1,pixel2,...]}
        """
        
        colorRepartition = {}
        
        for x,y in product(range(0,self.source.width,2),range(0,self.source.height,2)):
            if (x,y) not in self.forbidden:
                tempColor = self.source.getpixel((x, y))
                
                if tempColor not in colorRepartition:
                    
                    colorRepartition[tempColor] = [(x, y)]
                
                else:
                    
                    colorRepartition[tempColor].append((x, y))
            else:
                pass
        
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
        
        repartition = {}
        
        
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
        
        colorSet = {targetColor}
        
        containedBits = len(self.colorRepartition[targetColor])
        
        while containedBits < numberOfBits:
            
            tolerance += roundStep
            toleranceIndicator += 1
                        
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
        
        roundStep = tolerance//self.toleranceIndicator
        
        actualColorRepartition = self._customColorRepartition(targetColor, roundStep)
        
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
        
        return colorPixelSet
    
    def getColorRange(self,lengthOfMessage:int = None,targetColor:tuple = None, tolerance:int = None, whiteNoise:int = 0) -> set:
        """
            Fonction gérant le désir de création ou de décryption d'un intervalle de couleur définissant le masque.
        """
        
        if lengthOfMessage: # Si le message a une longueur = désir d'encryption (dans le cas contraire la longueur du message voulue serait inconnue)
            
            return self._createRange(lengthOfMessage + whiteNoise)
        
        else:
            
            return self._loadRange(targetColor,tolerance)