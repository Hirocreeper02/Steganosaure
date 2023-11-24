import os
import sys

#base_directory stock le chemin relatif jusqu'a Scripts
base_directory = os.getcwd()+"/Scripts"

# permet d'importer le fichier cubeDilution
pathcubeDilution = os.path.join(base_directory, 'SquareDilution')
sys.path.append(pathcubeDilution)
import cubeDilution as cubeD


cubeD.encryptMessage("Hello the world",os.path.join(base_directory, 'SquareDilution', "farouk.jpeg"),os.path.join(base_directory, 'SquareDilution', "kenan.jpeg"))
print("AND THE MESSAGE IS:",cubeD.decryptMessage(os.path.join(base_directory, 'SquareDilution', "kenan.jpeg")))


