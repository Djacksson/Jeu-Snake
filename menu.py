from tkinter import *
import os
import pygame

#----------------------------------------------------------------------------------------------------
# Fonction pour quitter le launcher
def quitter():
    Fenetre.destroy()

#----------------------------------------------------------------------------------------------------
# Fonction ajouter une valeur à une variable quand on clique sur le bouton radio
def jouer():
    global var_jouer
    var_jouer += 1

#----------------------------------------------------------------------------------------------------
# Bouton pour lancer le jeu
def start():

    # Le jeu correspondant à un seul joueur suivant les niveaux
    if var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==1:   #niveau 1
        os.popen("1_Player\A1_Snake_70.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==2: #niveau 2
        os.popen("1_Player\A1_Snake_50.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==3: #niveau 3
        os.popen("1_Player\A1_Snake_40.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==4: #niveau 4
        os.popen("1_Player\A1_Snake_30.py")
    #----------------------------------------------------------------------------------------------------
    # Le jeu correspondant à deux joueurs suivant les niveaux
        
    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==1: #niveau 1
        os.popen("2_Players\A2_Snake_70.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==2: #niveau 2
        os.popen("2_Players\A2_Snake_50.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==3: #niveau 3
        os.popen("2_Players\A2_Snake_40.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==4: #niveau 4
        os.popen("2_Players\A2_Snake_30.py")
    #----------------------------------------------------------------------------------------------------
    # Cas où le nombre de joueurs n'est pas definie

    elif var_jouer==0:
        filewin4=Toplevel(Fenetre)
        x_pos= (width_wind/2) - (600/2)
        y_pos= (height_wind/2) + (30/2)
        filewin4.geometry('600x30+%d+%d' % ( x_pos, y_pos))
        filewin4.title('Attention !')
        filewin4.resizable(width=False,height=False)
        
        Label7=Label(filewin4,text="Veuillez sélectionner le nombre de joueur.")
        Label7.config(font=('courrier',15,'bold'),fg='red',bg='#73aadc')
        Label7.pack(fill=BOTH,expand=1)
    #----------------------------------------------------------------------------------------------------
    #Cas où le mode de jeu n'est pas definie
    
    elif var_jouer==1:
        filewin4=Toplevel(Fenetre)
        x_pos= (width_wind/2) - (600/2)
        y_pos= (height_wind/2) + (30/2)
        filewin4.geometry('600x30+%d+%d' % ( x_pos, y_pos))
        filewin4.title('Attention !')
        filewin4.resizable(width=False,height=False)
        
        Label7=Label(filewin4,text="Veuillez sélectionner un mode de jeu.")
        Label7.config(font=('courrier',15,'bold'),fg='red',bg='#73aadc')
        Label7.pack(fill=BOTH,expand=1)
#----------------------------------------------------------------------------------------------------
# Bouton d'indication
def click():
    filewin5=Toplevel(Fenetre)
    x_pos= (width_wind/2) - (600/2)
    y_pos= (height_wind/2) + (50/2)
    filewin5.geometry('600x50+%d+%d' % ( x_pos, y_pos))
    filewin5.title('Attention !')
    filewin5.resizable(width=False,height=False)
        
    Label8=Label(filewin5,text="Cocher le nombres de joueurs et la vitesse du jeu!\nAppuyer sur Commencer pour jouer !")
    Label8.config(font=('courrier',15,'bold'),fg='red',bg='#73aadc')
    Label8.pack(fill=BOTH,expand=1)
#---------------------------------------------------------------------------------------------------
#Fonction pour le menu ( Work in progress )
def Docs():
    
   filewin = Toplevel(Fenetre)
   filewin.config(bg='#73aadc')
   x_pos= (width_wind/2) - (600/2)
   y_pos= (height_wind/2) - (300/2)
   filewin.geometry('600x300+%d+%d' % ( x_pos, y_pos))
   filewin.resizable(width=True,height=True)
   
   Label4=Label(filewin,text="-Pour lancer une partie veuillez sélectionner le nombres de joueurs et la vitesse de votre serpent.\n" +
                "-Une fois cette démarche réalisé appuyé sur le bouton Jouer.\n")
   Label4.config(font=('courrier',10,'italic','bold'),bg='#73aadc')
   Label4.pack(fill=BOTH)
#----------------------------------------------------------------------------------------------------
#Informations sur le(s) programmeur(s)
def En_Savoir_Plus():
   filewin2 = Toplevel(Fenetre)
   filewin2.config(bg='#73aadc')
   x_pos= (width_wind/2) - (600/2)
   y_pos= (height_wind/2) - (300/2)
   filewin2.geometry('600x300+%d+%d' % ( x_pos, y_pos))
   filewin2.resizable(width=True,height=True)
   
   Label5=Label(filewin2,text="Projet ISN 2015\n\n Lycée du Forez\n\n" +
                " Contact : extrat.h@gmail.com")
   Label5.config(font=('courrier',10,'italic','bold'),bg='#73aadc')
   Label5.pack(fill=BOTH)
#----------------------------------------------------------------------------------------------------
#Document de tutoriel du jeu
def tuto():
    filewin3 = Toplevel(Fenetre)
    filewin3.config(bg='#73aadc')
    x_pos= (width_wind/2) - (600/2)
    y_pos= (height_wind/2) - (300/2)
    filewin3.geometry('600x300+%d+%d' % ( x_pos, y_pos))
    filewin3.resizable(width=True,height=True)
    
    Label6=Label(filewin3,text="Snake 1 Joueur :\n\n -Pour le déplacement du serpent vous pouvez utiliser les touches ZQSD ou les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n\n" +
                 "Snake 2 Joueurs :\n\n -Le premier joueur va jouer avec les touches ZQSD et l'autre joueur avec les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n" +
                 "-Pour lancer une nouvelle partie vous avez la touche N ou le bouton Nouvelle Partie.\n" +
                 "-Si l'un des joueurs fait mourir son serpent il perd la partie.\n\n" +
                 " Nous vous souhaitons bonne chance et bon jeu")
    Label6.config(font=('courrier',10,'italic','bold'),bg='#73aadc')
    Label6.pack(fill=BOTH)

#----------------------------------------------------------------------------------------------------
# Fenetre tkinter avec des variables

Fenetre=Tk()
Fenetre.title('Snake')
Fenetre.config(bg='#73aadc')
Fenetre.resizable(width=False,height=False)
#----------------------------------------------------------------------------------------------------
#Dimmension et position de l'interface du menu 
width_inter = 700
height_inter = 500
width_wind = Fenetre.winfo_screenwidth()
height_wind = Fenetre.winfo_screenheight()
x_inter = (width_wind/2) - (width_inter/2)
y_inter = (height_wind/2) - (height_inter/2)
Fenetre.geometry("%dx%d+%d+%d" % (width_inter, height_inter, x_inter, y_inter))

menubar = Menu(Fenetre)
#----------------------------------------------------------------------------------------------------
#Création d'un menu
fichier_menu = Menu(menubar)    #pour créer la barre où s'affiche "Fichier"
menubar.add_cascade(label="Fichier", menu=fichier_menu)
fichier_menu.add_command(label="Comment jouer ?", command=tuto)
fichier_menu.add_command(label="Quitter", command=quitter)

aide_menu = Menu(menubar)   #pour créer la barre où s'affiche "Aide"
menubar.add_cascade(label="Aide", menu=aide_menu)
aide_menu.add_command(label="Docs", command=Docs)
aide_menu.add_command(label="En savoir plus", command=En_Savoir_Plus)

Fenetre.config(menu=menubar)

#---------------------------------------------------------------------------------------------------
#Variables
var_jouer = 0
var_joueur = IntVar()
var_vitesse = IntVar()
#------------------------------------------------------------------------------------------------------
# Titre du jeu
titre=Label(Fenetre, text='SNAKE')
titre.config(font=('courrier',70,'bold'),bg='#73aadc',fg='#fcbf7c')
titre.pack()
#----------------------------------------------------------------------------------------------------
# Bouton pour lancer le jeu
bouton_jouer=Button(Fenetre, text='Commencer', command=start, bd=2,relief='raised')
bouton_jouer.config(font=('courrier',20,'bold'),bg='#fcbf7c',fg='#646464',width=20)
bouton_jouer.pack(side=TOP,expand=0)
#------------------------------------------------------------------------------------------------------
# Bouton pour quitter le launcher
bouton_quitter=Button(Fenetre,text='Quitter',command=quitter,bd=2,relief='raised')
bouton_quitter.config(font=('courrier',20,'bold'),bg='#fcbf7c',fg='#646464',width=20)
bouton_quitter.pack(side=BOTTOM,expand=1)
#----------------------------------------------------------------------------------------------------
# Affichage du nombre de joueurs
Nombre_joueur=Button(Fenetre,text='Nombre de joueurs', command=click, bd=2,relief='raised')
Nombre_joueur.config(font=('courrier',20,'bold'),bg='#fcbf7c',fg='#646464',width=20)
Nombre_joueur.pack(expand=1)
#----------------------------------------------------------------------------------------------------
# Bouton radios permettant le choix du nombre de joueurs
bouton_joueur_un=Radiobutton(Fenetre, text='Un Joueur', value=1, variable=var_joueur, command=jouer,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_joueur_un.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_joueur_un.pack(expand=0)

bouton_joueur_deux=Radiobutton(Fenetre,text='Deux Joueurs', value=2, variable=var_joueur, command=jouer,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_joueur_deux.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_joueur_deux.pack(expand=0)
#----------------------------------------------------------------------------------------------------
# Affichage de la vitesse en Ms
vitesse=Button(Fenetre,text='Vitesse', command=click, bd=2, relief='raised')
vitesse.config(font=('courrier',20,'bold'),bg='#fcbf7c',fg='#646464',width=20)
vitesse.pack(expand=1)
#----------------------------------------------------------------------------------------------------
# Bouton radios permettant le choix de la vitesse
bouton_vitesseun=Radiobutton(Fenetre,text='Lente', value=1, variable=var_vitesse,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_vitesseun.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_vitesseun.pack(side=LEFT,expand=0)

bouton_vitessedeux=Radiobutton(Fenetre,text='Normale', value=2, variable=var_vitesse,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_vitessedeux.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_vitessedeux.pack(side=LEFT,expand=0)

bouton_vitessetrois=Radiobutton(Fenetre,text='Rapide', value=3, variable=var_vitesse,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_vitessetrois.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_vitessetrois.pack(side=LEFT,expand=0)

bouton_vitessequatre=Radiobutton(Fenetre,text='Hardcore', value=4, variable=var_vitesse,bd=2,relief='sunken',selectcolor='#fcbf7c')
bouton_vitessequatre.config(font=('courrier',15,'italic','bold'),bg='#fcbf7c',fg='#646464',width=12)
bouton_vitessequatre.pack(side=LEFT,expand=0)
#----------------------------------------------------------------------------------------------------

Fenetre.mainloop()
