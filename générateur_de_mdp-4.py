from tkinter import *
import tkinter.messagebox
import tkinter as tk
from random import randint

# Création de la fenêtre

##########################################
#color :
couleur_fond = "#555555" #On peut mettre les couleurs en hexadécimal, par exemple, ici, mettre "gray" ou "#5FB691"
couleur_titre = "black"
police_lettre = "Arial 12 bold"

#dimension
hauteur_page = 500
largeur_page = 500

##########################################

fenetre = Tk()
canvas = Canvas(fenetre, width=hauteur_page, height=largeur_page, bg = couleur_fond, highlightthickness=0)
canvas.pack(padx=0, pady=0)
fenetre.geometry('500x500')
fenetre.config(bg=couleur_fond)
fenetre.title("Générateur de mot de passe sécurisé")


confirmation_copie = canvas.create_text(380, 280, text="",
                fill=couleur_titre,
                font=police_lettre)

confirmation_max = canvas.create_text(100, 75, text="",
                fill=couleur_titre,
                font=police_lettre)

btn_generer = Button(fenetre, height=1, width=10, text="Créer", command=lambda: generer())
btn_generer.pack()
btn_copier = Button(fenetre, height=1, width=10, text="Copier", command=lambda: copier())
btn_copier.pack()
btn_val_max1 = Button(fenetre, height=1, width=10, text="Confirmer", command=lambda: change_max_value(saisie_max.get()))
btn_val_max1.pack()

saisie = tkinter.Entry()
saisie.config(state = tkinter.NORMAL)

saisie_max = tkinter.Entry()
saisie_max.config(state = tkinter.NORMAL)

saisie_fenetre = canvas.create_window(250, 250, window=saisie)
btn_fenetre = canvas.create_window(250, 280, window=btn_generer)
btn_fenetre = canvas.create_window(380, 250, window=btn_copier)

saisie_fenetre = canvas.create_window(75, 25, window=saisie_max)
btn_fenetre = canvas.create_window(200, 25, window=btn_val_max1)

liste_lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
liste_chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
liste_caractere = ['!', '?', '.', ",", ";", "'", '"', "/", ":", "&"]

max_cara = 8

def change_max_value(val):
    global max_cara, liste_chiffre
    compteur = 0
    for c in val:
        if c == "." or c == "-":
            compteur += 1
        if c not in liste_chiffre :
            compteur += 1
    if len(val) == 0 or compteur >= 1:
        canvas.itemconfig(confirmation_max, text="Le paramètre n'est\n pas compatible !")
    elif compteur == 0:
        val = int(val)
    change_max_value2(val)

def change_max_value2(val):
    global max_cara
    if str(val) == '0'or val == "":
        canvas.itemconfig(confirmation_max, text="Le paramètre n'est\n pas compatible !")
    else :
        if type(val) == float:
            canvas.itemconfig(confirmation_max, text="Le paramètre n'est\n pas compatible !")
        elif type(val) == int:
            max_cara = val
            canvas.itemconfig(confirmation_max, text="Le paramètre a bien\n été pris en compte !")

def copier():
    fenetre.clipboard_clear()
    fenetre.clipboard_append(saisie.get())
    canvas.itemconfig(confirmation_copie, text="copié !")

def generer():
    global saisie, max_cara
    canvas.itemconfig(confirmation_copie, text="")
    canvas.itemconfig(confirmation_max, text="")
    saisie.delete(0,len(saisie.get()))
    var_lettre = 0
    var_chiffre = 0
    text = ""
    compteur_while = 0
    while compteur_while <= (max_cara-1) :
        compteur = randint(1,4)
        compteur_while += 1
        if compteur == 1 :
            var_lettre_maj = randint(0,len(liste_lettre_maj)-1)
            text += liste_lettre_maj[var_lettre_maj]
        if compteur == 2 :
            var_lettre_min = randint(0,len(liste_lettre_min)-1)
            text += liste_lettre_min[var_lettre_min]
        if compteur == 3 :
            var_chiffre = randint(0,len(liste_chiffre)-1)
            text += liste_chiffre[var_chiffre]
        if compteur == 4 :
            var_caractere = randint(0,len(liste_caractere)-1)
            text += liste_caractere[var_caractere]
    saisie.insert(0, text)

fenetre.mainloop()