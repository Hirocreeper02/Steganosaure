import itertools

from PIL import Image
import random

source = Image.open("bus_go_brrr.jpg")

abracadabric = 10

class Moreorlesssamecolor():
    """
        Martin Gremeaux-Bader (3M5) a nommé la classe. 
        Veuillez vous référer au 079 562 37 85 pour plus d'informations.
    """

    def __init__(self,interval,size):
        
        self.image = Image.new("RGBA",(source.width,source.height))
        self.interval = interval
        self.size = size
        self.abracadabroc = abracadabric

