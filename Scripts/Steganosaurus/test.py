from itertools import *

targetColor = (0,0,0)
tolerance = 0

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
