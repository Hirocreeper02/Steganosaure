
OHOUIIIIIIIIIIII = {' ': '1010110', 'e': '0110011', 't': '0100111', 'n': '0000111', 's': '0100011', 'i': '1010001', 'a': '0011011', 'r': '1100011', 'u': '1110000', 'o': '0011101', 'l': '0001110', 'd': '0110101', 'c': '1010101', 'p': '0101011', 'm': '0011001', 'é': '1100001', 'q': '0110100', 'v': '0111000', '.': '0111001', 'f': '1111000', 'g': '1011100', 'h': '1001001', ',': '1100100', 'b': '0110010', 'è': '1000101', 'x': '1001011', 'à': '1001110', 'y': '0001111', '1': '1101000', 'L': '1011000', '-': '0011110', 'C': '0111100', '2': '1101100', '0': '1110001', '/': '0100101', 'j': '0010111', 'E': '1110100', 'P': '1101001', 'I': '1100101', 'z': '0011010', 'S': '1000111', '5': '1011010', '4': '0100110', '3': '0111010', 'k': '1010010', '[': '1001010', ']': '0010101', 'D': '1110010', 'w': '1100010', '9': '1000110', 'U': '1001100', 'T': '0101101', ':': '1010100', 'B': '0001011', '6': '1001101', '8': '1010011', 'M': '0110110', 'A': '1101010', 'W': '0010110', 'G': '1000011', 'F': '0010011', '7': '0110001', 'O': '0101001', 'ù': '0101100', 'Q': '0001101', 'R': '1011001', '?': '1100110', 'H': '0101110', 'V': '0011100', 'N': '0101010', '(': '0000011', ')': '0000101', '=': '0000110', 'Y': '0001001', 'J': '0001010', '%': '0001100', 'X': '0010001', 'K': '0010010', 'Z': '0010100', '+': '0011000', '!': '0011111', '"': '0100001', '#': '0100010', '$': '0100100', '&': '0101000', "'": '0101111', '*': '0110000', ';': '0110111', '<': '0111011', '>': '0111101', '@': '0111110', '\\': '1000001', '^': '1000010', '_': '1000100', '`': '1001000', '{': '1001111', '|': '1010000', '}': '1010111', '~': '1011011', 'Ç': '1011101', 'ü': '1011110', 'â': '1100000', 'ä': '1100111', 'ç': '1101011', 'ê': '1101101', 'ë': '1101110', 'ï': '1110011', 'î': '1110101', 'ì': '1110110', '\n': '1111001', 'É': '1111010', 'ô': '1111100', 'ö': '0000001', 'ò': '0000010', 'û': '0000100', 'Ö': '0001000', 'Ü': '0010000', 'ø': '0100000', '£': '0111111', '±': '1000000', '§': '1011111', '÷': '1101111', '°': '1110111', 'ß': '1111011', 'Ô': '1111101', 'È': '1111110', 'µ': '0000000', '’': '1111111'}
OHNOOOOOOOOONNNN = dict(zip([OHOUIIIIIIIIIIII[value] for value in OHOUIIIIIIIIIIII], list(OHOUIIIIIIIIIIII)))

# binMsg = ""

# for char in "Hello the world":

#     binMsg += OHOUIIIIIIIIIIII[char]

# print(binMsg)

def translateBinary(message:str) -> list:

    binaryList = []

    for char in message:

        if char in OHOUIIIIIIIIIIII:

            # boolList = [bool(int(boolean)) for boolean in OHOUIIIIIIIIIIII[char]]
            # print(boolList)

            binaryList.extend(
                int(boolean) for boolean in f"{OHOUIIIIIIIIIIII[char]}1"
            )

    return binaryList

def translateAlphabetical(binaryList:list) -> str:
    
    # On subdivise la liste en tronçons de 8
    binaryList = [binaryList[i:i+8] for i in range(0, len(binaryList), 8)]
    #print("LEN AVANT",len(binaryList))

    for i,binary in enumerate(binaryList):
        
        if binary[-1] == False or len(binary) != 8: # S'il y a l'instruction d'ignorer la lecture
            
            binaryList.pop(i)
        
        # else: # Sinon, on enlève l'instruction de lecture
            
        #     binaryList[i] = binaryList[i][:7]

    #print("LEN APRES",len(binaryList))
    
    message = ""
    
    for i,binary in enumerate(binaryList):
        
        # print("REAL LEN",len(binary))

        binaryList[i] = "".join(str(int(value)) for value in binaryList[i][:7])
        # print(binaryList[i])

        message += OHNOOOOOOOOONNNN[binaryList[i]]

    return message

#a = (translateBinary("Hi bro! How are you today? Does this code really work? (I think it doesn't, but I let you decide)"))

#print(a,translateAlphabetical(a))

#print(translateAlphabetical([False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True]))


#                                                                                                                               111010110010001000111000101 01001

#print(translateAlphabetical([True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True]))

print(translateBinary("ABC"))



