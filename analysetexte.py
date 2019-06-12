from tkinter import *
from functools import partial

def action_boutonOK(wentry,wlabel):
    chemin=wentry.get()
    texteprovisoire='bonjour je vais à la maison'
    wlabel.config(text=texteprovisoire)
    

    
def calculglobal (wlabel,texte):
    nbcaracteres=len(texte)
    resultat=f'Le nombre de caractères est {nbcaracteres}.'
    wlabel.config(text=resultat)
    

def traitementtextuel (wlabel,iter):
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
    
    resultats=''
    for tuple in listetriee :
        resultats=resultats+f"{tuple[0]:^3} Nombre d\'occurences = {tuple[1][0]} et fréquence = {tuple[1][1]:>.2f} %\n"
    wlabel.config(text=resultats)

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

def traitementmots (wlabel,chaine):
    """
        Reçoit un texte
        Appel à la fonction traitementtextuel
    """
    listemots = formatage_mots(chaine)
    traitementtextuel(wlabel,listemots)
    
 #Programme principal   
Fenetre=Tk()
Fenetre.title('Analyse textuelle')

cheminsaisi=StringVar(Fenetre)
cheminsaisi.set('Entrez le chemin du fichier ici puis cliquez sur le bouton OK')
inputchemin=Entry(Fenetre, textvariable=cheminsaisi, width=100, bd=10, justify='center')
inputchemin.grid(row=0, column=0,columnspan=2)

textefichier=Label(Fenetre, text='')
textefichier.grid(row=1, column=0, columnspan=3)

boutonchemin = Button(Fenetre, text='OK', command=partial(action_boutonOK, inputchemin, textefichier))
boutonchemin.grid(row=0, column=2)



labelaction0=Label(Fenetre,text='')
boutonaction0=Button(Fenetre, text='Calculs globaux', command=partial(calculglobal,labelaction0,'bonjour, ça va ?'))
labelaction1=Label(Fenetre,text='')
boutonaction1=Button(Fenetre, text='Nb d\'occurences et fréquences des caractères', command=partial(traitementtextuel,labelaction1,'bonjour, ça va ?'))
labelaction2=Label(Fenetre,text='')
boutonaction2=Button(Fenetre, text='Nb d\'occurences et fréquences des mots', command=partial(traitementmots,labelaction2,'bonjour, ça va ?'))

boutonaction0.grid(row=2, column=0)  
boutonaction1.grid(row=2, column=1)
boutonaction2.grid(row=2, column=2)
labelaction0.grid(row=3,column=0)
labelaction1.grid(row=3,column=1)
labelaction2.grid(row=3,column=2) 
    

Fenetre.mainloop()
