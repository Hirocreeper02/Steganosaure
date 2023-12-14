# Steganosaure
Steanosaurus Rex

	                                           011 1    1 010                                          
	                                              010 10    0    00 1                                   
	                                  1  011   1    11         111    1 1000                            
	                                 1 10  01 111  00          11     101                               
	                            0   1 00111   0010010          111   01   10                            
	                           00   000      0  10000    0     110                                      
	                                  1     11011011011100101 0100          01 01                       
	                       1   10 00  10  011101001101100111111000101000    001  1 10                   
	                             00010011001001                   1011010 010  10    0                  
	                    0 00    000111010                              10 011100     0                  
	        1   00     10 11  01001001                                   00  1000   1                   
	   0  000   010    1   100111                                               01 110  0               
	0   0  0 11 10   0 0  1100                  0000                             0010 11110             
	1  10   10 0 0 0001011              01    001  011     10                     10 01 1100            
	00     0110010101      000   001100101    1  1 01      1010  0111    0001          111011           
	0  11 010000010001101111011100101101100110101 011111000110100110110  00111      0      00111  1 011 
	       1  011   01001001101110   1 110 10 00100  11010 00000   01111101000110  1101100  100 0000000 
	                                     00001011011001111000101    1   10110  10010  1101100000 1011 1 
	                                      001011000 00100001000101      111011100 010    100  1 10      
	                                      000111110000  00111001110100110001101010 1   10               
	                                      1100110  1 001111 011011  0110111   1101 00 1                 
	                                    0001 1 00      0110 001    0 1010100  1  00100 1                
	                                    11 000          1  001       011010       01 000                
	                                 1111110            100100          0 11          0 10              
	                                   001               1101101        1 1 0       00000 0             
	                                  01 01              010100010     000 01101     0 1100             
	                                 1 0 0 11           0   0010 11     110   10  11   00011           
                                 
 # PROJET STEGANOSAURUS
 
 ## Descriptif
 Ce projet consiste en la création de différents algorithmes, nous permettant de faire de la stéganographie avec des images de type PNG. Nous avons donc défini deux méthodes, empruntant des chemins différents mais tout en ayant en tête un objectif commun. La première camoufle le message en se basant la répartition de groupes de pixels avec des valeurs de couleurs paires ou impaires, tandis que l'autre méthode se concentre sur une manière de trouver des régions de couleurs similaires dans l'image.
 
 ## Mode d'emploi
 
 
 ## CubeDilution
 Cette première méthode est celle qui se base sur les valeurs des pixels.
 On commence donc par séparer l'image en carrés de 2x2, pour chacun de ces carrés on calcule le modulo 2 de chacun des pixels pour une couleur bien spécifique. Si l'on a le même nombre de modulos égaux à 0 que de modulos égaux à 1, alors on attribue à la couleur que l'on considère la valeur **True**