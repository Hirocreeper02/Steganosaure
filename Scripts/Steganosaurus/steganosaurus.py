import time

import cubeDilution

import itertools
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

def massTimeTesting(numberOfTests:int,step:int = 1):
    
    with open("Steganosaurus/results.txt","w") as resultFile:
        for iteration in range(1,numberOfTests,step):
            
            print(iteration)
            
            for test in range(3):
                testMessage = generate_random_string(iteration)
                
                firstTime = time.time()
                
                cubeDilution.encryptMessage(testMessage,"Steganosaurus/kenan.jpeg","Steganosaurus/farouk.png")
                
                secondTime = time.time()
                
                decryptedMessage = cubeDilution.decryptMessage("Steganosaurus/farouk.png")
                
                thirdTime = time.time()
                
                resultFile.write(f"[{test}]LEN {iteration}: {secondTime-firstTime} s; {thirdTime-secondTime} s; {thirdTime-firstTime}\n")

# firstTime = time.time()

# cubeDilution.encryptMessage("HELLO THE WORLD! THIS VERSION IS SUPPOSED TO BE SLIGHTLY MORE OPTIMISED!!!","Steganosaurus/kenan.jpeg","Steganosaurus/farouk.png")

# secondTime = time.time()

# decryptedMessage = cubeDilution.decryptMessage("Steganosaurus/farouk.png")

# thirdTime = time.time()

# print(decryptedMessage)

# print(f"ENCRYPTION: {secondTime-firstTime} s\nDECRYPTION: {thirdTime-secondTime} s \n(TOTAL: {thirdTime-firstTime} s)")

def userInterface():
    
    answer = input("Bonjour! Que souhaiteriez-vous effectuer comme action? \n([E] : Encrpyter, [D] : Décrypter)\n")
    
    if answer == "E":
        
        inputFileName = input("Veuillez donner le nom du fichier de l'image dans laquelle vous souhaiteriez cacher de l'information:\n")
    
        outputFileName = input("Veuillez donner le nom du fichier de sortie que vous souhaiteriez avoir:\n([ENTER] : Auto-généré, [NAME] : Nom, évitez les charactères spéciaux, et ne spécifiez pas le type du fichier)\n")
        
        if not outputFileName: 
            
            from datetime import datetime
            
            outputFileName = inputFileName.split(".")
            outputFileName[0] += "_" + datetime.now().strftime("%d-%m-%Y")
            outputFileName[1] = "." + outputFileName[1]
            outputFileName = "".join(outputFileName)
            
            print(outputFileName)
        
        key = input("Veuillez donner votre clef confidentielle (ne divulger à personne):\n")
        
        while input(f"Confirmez-vous bien la clef '{key}'?\n([O] : Oui , [N] : Non)\n") != "O":
            
            key = input("Veuillez donner votre clef confidentielle (ne divulger à personne):\n")
        
        print(f"\nLe message a été encrypté avec succès dans le fichier {outputFileName}.png!")
        
        return True
    
    elif answer == "D":
        
        fileName = input("Veuillez donner le chemin d'accès du fichier d'entrée duquel vous souhaiteriez décrypter de l'information:\n")
        
        key = input("Veuillez donner votre clef confidentielle (ne divulger à personne):\n")
        
        while input(f"Confirmez-vous bien la clef '{key}'?\n([O] : Oui , [N] : Non)\n") != "O":
            
            key = input("Veuillez donner votre clef confidentielle (ne divulger à personne):\n")
        
        print("\nVotre message caché est:\n\n","MARTIIIIINNNNNNN")
        
        return True
    
    else:
        
        print("\n[USER ERROR] L'UTILISATEUR A UTILISE UN CHARACTERE INTERDIT")
        
        return False



if __name__ == "__main__":
    print("\n==============================\nEXECUTION OF MODULE STEGANOSAURUS AS SCRIPT\n==============================\n")
    
    userInterface()