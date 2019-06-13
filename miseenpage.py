# coding: utf-8

import os
from tkinter import *
from functools import partial

global chaine
global existe
global nb_lignes
global saisie_nom_fichier
global contenu_fichier
global liste_mots



def lecture_fichier(nom_fichier) :
    fichier = open(nom_fichier, "r")
    contenu_fichier = fichier.read()
    fichier.close()
    
    while contenu_fichier[len(contenu_fichier)-1] == (" " or "\n"):
        contenu_fichier = contenu_fichier[:len(contenu_fichier)-1]
    

    

    return contenu_fichier 
    

def is_fichier ():
    
    
    nom_fichier = saisie_nom_fichier.get()
    if os.path.isfile(nom_fichier) :
        contenu_initial = lecture_fichier(nom_fichier)
        contenu = Label(top, text=contenu_initial, justify="left")
    else:
        # chemin fichier incorrect
        contenu = Label(top, padx=10, pady=5, text="Fichier inexistant")
    contenu.grid(column=0, row=1, columnspan=2)
    

def formatage_mots(chaine):

    global liste_mots
    
    # Remplacement de fins de ligne par des espaces
    contenu_sansretour = chaine.replace("\n"," ")
    chaine0 = contenu_sansretour[0]

    # Les caractères de ponctuation sont remplacés par des espaces
    ponctuation = ["'",'"',",",";",".","!","?","{","}","[","]","(",")"]
    for car in contenu_sansretour[1:]:
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


def calculglobal (contenu,wlabel):  
    
    
    nbcaracteres=len(contenu)
    nb_lignes= contenu.count("\n")
    listemots=formatage_mots(contenu)
    nb_mots = len(listemots)
    resultat=f'Le nombre total de caractères est {nbcaracteres}.\nLe nombre total de ligne est {nb_lignes}.\n'
    resultat+=f'Le nombre total de mot est {nb_mots}.'
    wlabel.config(text=resultat)
    

def traitementtextuel (wlabel, option):

    global contenu_fichier
    global liste_mots
    
    """
        Reçoit un itérable
        Crée un dictionnaire (clé=item de l'itérable ; valeur=liste(nboccurences;fréquence)
        Affiche par ordre décroissant d'occurences les items du dictonnaire convertit préalablement en liste
        dans un widget label
    """
    if option == 0:
        itera = contenu_fichier
    else :
        itera = liste_mots
        
    longmaxitem=0
    for k in itera :
        if len(k) > longmaxitem :
            longmaxitem=len(k)

    longueuriter=len(itera)
    print(itera)
    dicoiters={}
    for char in itera : #dico[0]=nb occurences ; dico[1]=fréquences
        dicoiters[char]=[0,0]
    for char in itera :
        dicoiters[char][0]=dicoiters[char][0]+1
        dicoiters[char][1]=dicoiters[char][0]/longueuriter*100
    listetriee= sorted(dicoiters.items(), key=lambda x: x[1][0], reverse=True)
    
    resultats=''
    for tuples in listetriee :
        resultats=resultats+f"{(longmaxitem-len(tuples[0]))*'  '}'{tuples[0]}' Nombre d\'occurences = {tuples[1][0]} et fréquence = {tuples[1][1]:>.2f} %\n"
    wlabel.config(text=resultats)

def traitementmots (contenu_fichier,wlabel):

    """
        Reçoit un texte
        Appel à la fonction traitementtextuel
    """
    
    listemots = formatage_mots(contenu_fichier)
    traitementtextuel(wlabel,1)
    
    
# Création de la fenêtre tkinter
top = Tk()
top.geometry("1000x1000")
top.title("Analyse d'un fichier texte")



# Création des widgets pour saisir le nom du fichier

# Étiquette
label_fichier = Label(top, padx=10, pady=5, text="Nom du fichier")
label_fichier.grid(column=0, row = 0)

# Zone de saisie du nom du fichier
nom_fichier = StringVar(top)
saisie_nom_fichier = Entry(top, textvariable=nom_fichier)
saisie_nom_fichier.grid(column=1, row=0)
saisie_nom_fichier.focus_set()

# Bouton de lecture du fichier
bouton_fichier = Button(top, text="Valider", padx=20, command=is_fichier)
bouton_fichier.grid(column=2, row=0)

# Contenu du fichier
contenu = Label(top, text="")
contenu.grid(column=0,row=1,columnspan=2)

# Boutons d'execution d'analyse

#création des widgets d'action
labelaction0=Label(top,text='',justify='left', anchor='nw')
boutonaction0=Button(top, text='Calculs globaux', command=partial(calculglobal,contenu_fichier,labelaction0))
labelaction1=Label(top,text='',justify='left', anchor='nw')
boutonaction1=Button(top, text='Nb d\'occurences et fréquences des caractères', command=partial(traitementtextuel,labelaction1,0))
labelaction2=Label(top,text='',justify='left', anchor='nw')
boutonaction2=Button(top, text='Nb d\'occurences et fréquences des mots', command=partial(traitementmots,labelaction2))

boutonaction0.grid(row=3, column=0)  
boutonaction1.grid(row=3, column=1)
boutonaction2.grid(row=3, column=2)
labelaction0.grid(row=4,column=0,sticky="n")
labelaction1.grid(row=4,column=1,sticky="n")
labelaction2.grid(row=4,column=2,sticky="n") 

top.mainloop()
