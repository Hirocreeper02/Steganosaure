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

massTimeTesting(100,10)



# firstTime = time.time()

# cubeDilution.encryptMessage("HELLO THE WORLD! THIS VERSION IS SUPPOSED TO BE SLIGHTLY MORE OPTIMISED!!!","Steganosaurus/kenan.jpeg","Steganosaurus/farouk.png")

# secondTime = time.time()

# decryptedMessage = cubeDilution.decryptMessage("Steganosaurus/farouk.png")

# thirdTime = time.time()

# print(decryptedMessage)

# print(f"ENCRYPTION: {secondTime-firstTime} s\nDECRYPTION: {thirdTime-secondTime} s \n(TOTAL: {thirdTime-firstTime} s)")