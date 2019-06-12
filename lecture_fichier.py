import os

def lecture_fichier() :
    fichier_existe = False
    # Tant que le fichier demandé n'existe pas
    while not fichier_existe:
        # Demande du nom du fichier à analyser
        nom_fichier = input("Donner le nom du fichier à analyser : ")
        # Vérification de l'existence du fichier
        fichier_existe = os.path.isfile(nom_fichier)
        if not fichier_existe :
            print ("Ce fichier n'existe pas, veuillez donner un autre nom de fichier:")
    #Ouverture du fichier
    fichier = open(nom_fichier, "r")
    #Lecture du fichier avec remplacement de passage à la ligne par des espace
    texte = fichier.read()
    #Comptage du nombre de retour à la ligne
    nb_lignes = texte.count("\n")
    # Remplacement de fins de ligne par des espaces
    texte = texte.replace("\n"," ")
    # Fermeture du fichier
    fichier.close()

    while texte[len(texte)-1] == " ":
        texte = texte[:len(texte)-1]
    return texte, nb_lignes

texte, lignes = lecture_fichier()
mots = formatage_mots(texte)
nombre = len(mots)
print (nombre)



