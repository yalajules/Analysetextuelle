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

def formatage_mots(chaine):
    chaine0 = chaine[0]

    # Les caractères de ponctuation sont remplacés par des espaces
    ponctuation = ["'",'"',",",";",".","!","?","{","}","[","]","(",")"]
    for car in chaine[1:]:
        if car not in ponctuation :
            chaine0 += car
        else :
            chaine0 += " "
    # Les espaces qui se suivent sont remplacés par un seul espace
    chaine1 = chaine0.replace("  "," ")
    # Suppression des doubles espaces
    while len(chaine1) != len(chaine0):
        chaine0 = chaine1
        chaine1 = chaine0.replace("  "," ")
       
    # Une liste de mot est générée sous forme de liste
    liste_mots = chaine1.split(" ")
    # Si le dernier élément de la liste est vide
    if liste_mots[len(liste_mots)-1] == '':
        liste_mots.remove("")
    return liste_mots

texte, lignes = lecture_fichier()
mots = formatage_mots(texte)
nombre = len(mots)
print (nombre)



