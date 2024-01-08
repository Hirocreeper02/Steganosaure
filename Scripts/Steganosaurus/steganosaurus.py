import time

import cubeDilution



def userInterface():
    
    answer = input("Bonjour! Que souhaiteriez-vous effectuer comme action? \n([E] : Encrpyter, [D] : Décrypter)\n")
    
    if answer == "E":
        
        inputFileName = input("Veuillez donner le nom du fichier de l'image dans laquelle vous souhaiteriez cacher de l'information:\n")
    
        outputFileName = input("Veuillez donner le nom du fichier de sortie que vous souhaiteriez avoir:\n([ENTER] : Auto-généré, [NAME] : Nom, évitez les charactères spéciaux, et ne spécifiez pas le type du fichier)\n")

        message = input("Veuillez mettre votre message:\n")
        
        if not outputFileName: 
            
            from datetime import datetime
            
            outputFileName = inputFileName.split(".")
            outputFileName[0] += "_" + datetime.now().strftime("%d-%m-%Y")
            outputFileName[1] = "." + outputFileName[1]
            outputFileName = "".join(outputFileName)
            
            print(outputFileName)

        cubeDilution.encryptMessage(message,inputFileName,outputFileName)
        
        print(f"\nLe message a été encrypté avec succès dans le fichier {outputFileName}!")

    
    elif answer == "D":
        
        fileName = input("Veuillez donner le chemin d'accès du fichier d'entrée duquel vous souhaiteriez décrypter de l'information:\n")

        message = cubeDilution.decryptMessage(fileName)
        
        print("\nVotre message caché est:", message)


    else:
        
        print("\n[USER ERROR] L'UTILISATEUR A UTILISE UN CHARACTERE INTERDIT")
        
        return False



if __name__ == "__main__":
    userInterface()