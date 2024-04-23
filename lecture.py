"""
Manipulation des fichiers
"""

####" LECTURE #########################################
#######################################################

# Le fichier doit exister
# Le chemin peut être relatif ou absolu
cheminFichier: str = "harouna.txt"

# Seuls modes de lecture possibles:  r, r+
# r => Lecture en chaines de caractères
# r+ => Lecture en binaire
modeOuverture: str = "r" 

# Une erreur est levée si le fichier n'est pas accessible
# 1. Soit le chemin n'existe pas
# 2. Soit le programme n'a pas les en accès en lecture dans ce chemin

with open(cheminFichier, modeOuverture) as monFichier:
    contenu: str = monFichier.read()
    print("Contenu du fichier : ", contenu)

