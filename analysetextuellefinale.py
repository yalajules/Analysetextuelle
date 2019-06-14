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

def formatage_mots(chaine):

    global liste_mots
    
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

def lecture_fichier(nom_fichier) :

    global contenu_fichier
    global contenu_fichier2
    
    #Ouverture du fichier
    fichier = open(nom_fichier, "r")
    #Lecture du fichier avec remplacement de passage à la ligne par des espace
    contenu_fichier = fichier.read()

    # Suppression des sauts de lignes et espaces inutiles
    contenu_fichier.strip("n")
#    print (ord(contenu_fichier[0]))
    if ord(contenu_fichier[0]) == 10:
        print ("10")
        contenu_fichier = contenu_fichier[1:]
#    print(contenu_fichier)
    # Les espaces qui se suivent sont remplacés par un seul espace
    chaine0 = contenu_fichier
    chaine1 = chaine0.replace("\n\n","\n")
    # Suppression des doubles espaces
    while len(chaine1) != len(chaine0):
        chaine0 = chaine1
        chaine1 = chaine0.replace("\n\n","\n")
        
    contenu_fichier = chaine1

    nb_lignes = contenu_fichier.count("\n")
    # Fermeture du fichier
    fichier.close()

    #Les sauts de lignes sont remplacés par des espaces
    contenu_fichier0 = contenu_fichier
    contenu_fichier2 = contenu_fichier.replace("\n"," ")

    # Génération de la liste des mots
    listemots = formatage_mots(contenu_fichier2)
    
    return contenu_fichier0, nb_lignes

def is_fichier ():
    global nb_lignes
    global saisie_nom_fichier
    global contenu_fichier
    
    nom_fichier = saisie_nom_fichier.get()
    # Si le fichier est trouvé
    if os.path.isfile(nom_fichier) :
        # Lecture du contenu du fichier
        contenu_fichier, nb_lignes = lecture_fichier(nom_fichier)
        foreground = "black"
    else:
        # Etiquette fichier absent
        contenu_fichier="Fichier inexistant"
        foreground = "red"
    contenu.config(text=contenu_fichier, fg = foreground)

def calculglobal (wlabel):

    global contenu_fichier
    global nb_lignes
    global liste_mots

    print(liste_mots)
    nbcaracteres=len(contenu_fichier)
    nb_mots = len(liste_mots)
    resultat=f'Le nombre total de caractères est {nbcaracteres}.\nLe nombre total de lignes est {nb_lignes}.\n'
    resultat+=f'Le nombre total de mots est {nb_mots}.'
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
    dicoiters={}
    for char in itera : #dico[0]=nb occurences ; dico[1]=fréquences
        dicoiters[char]=[0,0]
    for char in itera :
        dicoiters[char][0]=dicoiters[char][0]+1
        dicoiters[char][1]=dicoiters[char][0]/longueuriter*100
    listetriee= sorted(dicoiters.items(), key=lambda x: x[1][0], reverse=True)
    
    resultats=''
    for tuple1 in listetriee :
        if tuple1[0] == " ":
#        resultats=resultats+f"'{tuple[0]}' Nombre d\'occurences = {tuple[1][0]} et fréquence = {tuple1[1][1]:>.2f} %\n"
            resultats=resultats+f"'{tuple1[0]}' Nombre d\'occurences = {tuple1[1][0]-(nb_lignes-1)} et fréquence = {tuple1[1][1]:>.2f} %\n"
        elif tuple1[0]!= "\n":
            resultats=resultats+f"'{tuple1[0]}' Nombre d\'occurences = {tuple1[1][0]} et fréquence = {tuple1[1][1]:>.2f} %\n"
    wlabel.config(text=resultats)

def traitementmots (wlabel):

    """
        Reçoit un texte
        Appel à la fonction traitementtextuel
    """
    global contenu_fichier
    
    listemots = formatage_mots(contenu_fichier)
    traitementtextuel(wlabel,1)
    
    
# Création de la fenêtre tkinter
top = Tk()
top.geometry("900x600")
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
contenu = Label(top, text="Aucun fichier n'a été lu",justify='left', anchor='nw')
contenu.grid(column=0,row=1,columnspan=2)

# Boutons d'execution d'analyse

#création des widgets d'action
labelaction0=Label(top,text='',justify='left', anchor='nw')
boutonaction0=Button(top, text='Calculs globaux', command=partial(calculglobal,labelaction0))
labelaction1=Label(top,text='',justify='left', anchor='nw')
boutonaction1=Button(top, text='Nb d\'occurences et fréquences des caractères', command=partial(traitementtextuel,labelaction1,0))
labelaction2=Label(top,text='',justify='left', anchor='nw')
boutonaction2=Button(top, text='Nb d\'occurences et fréquences des mots', command=partial(traitementmots,labelaction2))

boutonaction0.grid(row=3, column=0)  
boutonaction1.grid(row=3, column=1)
boutonaction2.grid(row=3, column=2)
labelaction0.grid(row=4,column=0,sticky="nw")
labelaction1.grid(row=4,column=1,sticky="nw")
labelaction2.grid(row=4,column=2,sticky="nw")


top.mainloop()
