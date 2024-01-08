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
Ce projet consiste en la création de différents algorithmes nous permettant de faire de la stéganographie avec des images de type PNG. Nous avons donc défini deux méthodes, empruntant des chemins différents mais tout en ayant en tête un objectif commun. La première (**CubeDilution**) camoufle le message en se basant sur la répartition de groupes de pixels représentant des bits d'information, tandis que la seconde (**ColorDistinction**) se concentre sur la manière de trouver des régions de couleurs similaires dans l'image, où dissimuler notre message.
 
## Mode d'emploi

Dans cette section, nous allons détailler la manière d'utiliser nos méthodes. Il y a deux façons de l'approcher, en tant que script ou en tant que module.

### Utilisation comme script
Il faut tout d'abord commencer par ouvrir le fichier **steganosaurus.py** (en faisant bien attention à avoir l'image dans le même dossier que le fichier où alors copier scrupuleusement le chemin d'accès au fichier).
Une fois que le fichier a été exécuté, il suffit de se laisser porter par les instructions.

### Utilisation comme module
Après avoir importé le fichier **cubeDilution.py**, il suffit d'appeler la foction **encryptMessage()** en lui passant comme arguments le message (sous forme de chaîne de caractères), le chemin pour accéder à l'image que l'on veut modifier et, finalement, le chemin de où stocker l'image modifiée. Ensuite, pour décrypter, utilisez la fonction **decryptMessage()** avec comme seul argument le chemin d'accès à l'image.
Si l'utilisateur désire tester nos fonctions, il le peut en runnant le fichier **testDrivenDevelopment.py** mais cela doit se faire depuis le terminal en utilisant cette commande : python3.11 relativepath/testDrivenDevelopment.py. Si il y a besoin de plus de detail, il doit mettre -v à la fin de la commande.

## Algorithmes
 
### CubeDilution
Cette première méthode est celle qui se base sur les carrés de pixels. On commence donc par séparer l'image en carrés de 2x2; à chacun de ces carrés est attribuée un bit d'information déterminé comme ceci. On s'intéresse à une couleur tout d'abord, en calculant le modulo 2 des valeurs de chacun des pixels. On obtient une liste de 4 éléments, des 0 ou des 1, on compte le nombre de 0 et s'il y en a 2 la couleur est considérée comme **True** pour la suite, sinon comme **False**. Après l'avoir fait sur chacune des couleurs (RGB) on obtient donc une liste de trois éléments de laquelle on tire la valeur booléenne qui vient en majorité. Et nous voilà donc avec une liste de booléens que l'on peut modifier à volonté, uniquement en changeant la parité de quelques pixels sur certaines couleurs, pour représenter un message.

Division en carrés : L'image est découpée en carrés de 2x2 pixels. Chaque carré est considéré comme une unité de base pour l'encryption.

Calcul des modulos : Pour chaque carré, le modulo 2 est calculé pour chaque pixel dans une couleur spécifique (R, G, ou B). Cela crée une série de valeurs binaires indiquant si la couleur de chaque pixel est paire (0) ou impaire (1).

Majorité des couleurs : En parcourant les trois couleurs du système RGB, une décision similaire est prise en prenant la majorité des valeurs booléennes attribuées à chaque couleur. Ainsi, chaque carré se voit attribuer une valeur booléenne pour l'ensemble de ses couleurs.

Assemblage du message : En combinant les valeurs attribuées à chaque carré, un message binaire est obtenu.
#### Implémentation
 Il faut tout d'abord transcrire le message que l'utilisateur désire dissimuler dans l'image en binaire (en utilisant un dictionnaire que l'on a créé afin de conserver approximativement le même nombre de 0 que de 1). C'est donc le rôle des fonctions **translateBinary** et **translateAlphabetical**. Nous avons cependant uniquement besoin de 7 bits pour encrypter tous les caractères que nous avons trouvé nécessaires, le choix a donc été fait d'utiliser ce huitième bit pour déterminer quels groupes de huit bits seront significatifs dans le message à décrypter et devront donc l'être.

 La méthode en elle même a été regroupée sous la forme d'une classe, simplifiant l'organisation des fonctions et améliorant leur relations. Il y a à l'intérieur de cette classe que dedux méthodes qui ne soient pas privées, donc auxquelles l'utilisateur doit avoir accès. Ce sont les méthodes d'encryption et de décryption.**encryptMessage** fonctionne de cette manière: on lui fournit un message à cacher dans une image, elle va donc chercher à modifier les cubes (les carrés dont on considère les 3 couleurs) en utilisant la méthode **_setCube**. Cependant cette dernière a elle même besoin de modifier la valeur du carré pour une couleur spécifique, la méthode **_setSquare**, et cette dernière a pour ce faire besoin d'une dernière méthode permettant de modifier le résultat du modulo 2 sur certains pixels, ce que fait **_incrementRandomPixel**.
 
### ColorDistinction
 Celle ci consiste à choisir au hasard une couleur de départ parmi toutes celles présentes dans l'image puis de déterminer l'intervalle sur les valeurs RGB des couleurs qui permet d'obtenir suffisamment d'espace pour encrypter tout le message fourni par l'utilisateur. Il s'agit ensuite d'utiliser les méthodes de l'algorithme précédent pour modifier les valeurs de quelques pixels et de donc stocker les informations qui nous seront nécessaires, mais donc uniquement dans les pixels/squares déterminés à la première étape avec l'intervalle.
 #### Implémentation
On commence par utiliser **getColorRepartition** pour obtenir l'ensemble des couleurs présentes sur l'image. Elles seront stockées dans un dictionnaire pour nous permettre d'associer à chaque couleur la liste de toutes les coordonnées des pixels de cette couleur. Cependant, pour conserver une taille de dictionnaire gérable, on utilise les méthodes **_getRoundStep**, qui nous donne l'intervalle auquel on va arrondir les valeurs, **_roundColorValue** qui arrondit une valeur à l'intervalle inférieur, et **_roundColor** qui applique la méthode sur le R, G et B de chaque pixel. Ces dernières permettent donc la création du dictionnaire simplifié par la méthode **_customColorRepartition** qui est, à part ce principe d'arrondi, très similaire à **getColorRepartition**.
Il faut après encore décider quelle partie du dictionnaire nous sera utile pour encrypter. Et ceci est le rôle de **_createRange**, où l'on commence par décider laquelle des couleurs sera notre couleur de référence qui sera de toute façcon inclue dans l'ensemble des couleurs retenues (un ensemble pour être sûr de ne pas prendre plusieurs fois la même couleur). On commence par notre couleur puis l'on s'éloigne de plus en plus jusqu'à avoir suffisamment de bits pour encrypter tout notre message.

## Journal de bord
- **[08.11.23-10.11.23] Emilien & Nils & Yoann :**
	
	Concepctualisation des idées des méthodes d'encryption et début du code.

- **[17.11.23] Emilien & Nils & Yoann :** 
	
	Conceptions des charactères et leur dictionnaire de traduction binaire.

- **[22.11.23-03.12.23] Emilien & Nils & Yoann :**
	
	Résolution d'un bug majeur de CubeDilution (Nils a gagné la cagnotte de 5.- pour avoir réussi à le résoudre).

- **[10.12.23] Emilien :** 
	
	Optimisation de CubeDilution

- **[14.12.23-26.12.23] Emilien :**
	
	Création et optimisation de ColorDistinction 

- **[15.12.23-29.12.23] Nils :**
	
	Rédaction des fonctions de test (à posteriori, mais en soit on avait déjà des petits bouts de code qui testaient par ci par là)

- **[14.12.23-08.01.23] Yoann :**
	
	Rédaction du README.md et documentation du code

- **[08.01.2023] Emilien & Nils & Yoann :**

	Peaufinage et résolution des bugs finaux, ainsi qu'implémentation de l'interface utilisateur par console.
