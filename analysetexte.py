def traitementtextuel (objet):
    """
        Reçoit un itérable
        Crée un dictionnaire (clé=item de l'itérable ; valeur=liste(nboccurences;fréquence)
        Affiche par ordre décroissant d'occurences les objets du dicitonnaire convertit préalablement en liste
    """
    longueur=len(objet)
    dicoobjets={}
    for char in objet : #dico[0]=nb occurences ; dico[1]=fréquences
        dicoobjets[char]=[0,0]
    for char in objet :
        dicoobjets[char][0]=dicoobjets[char][0]+1
        dicoobjets[char][1]=dicoobjets[char][0]/longueur*100
    listetriee= sorted(dicoobjets.items(), key=lambda x: x[1][0], reverse=True)

    for tuple in listetriee :
        print(tuple[0],': Nombre d\'occurences =',tuple[1][0],'et fréquence = ',tuple[1][1])

def traitementmots (texte):
    """
        Reçoit un texte
        Appel à traitementtextuel
    """
    listemots=texte.split(' ')
    traitementtextuel(listemots)
    
 #Programme principal   
texte='bonjour, vous allez bien ?'
traitementtextuel(texte)
print()
traitementmots(texte)
