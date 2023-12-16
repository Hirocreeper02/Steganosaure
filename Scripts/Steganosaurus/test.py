from itertools import *

n = 10

valeurs = {(146, 160, 101): [(252, 22)], (129, 145, 74): [(252, 24)], (117, 133, 60): [(252, 26)], (105, 127, 62): [(252, 42)], (92, 117, 51): [(252, 48)], (83, 109, 46): [(252, 52)], (82, 107, 49): [(252, 56)], (73, 97, 45): [(252, 62)], (72, 100, 49): [(252, 64)], (52, 84, 34): [(252, 80)], (48, 80, 30): [(252, 82)], (68, 75, 42): [(252, 98), (254, 98)], (78, 81, 50): [(252, 104), (254, 104)], (120, 146, 81): [(252, 110)], (193, 199, 127): [(252, 144)], (182, 184, 111): [(252, 146)], (165, 174, 95): [(252, 148)], (161, 175, 90): [(252, 150)], (153, 179, 105): [(252, 156)], (157, 187, 117): [(252, 158)], (160, 183, 105): [(252, 176)], (109, 130, 51): [(252, 200)], (181, 202, 123): [(252, 204)], (94, 121, 26): [(252, 210)], (136, 166, 70): [(252, 212)], (124, 156, 59): [(252, 214)], (106, 140, 43): [(252, 216)], (99, 137, 38): [(252, 218)], (125, 165, 66): [(252, 220)], (104, 146, 46): [(252, 222)], (135, 163, 88): [(252, 224)], (123, 146, 74): [(252, 230)], (101, 127, 38): [(252, 246)], (109, 135, 46): [(252, 248)], (219, 229, 238): [(254, 6)], (198, 208, 217): [(254, 14)], (184, 190, 186): [(254, 16)], (175, 182, 164): [(254, 18)], (145, 159, 100): [(254, 22)], (128, 144, 73): [(254, 24)], (107, 122, 53): [(254, 28)], (95, 115, 52): [(254, 32)], (108, 130, 66): [(254, 42)], (91, 116, 51): [(254, 48)], (83, 109, 44): [(254, 50)], (80, 106, 43): [(254, 52)], (88, 114, 53): [(254, 54)], (90, 115, 57): [(254, 56)], (71, 95, 43): [(254, 60)], (57, 89, 39): [(254, 80)], (50, 82, 32): [(254, 82)], (63, 90, 47): [(254, 86)], (63, 83, 46): [(254, 90)], (72, 89, 55): [(254, 94)], (75, 89, 53): [(254, 96)], (69, 72, 43): [(254, 100)], (75, 84, 41): [(254, 106)], (126, 152, 87): [(254, 110)], (172, 193, 118): [(254, 132)], (172, 175, 104): [(254, 144)], (178, 178, 106): [(254, 146)], (177, 181, 104): [(254, 148)], (166, 178, 94): [(254, 150)], (148, 166, 82): [(254, 152)], (156, 182, 108): [(254, 156)], (149, 179, 109): [(254, 158)], (159, 181, 99): [(254, 176)], (165, 187, 105): [(254, 182)], (137, 159, 77): [(254, 188)], (166, 187, 108): [(254, 202)], (119, 144, 52): [(254, 208)], (107, 139, 40): [(254, 214)], (109, 145, 45): [(254, 216)], (109, 150, 48): [(254, 218)], (115, 157, 55): [(254, 220)], (126, 171, 68): [(254, 222)], (133, 161, 87): [(254, 224)], (121, 144, 76): [(254, 228)], (169, 195, 108): [(254, 240)], (158, 184, 95): [(254, 244)]}

repartition = {}

for couleur in valeurs:
    
    r,g,b = couleur[0]-couleur[0]%n,couleur[1]-couleur[1]%n,couleur[2]-couleur[2]%n
    
    if (r,g,b) not in repartition:
        
        repartition[(r,g,b)] = [valeurs[couleur]]
    
    else:
        
        repartition[(r,g,b)].append(valeurs[couleur])

# 5 : 140'608
# 1 : 