
# checher methode python path commune

import sys
import os

sys.path.append('SquareDilution/')

import cubeDilution

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'input.txt')) as inputText:

    cubeDilution.encryptMessage("Hello the world","SquareDilution/farouk.jpeg")
    print("AND THE MESSAGE IS:",cubeDilution.decryptMessage("SquareDilution/kenan.jpeg"))


