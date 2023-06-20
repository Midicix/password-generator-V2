from tkinter import *
import tkinter.messagebox
import tkinter as tk
from random import randint
import os

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


confirmation_copie = canvas.create_text(250, 200, text="Que voulez-vous que \n  votre mot de passe\n       contiennent ?",
                fill=couleur_titre,
                font=police_lettre)

btn_lettre_min = Button(fenetre, height=1, width=10, text="lettre_min", command= lambda : choix(1))
btn_lettre_min.pack()
btn_lettre_maj = Button(fenetre, height=1, width=10, text="lettre_maj", command= lambda : choix(2))
btn_lettre_maj.pack()
btn_chiffre = Button(fenetre, height=1, width=10, text="chiffre", command=lambda: choix(3))
btn_chiffre.pack()
btn_caractere = Button(fenetre, height=1, width=10, text="caractere", command=lambda: choix(4))
btn_caractere.pack()


saisie_btn_lettre_min = canvas.create_window(250, 275, window=btn_lettre_min)
saisie_btn_lettre_maj = canvas.create_window(250, 310, window=btn_lettre_maj)
saisie_btn_chiffre = canvas.create_window(250, 345, window=btn_chiffre)
saisie_btn_caractere = canvas.create_window(250, 380, window=btn_caractere)

def choix(var):
    var = str(var)
    fenetre.destroy()
    os.system('python password_generator-'+var+'.py')

fenetre.mainloop()