import os
import sys

#base_directory stock le chemin relatif jusqu'a Scripts
#base_directory = f"{os.getcwd()}/Scripts"
base_directory = os.getcwd() # Perso ça marche mieux

# permet d'importer le fichier cubeDilution
pathcubeDilution = os.path.join(base_directory, 'SquareDilution')
sys.path.append(pathcubeDilution)
import cubeDilution as cubeD


cubeD.encryptMessage("Hello world !!! je vais bien blabla",os.path.join(base_directory, 'SquareDilution', "farouk.jpeg"),os.path.join(base_directory, 'SquareDilution', "kenan.png"))

messagedecoder = cubeD.decryptMessage(os.path.join(base_directory, 'SquareDilution', "kenan.png"))
print("AND THE MESSAGE IS:",messagedecoder)

output = "76:càd§ÇgNM#Ncc"
for char1, char2 in zip("Hello world !!!", output):
    bin1 = list(cubeD.ohoui.OHOUIIIIIIIIIIII[char1])
    bin2 = list(cubeD.ohoui.OHOUIIIIIIIIIIII[char2])
    comparatif = ""
    for c1, c2 in zip(bin1, bin2):

        if int(c1) ^ int(c2) == 0:
            comparatif += " "
        else:
            comparatif += "1"

    #print("".join(bin1), ";", "".join(bin2), "->", comparatif)



