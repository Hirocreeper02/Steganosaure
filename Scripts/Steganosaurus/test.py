# from itertools import *

# def roundColorValue(reference:int,component:int,roundStep:int):
    
#     result = component + (reference-component)%roundStep
#     result -= roundStep * (result > component)
    
#     return result

# def roundColor(pixelColor:tuple,targetColor:tuple,roundStep:int) -> tuple:
#     """
#         Résultat -> 
#         couleur                     # Target color
#         - couleur mod(roundStep)    # We take only the rounded rest
#         + reference%roundStep       # We take it to the closest rounded value of the target color
#         ( - roundStep)              # If it's bigger than the reference component, take it down of a notch
#     """
    
#     roundedColor = [
#         roundColorValue(reference, component, roundStep)
#         for reference, component in zip(targetColor, pixelColor)
#     ]
    
#     return tuple(roundedColor)



# # for r,g,b in product(range(0,100,3),range(0,100,3),range(0,100,3)):

# #     print((r,g,b),"->",((r,g,b),(16,72,43),5))

# for i in range(100):
    
#     print(i,"->",roundColorValue(16,i,3))

encryption = {
    (189, 195, 189), 
    (178, 195, 178), 
    (178, 184, 178), 
    (178, 206, 189), 
    (178, 195, 200), 
    (189, 206, 200), 
    (178, 195, 189), 
    (178, 184, 189), 
    (167, 184, 178), 
    (189, 195, 200), 
    (189, 206, 189)
}

inconsistentEncryption = {
    (167, 195, 189),
    (167, 184, 189),
    (167, 195, 178),
    (178, 206, 200)
}

decryption = {
    (167, 184, 178),
    (178, 184, 178),
    (178, 184, 189),
    (178, 195, 178),
    (178, 195, 189),
    (178, 195, 200),
    (178, 206, 178),
    (178, 206, 189),
    (189, 184, 178),
    (189, 184, 189),
    (189, 195, 178),
    (189, 195, 189),
    (189, 195, 200),
    (189, 206, 178),
    (189, 206, 189),
    (189, 206, 200)
}

a = decryption - encryption
b = decryption - inconsistentEncryption

print(a, b)