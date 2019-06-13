#import analysetexte
import os
import tkinter
from tkinter import *
from functools import partial

global chaine
global existe
global nb_lignes
global saisie_nom_fichier
global contenu_fichier
global liste_mots
global texte_fichier

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
    
    #Ouverture du fichier
    fichier = open(nom_fichier, "r")
    #Lecture du fichier avec remplacement de passage à la ligne par des espace
    contenu_fichier = fichier.read()
    #Comptage du nombre de retour à la ligne
    if contenu_fichier[len(contenu_fichier)-1]=="\n":
        nb_lignes = contenu_fichier.count("\n")
    else:
        nb_lignes = contenu_fichier.count("\n")+1
    # Fermeture du fichier
    fichier.close()

    contenu_fichier.replace("\n"," ")
    while contenu_fichier[len(contenu_fichier)-1] == " ":
        contenu_fichier = contenu_fichier[:len(contenu_fichier)-1]

    # Génération de la liste des mots
    listemots = formatage_mots(contenu_fichier)
    
    return contenu_fichier, nb_lignes

def is_fichier ():
    global nb_lignes
    global saisie_nom_fichier
    global contenu_fichier
    global texte_fichier
    
    nom_fichier = saisie_nom_fichier.get()
    labelaction0.config(text="")
    labelaction1.config(text="")
    labelaction2.config(text="")
    
    # Si le fichier est trouvé
    if os.path.isfile(nom_fichier) :
        # Lecture du contenu du fichier
        contenu_fichier, nb_lignes = lecture_fichier(nom_fichier)
        # Affichage du contenu du fichier
        texte_fichier=contenu_fichier
        contenu_fichier1.config(text=texte_fichier)
        contenu_fichier1.config(fg="black")
    else:
        # Etiquette fichier absent
        contenu_fichier1.config(text="Fichier inexistant")
        contenu_fichier1.config(fg="red")

def calculglobal (wlabel):

    global contenu_fichier
    global nb_lignes
    global liste_mots
    
    nbcaracteres=len(contenu_fichier)
    nb_mots = len(liste_mots)
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
            resultats=resultats+f"{(longmaxitem-len(tuple1[0]))*'  '}'{tuple1[0]}' Nombre d\'occurences = {tuple1[1][0]-(nb_lignes-1)} et fréquence = {tuple1[1][1]:>.2f} %\n"
        elif tuple1[0]!= "\n":
            resultats=resultats+f"{(longmaxitem-len(tuple1[0]))*'  '}'{tuple1[0]}' Nombre d\'occurences = {tuple1[1][0]} et fréquence = {tuple1[1][1]:>.2f} %\n"
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
top = tkinter.Tk()
top.geometry("1100x900")
top.title("Analyse d'un fichier texte")

# Création des widgets pour saisir le nom du fichier

# Création d'une frame de saisie
frameS = LabelFrame(top, borderwidth=0, height= 800, width = 1000)
frameS.place(x=50, y=20)

# Étiquette
label_fichier = Label(frameS, text="Nom du fichier")
label_fichier.place(x=100, y=20)

# Zone de saisie du nom du fichier
nom_fichier = StringVar(frameS)
saisie_nom_fichier = Entry(frameS, textvariable=nom_fichier)
saisie_nom_fichier.place(x=200, y=20)
saisie_nom_fichier.focus_set()

# Bouton de lecture du fichier
bouton_fichier = Button(frameS, text="Valider", command=is_fichier)
bouton_fichier.place(x=500, y=20)

# Contenu du fichier

#texte_fichier = StringVar()
texte_fichier="Texte inconnu"
contenu_fichier1=Label(frameS, text=texte_fichier, justify="left")
contenu_fichier1.place(x=50, y=50)

# Boutons d'execution d'analyse

#création des widgets d'action
labelaction0=Label(frameS,text='',justify='left', anchor='nw')
boutonaction0=Button(frameS, text='Calculs globaux', command=partial(calculglobal,labelaction0))
labelaction1=Label(frameS,text='',justify='left', anchor='nw')
boutonaction1=Button(frameS, text='Nb d\'occurences et fréquences des caractères', command=partial(traitementtextuel,labelaction1,0))
labelaction2=Label(frameS,text='',justify='left', anchor='nw')
boutonaction2=Button(frameS, text='Nb d\'occurences et fréquences des mots', command=partial(traitementmots,labelaction2))

boutonaction0.place(x=0, y=300)
boutonaction1.place(x=210, y=300)
boutonaction2.place(x=550, y=300)
labelaction0.place(x=0, y=350)
labelaction1.place(x=210, y=350)
labelaction2.place(x=550, y=350)

top.mainloop()
