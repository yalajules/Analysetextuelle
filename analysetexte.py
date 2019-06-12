def traitementtextuel (iter):
    """
        Reçoit un itérable
        Crée un dictionnaire (clé=item de l'itérable ; valeur=liste(nboccurences;fréquence)
        Affiche par ordre décroissant d'occurences les items du dictonnaire convertit préalablement en liste
    """
    longmaxitem=0
    for k in iter :
        if len(k) > longmaxitem :
            longmaxitem=len(k)

    longueuriter=len(iter)
    
    dicoiters={}
    for char in iter : #dico[0]=nb occurences ; dico[1]=fréquences
        dicoiters[char]=[0,0]
    for char in iter :
        dicoiters[char][0]=dicoiters[char][0]+1
        dicoiters[char][1]=dicoiters[char][0]/longueuriter*100
    listetriee= sorted(dicoiters.items(), key=lambda x: x[1][0], reverse=True)

    for tuple in listetriee :
        print(f"{tuple[0]:^3}  Nombre d\'occurences = {tuple[1][0]} et fréquence = {tuple[1][1]:>.2f} %")

def traitementmots (chaine):
    """
        Reçoit un texte
        Appel à la fonction traitementtextuel
    """
    listemots=texte.split(' ')
    traitementtextuel(listemots)
    
 #Programme principal   
texte='bonjour, vous allez bien ?'
traitementtextuel(texte)
print()
traitementmots(texte)
