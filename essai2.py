# coding: utf-8

import os
from tkinter import *
from functools import partial



def lecture_fichier(nom_fichier) :
    fichier = open(nom_fichier, "r")
    contenu_fichier = fichier.read()
    fichier.close()
    
    while contenu_fichier[len(contenu_fichier)-1] == (" " or "\n"):
        contenu_fichier = contenu_fichier[:len(contenu_fichier)-1]
    # Remplacement de fins de ligne par des espaces
    contenu_fichier = contenu_fichier.replace("\n"," ")
    # Fermeture du fichier

    

    # Génération de la liste des mots
    #listemots = formatage_mots(contenu_fichier)
    return contenu_fichier 
    

def is_fichier ():
    nom_fichier = saisie_nom_fichier.get()
    if os.path.isfile(nom_fichier) :
        contenu_initial = lecture_fichier(nom_fichier)
        contenu = Label(top, text=contenu_initial, justify="left")
    else:
        # Etiquette fichier absent
        contenu = Label(top, padx=10, pady=5, text="Fichier inexistant")
    contenu.grid(column=0, row=1, columnspan=2)
    
    
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
    
    