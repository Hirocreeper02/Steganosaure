import os
import sys
import time

#base_directory stock le chemin relatif jusqu'a Scripts
#base_directory = f"{os.getcwd()}/Scripts"
base_directory = os.getcwd() # Perso ça marche mieux

# permet d'importer le fichier cubeDilution
pathcubeDilution = os.path.join(base_directory, 'SquareDilution')
sys.path.append(pathcubeDilution)
import cubeDilution as cubeD


# NORMAL TEST #

# cubeD.encryptMessage("Hello world !!! je vais bien blabla",os.path.join(base_directory, 'SquareDilution', "farouk.jpeg"),os.path.join(base_directory, 'SquareDilution', "kenan.png"))

# messagedecoder = cubeD.decryptMessage(os.path.join(base_directory, 'SquareDilution', "kenan.png"))
# print("AND THE MESSAGE IS:",messagedecoder)

# COLOR TEST #


# with open(os.path.join(base_directory, 'Main', "input.txt")) as textInput:
#     text = "".join(textInput.readlines())
#     print(len(text))

firstTime = time.time()

targetColor,tolerance = cubeD.encryptMessage("Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple.Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple. Cette phrase sert à montrer un exemple.",os.path.join(base_directory, 'ColorDistinction', "bus_go_brrr.jpg"),os.path.join(base_directory, 'SquareDilution', "kenan.png"))

# x/100 + 12 = nb de secondes d'éxécution python
# x/10000 + 12 =? nb de secondes d'éxécution C?

secondTime = time.time()

# messageDecoder = cubeD.decryptMessage(os.path.join(base_directory, 'SquareDilution', "kenan.png"),targetColor,tolerance)
messageDecoder = cubeD.decryptMessage(os.path.join(base_directory, 'SquareDilution', "kenan.png"))

thirdTime = time.time()

print(messageDecoder)

print(f"ENCRYPTION: {secondTime-firstTime} s\nDECRYPTION: {thirdTime-secondTime} s")

# output = "76:càd§ÇgNM#Ncc"
# for char1, char2 in zip("Hello world !!!", output):
#     bin1 = list(cubeD.ohoui.OHOUIIIIIIIIIIII[char1])
#     bin2 = list(cubeD.ohoui.OHOUIIIIIIIIIIII[char2])
#     comparatif = ""
#     for c1, c2 in zip(bin1, bin2):

#         if int(c1) ^ int(c2) == 0:
#             comparatif += " "
#         else:
#             comparatif += "1"

    #print("".join(bin1), ";", "".join(bin2), "->", comparatif)



