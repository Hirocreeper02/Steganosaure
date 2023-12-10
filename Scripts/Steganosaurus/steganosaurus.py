import time

import cubeDilution

firstTime = time.time()

cubeDilution.encryptMessage("HELLO THE WORLD!","Steganosaurus/kenan.jpeg","Steganosaurus/farouk.png")

secondTime = time.time()

decryptedMessage = cubeDilution.decryptMessage("Steganosaurus/farouk.png")

thirdTime = time.time()

print(decryptedMessage)

print(f"ENCRYPTION: {secondTime-firstTime} s\nDECRYPTION: {thirdTime-secondTime} s \n(TOTAL: {thirdTime-firstTime} s)")
