"""
Gestionnaire de mots de passe
"""

chemin = "users-data.txt"
separateur = "***---///5jkabd*****+++adion-"

def enregistrer():
    # Enregistrer un utilisateur
    username = input("Numéro de téléphone: ")
    pwd = input("Mot de passe: ")


    with open(chemin, "a") as fp:
        fp.write(f"{username}{separateur}{pwd}\n")

def lister():
    # Lister les utilisateurs
    with open(chemin, "r") as fp:
        contenu = fp.read()
        # print("Contenu: ", type(contenu), contenu)
        listeUtilisateurs = contenu.split("\n")
        # print("chaineCassee : ", listeUtilisateurs)

        for user in listeUtilisateurs:
            if user != '':
                data = user.split(separateur)
                tel = data[0]
                p = data[1]
                print(f"Utilisateur : {tel} {p}")


while True:
    choix = input("""
    ########## Gestionnaire de mot de passes\n
        1. Enregistrer
        2. Lister
        q: Quitter le programme
    """)
    if choix == '1':
        enregistrer()
    elif choix == '2' :
        lister()
    elif choix == 'q':
        break