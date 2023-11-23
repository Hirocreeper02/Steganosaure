import random

with open("SquareDilution/jafa.txt") as stego:

    stegoText = stego.readlines()

    print(stegoText)

    for i,line in enumerate(stegoText):

        line = list(line)

        for j,char in enumerate(line):

            if char == "1" and random.randint(0, 1) == 0:
                line[j] = "0"

        stegoText[i] = "".join(line)

    print(stegoText)

    with open("SquareDilution/jafa2.txt","w") as stego:

        stego.writelines(stegoText)
