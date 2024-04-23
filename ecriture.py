####" ECRITURE #########################################
#######################################################

# Le fichier PEUT NE PAS EXISTER
# Le chemin peut être relatif ou absolu
cheminFichier: str = "harouna.txt"

# w => On va écrire dans le fichier en chaines de caractères. L'ancien contenu sera remplacé.
# a => On va écrire dans le fichier en chaines de caractères. Le nouveau s'ajoutera à l'ancien.

modeOuverture: str = "w" 

chaine = "Bonjour Harouna"

with open(cheminFichier, modeOuverture) as monFichier:
    monFichier.write(chaine)
