from itertools import *

def roundColorValue(reference:int,component:int,roundStep:int):
    
    result = component + (reference-component)%roundStep
    result -= roundStep * (result > component)
    
    return result

def roundColor(pixelColor:tuple,targetColor:tuple,roundStep:int) -> tuple:
    """
        Résultat -> 
        couleur                     # Target color
        - couleur mod(roundStep)    # We take only the rounded rest
        + reference%roundStep       # We take it to the closest rounded value of the target color
        ( - roundStep)              # If it's bigger than the reference component, take it down of a notch
    """
    
    roundedColor = [
        roundColorValue(reference, component, roundStep)
        for reference, component in zip(targetColor, pixelColor)
    ]
    
    return tuple(roundedColor)



# for r,g,b in product(range(0,100,3),range(0,100,3),range(0,100,3)):

#     print((r,g,b),"->",((r,g,b),(16,72,43),5))

for i in range(100):
    
    print(i,"->",roundColorValue(16,i,3))