#######################
###### Python 3. ######
######## Snake ########
##### Hugo EXTRAT #####
#######################


from tkinter import*
from tkinter.colorchooser import *
from random import randrange
import os
import time
import pygame

'########################################################################'
'#----------------------------------------------------------------------#'
'#                                Fonctions                             #'
'#----------------------------------------------------------------------#'
'########################################################################'

#######################################################################
# Fonction pour l'écran de fin ----------------------------------------
#######################################################################
def fin():
    can.delete(ALL) ## On supprime tous les objets du Canvas (can)
    end=can.create_text(350,160,font=('Fixedsys',20),text="Vous êtes mort !!! \n\nVotre score est de : " +str(manger), fill="RED")  ## On crée un Texte avec le Score final

#######################################################################
# Les couleurs de la tete et du corp sont aléatoires ------------------
#######################################################################
def changecolor():
    global color_tete, color_corp
    couleur_tete = ['purple','cyan','maroon','green','red','blue','orange', 'yellow'] ## Couleur de la tête aléatoire
    color_t = randrange(8)
    color_tete = couleur_tete[color_t]
    
    couleur_corp = ['#a953ff','#0000ff','#ff8000','#8080ff','#ff8040','#00ffff','#ffff00','#ff0000','#ff80ff','#0080ff','#80ffff','#ff8080','#ffff80']
 ## Couleur du corp aléatoire
    color_c = randrange(9)
    color_corp = couleur_corp[color_c]

def tp():
    global coord_portail, coord_portail3,x_tp,y_tp,x_tp1,y_tp1
    x_tp=randrange(60,340,10)
    y_tp=randrange(60,300,10)
    portail=can.create_rectangle(x_tp,y_tp,x_tp+10,y_tp+10)
    portail1=can.create_rectangle(x_tp-5,y_tp-5,x_tp+15,y_tp+15)  
    coord_portail=(x_tp,y_tp)
    
    x_tp1=randrange(350,630,10)
    y_tp1=randrange(60,300,10)
    portail3=can.create_rectangle(x_tp1,y_tp1,x_tp1+10,y_tp1+10)
    portail4=can.create_rectangle(x_tp1-5,y_tp1-5,x_tp1+15,y_tp1+15)
    coord_portail3=(x_tp1,y_tp1)
#######################################################################
# La musique en jeu ( Utilisation de PyGame ) -------------------------
#######################################################################    
def music():
    pygame.mixer.init()
    son = pygame.mixer.Sound('music.ogg') ## On récupère la musique dans le dossier principal
    son.play(loops=-1, maxtime=0, fade_ms=0) ## Quand la musique se termine on la relance avec loops=-1
    
#######################################################################
# Fonction pour l'apparition aléatoire des pommes ---------------------
#######################################################################
def pose_pomme():
    global coord_pomme,x_pomme,y_pomme,pomme
    x_pomme=randrange(10,690,10) ## Coordonnées aléatoires X et Y des pommes
    y_pomme=randrange(10,440,10)
    pomme=can.create_oval(x_pomme,y_pomme,x_pomme+10,y_pomme+10,fill="Orange") ## Création d'une pomme dans le Canvas au coordonnées ci-dessus
    coord_pomme=(x_pomme,y_pomme) ## Coordonnées de la pomme

#######################################################################
# Fonction principale du jeu ------------------------------------------
#######################################################################
def move():
    global snake,direction,tete_x,tete_y,tete_x2,tete_y2,pomme,coord_pomme, color_corp, color_tete # 2 Lignes de Global
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n,manger, temps, temps1,delai, acceleration, acceleration1, Score, jouer, play, coord_tp1, x_tp1, y_tp1, x_tp2, y_tp2, coord_tp2          

    if temps == 2:
        jouer=can.create_text(350,200,font=('Fixedsys',20),text="Espace pour commencer !", fill="RED")

#######################################################################
# Boucles permettant le déplacement du serpent
    # Mouvement à gauche
    if direction==2:
        x=-10 ## Correspond à la valeur du déplacement en X
        y=0 ## De même mais en Y

    # Mouvement à droite
    elif direction==1:
        x=10
        y=0

    # Mouvement en bas      
    elif direction==0:
        y=-10
        x=0
        
    # Mouvement en haut     
    elif direction==3:
        y=10
        x=0

    #######################################################################
    long=len(snake)     #Longeur du Serpent
    long=long-1     # Dans une liste on part de 0 et la longueur donne le nombre d'éléments; Il faut donc enlever 1
    
    #######################################################################
    # Boucles permettant au serpent de grandir
    while long !=0: 
        ## On déplace d'abord les coordonnées des éléments, le corp du Serpent doit suivre la tête
        ## Le corp qui suit la tête ne doit jamais la dépasser, ainsi tous les carré vont se suivre
        pos_x[long]=pos_x[long-1] 
        pos_y[long]=pos_y[long-1]
        long+=-1
    
    pos_x[0]+=x
    pos_y[0]+=y
    
    while long!=len(snake):
        can.coords(snake[long],pos_x[long],pos_y[long],pos_x[long]+10,pos_y[long]+10) ## Ce qui était valable pour les positions le devient pour le déplacement.
        long+=1
    long=1


    coord_tete=pos_x[long],pos_y[long] ## Coordonnées de la tête

    ## Si on touche un mur on affiche la fonction fin()
    if pos_y[long] > 440 or pos_y[long] < 10:
        temps = 1
        fin()
        pseudo1()
    if pos_x[long] > 680 or pos_x[long] < 10:
        temps = 1
        fin()
        pseudo1()

   
    #######################################################################
    # Boucle pour la rencontre entre la tete et la pomme
    
    if coord_tete==coord_pomme: ## Si les coordonnées de la tête et de la pomme sont les mêmes on fait la boucle
        can.delete(pomme) ## On supprime la pomme
        pose_pomme() ## On crée une pomme à un endroit aléatoire

        ## La pomme ne doit pas être sur le Serpent
        if pos_x[0]==x_pomme and pos_y[0]==y_pomme:
            can.delete(pomme)
            pose_pomme()
        if pos_x[long]==x_pomme and pos_y[long]==y_pomme:
            can.delete(pomme)
            pose_pomme()
            
        manger+=10 ## Chaque pomme mangé le score augmente de 10
        Score.config(text="Score : "+str(manger)) ## On affiche le score

        ## Options du jeu
        if manger >= 100:
            can.configure(bg="white") ## Si manger >=100 le fond devient Blanc
        if manger >= 200:
            can.configure(bg="grey") ## Si manger >=100 le fond devient Gris
        if manger == 100:   #Augmenter l'accéleration quand le point atteint 100
            delai -= 5   ## Quand manger == 100 la vitesse du Serpent augmente
            acceleration=can.create_text(350,450,font=('Fixedsys',16),text="Attention ! Petite accélération du serpent.", fill="RED") ## Texte pour anoncer l'accélération du Serpent
        if manger == 200:   #Augmenter l'accéleration quand le point atteint 200
            delai -= 5   ## Quand manger == 200 la vitesse du Serpent augmente
            acceleration1=can.create_text(350,450,font=('Fixedsys',16),text="Vous êtes très fort, la difficulté augmente.", fill="RED")## Texte pour anoncer l'accélération du Serpent
        if manger > 100:
            can.delete(acceleration)
        if manger > 200:
            can.delete(acceleration1)
        if manger==200:
            tp()
            
        #Agrandissement du snake
        corps=can.create_rectangle(1000,1000,1010,1010,fill=color_corp)## On crée le carré en dehors du Canvas pour ne pas l'afficher à l'écran
        snake.append(corps)## On accroche ensuite le nouveau carré
        ## Et hop le serpent se crée au fil du jeu
        pos_x.append (pos_x[n]+10+x)
        pos_y.append (pos_y[n]+10+y)     

        n=n+1
        
    if manger>=200:
        if coord_tete==coord_portail:
            pos_x[0]=x_tp1+10
            pos_y[0]=y_tp1+10
        if coord_tete==coord_portail3:
            pos_x[0]=x_tp+10
            pos_y[0]=y_tp+10

    if temps == 0:    
        can.after(delai,move) ## On relance la fonction avec un temps défini
        
    while long!=len(snake):
        if pos_x[long]==pos_x[0] and pos_y[long]==pos_y[0]: ## Si le serpent se rentre dedans, l'écran de fin s'affiche
            temps = 1
            fin()
            pseudo1()
        long+=1
    
#######################################################################
# Fonctions définissant le mouvement avec les touches -----------------
#######################################################################
def up(event):
    global direction
    if direction !=3:
        direction = 0
        
def right(event):
    global direction
    if direction !=2:
        direction = 1

def left(event):
    global direction
    if direction !=1:
        direction = 2

def down(event):
    global direction
    if direction !=0:
        direction = 3

#######################################################################
# Fonctions pour lancer une nouvelle partie ---------------------------
#######################################################################


def new_game():
    global snake,direction,tete_x,tete_y,tete_x2,tete_y2,pomme,coord_pomme, coord_tete, color_tete, color_corp
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n, temps, temps1, manger, Score, top

    score=0
    can.delete(ALL)
    
    if temps == 1:
        top.destroy()
    
    can.configure(bg="#a5a5a5")

    changecolor()
    
    snake=[]
    
    tete=can.create_rectangle(100,100,110,110,fill=color_tete)
    corps=can.create_rectangle(90,100,100,110,fill=color_corp)
    
    snake.append(tete)
    snake.append(corps)

    pos_x=[]
    pos_y=[]

    #Position du serpent d'une nouvelle partie
    pos_x.append (can.coords(tete)[0])
    pos_y.append (can.coords(tete)[1])
    pos_x.append (can.coords(corps)[2])
    pos_y.append (can.coords(corps)[3])
    
    ## Ici les bordures avec leurs coordonnées
    can.create_rectangle(0,0,10,500,fill="#73aadc")
    can.create_rectangle(10,0,700,10,fill="#73aadc")
    can.create_rectangle(690,0,700,500,fill="#73aadc")
    can.create_rectangle(0,500,700,460,fill="#73aadc")
    #Redefinition des variables du serpent
    long==0
    n=1
    manger = 0
    temps = 2
    temps1 = 1
    temps2=0
    direction = 1
    delai=70

    Score.config(text="Score : " +str(manger))
    
    pose_pomme()

    if manger!=0:
        manger=0



#######################################################################
# Fonctions pour la Pause et la Fermeture -----------------------------
#######################################################################
def pause(event):
    global temps, pause, temps1, temps2
    temps = 1 ## Variable temps permettant de savoir quand le jeu est en cours ou quand celui-ci est en pause
    temps1 = 1
    if temps == 1:
        if temps2 == 1: ## Temps2 nous permet d'afficher qu'une fois le texte PAUSE
            pause=can.create_text(350,200,font=('Fixedsys',18),text="PAUSE", fill="RED") ## Voici l'affichage du texte PAUSE
            temps2 = 0

def play(event):
    global temps, pause, temps1, jouer, temps2
    temps=0
    if temps1 == 1: ## Nous permet de relancer le jeu en appuyant sur Espace si celui-ci était en pause
        if temps == 0:
            can.delete(pause)
            can.delete(jouer)
            temps1 = 0
            temps2 = 1
            move()

def auto():
    global temps, pause, temps1, jouer, temps2
    temps=0
    #Play
    if temps1 == 1:
        if temps == 0:
            can.delete(pause)
            can.delete(jouer)
            temps1 = 0
            temps2 = 1
            move()

def quitter():
    Fenetre.destroy() ## Pour fermer le jeu

#######################################################################
# Fonctions pour enregistrer le score ---------------------------------
#######################################################################
def score_text():
    global temps, temps1, pause
    os.popen("scores_70.txt")
    temps1 = 1
    temps = 1
    
def score():
    global pseudo, temps, pause, temps1, manger, top
    score = open("scores_70.txt", "a")
    score.write("\nLe score de " + pseudo.get() +
                " est de " + str(manger))
    temps1 = 1
    temps = 1
    top.destroy()
    
def pseudo1():
    global pseudo, top
    top = Toplevel(Fenetre)
    top.resizable(width=False,height=False)
    #Dimension et position de l'interface de jeu
    x_pos= (width_wind/2) - (300/2)
    y_pos= (height_wind/2) - (50/2)
    top.geometry('300x50+%d+%d' % ( x_pos, y_pos))
    top.config(bg="#73aadc")

    #Texte de fond de l'interface d'enregistrement de score
    Label_pseudo = Label(top, font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464',bd=2,relief='raised', text='Votre Pseudo')
    Label_pseudo.pack()
    
    #Cadre d'enregistrement de score
    pseudo=StringVar()
    pseudo.set('')
    pseudo = Entry(top,font=('Fixedsys',10,'bold'), textvariable = pseudo)
    pseudo.insert(0, "Joueur")
    pseudo.focus_set()
    pseudo.pack(side = LEFT)

    
    #Boutton d'enregistrement du score
    Bouton_pseudo = Button(top,font=('Fixedsys',15,'bold'),bg='#fcbf7c',fg='#646464', text='Valider', command=score)
    Bouton_pseudo.pack(side = RIGHT)

#######################################################################
# Fonctions pour le Menu ----------------------------------------------
#######################################################################
def Docs():
    global temps, temps1, pause
    filewin = Toplevel(Fenetre) ## Nous permet d'afficher une nouvelle fenetre au dessus de la première
    filewin.config(bg="#73aadc")
    x_pos= (width_wind/2) - (600/2)
    y_pos= (height_wind/2) - (300/2)
    filewin.geometry('600x300+%d+%d' % ( x_pos, y_pos))
    filewin.resizable(width=True,height=True)
    
    Label4=Label(filewin,text="Snake 1 Joueur :\n\n -Pour le déplacement du serpent vous pouvez utiliser les touches ZQSD ou les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n" +
                 "-Pour lancer une nouvelle partie vous avez la touche N ou le bouton Nouvelle Partie.\n\n" +
                 " Nous vous souhaitons bonne chance et bon jeu") ## Texte dans la fenetre
    Label4.config(font=('courrier',10,'italic','bold'),bg="#73aadc")
    Label4.pack(fill=BOTH)
    
    temps1 = 1## On met en pause le jeu quand on ouvre une fenetre
    temps = 1

def En_Savoir_Plus():
    global temps, temps1, pause
    filewin2 = Toplevel(Fenetre) ## Nous permet d'afficher une nouvelle fenetre au dessus de la première
    filewin2.config(bg="#73aadc")
    x_pos= (width_wind/2) - (600/2)
    y_pos= (height_wind/2) - (300/2)
    filewin2.geometry('600x300+%d+%d' % ( x_pos, y_pos))
    filewin2.resizable(width=True,height=True)

    Label5=Label(filewin2,text="Jeu réalisé par Aloïs et Hugo pour notre projet en ISN 2015.\n\n Lycée du Forez\n\n" +
                " Contact : jununelol@gmail.com") ## Texte dans la fenetre
    Label5.config(font=('courrier',10,'italic','bold'),bg="#73aadc")
    Label5.pack(fill=BOTH)
    
    temps1 = 1 ## On met en pause le jeu quand on ouvre une fenetre
    temps = 1

#######################################################################
# Création de la Fenetre avec le Canvas -------------------------------
#######################################################################
Fenetre = Tk()
menubar = Menu(Fenetre)
Fenetre.title("Best Snake") ## Titre de la fenetre
Fenetre.resizable(width=False,height=False) ## On ne peut pas agrandir la fenetre manuellement
#Dimension et position de l'interface de jeu
width_inter = 700
height_inter = 500
width_wind = Fenetre.winfo_screenwidth()
height_wind = Fenetre.winfo_screenheight()
x_inter = (width_wind/2) - (width_inter/2)
y_inter = (height_wind/2) - (height_inter/2)
Fenetre.geometry("%dx%d+%d+%d" % (width_inter, height_inter, x_inter, y_inter))

can=Canvas(Fenetre, width=700, height=500, bg="#a5a5a5",bd=0)    #taille et couleur de font de la fenetre de jeu
can.pack()

## Ici les bordures avec leurs coordonnées
can.create_rectangle(0,0,10,500,fill="#73aadc")
can.create_rectangle(0,0,700,10,fill="#73aadc")
can.create_rectangle(690,0,700,500,fill="#73aadc")
can.create_rectangle(0,500,700,460,fill="#73aadc")
#######################################################################
#Liste des touches sur l'interface
#######################################################################
Bouton_new=Button(Fenetre,font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464', text="Rejouer", command=new_game)
Bouton_new.place(x=10, y=465, width=100, height=30)

Button_play = Button(Fenetre,font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464', text="Play", command=auto)
Button_play.place(x=150, y=465, width=120, height=30)

Bouton_score=Button(Fenetre,font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464', text="Scores", command=score_text)
Bouton_score.place(x=430, y=465, width=120, height=30)

Bouton_quit=Button(Fenetre,font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464', text="Quitter", command=quitter)
Bouton_quit.place(x=590, y=465, width=100, height=30)
#######################################################################
# Définition des variables --------------------------------------------
#######################################################################
long=0
n=1
manger = 0

temps = 2
temps1 = 1
temps2 = 0

delai = 70 ## Delai == vitesse du Serpent

Score = Label(can, font=('Fixedsys',10,'bold'),bg='#fcbf7c',fg='#646464',bd=2,relief='raised', text="Score : " +str(manger),anchor=W)
Score.place(x=290, y=465, width=120, height=30)
#######################################################################
# Création d'un Menu --------------------------------------------------
#######################################################################
fichier_menu = Menu(menubar)
fichier_menu.add_command(label="Nouvelle Partie", command=new_game)
fichier_menu.add_command(label="Quitter", command=quitter)

menubar.add_cascade(label="Fichier", menu=fichier_menu)

aide_menu = Menu(menubar)
aide_menu.add_command(label="Docs", command=Docs)
aide_menu.add_command(label="En savoir plus", command=En_Savoir_Plus)

menubar.add_cascade(label="Aide", menu=aide_menu)

score_menu = Menu(menubar)
score_menu.add_command(label="Scores", command=score_text)

menubar.add_cascade(label="Score", menu=score_menu)

Fenetre.config(menu=menubar)

#######################################################################
# Liste pour le serpent qui va s'agrandir -----------------------------
#######################################################################
snake=[]

#######################################################################
# Direction du serpent au début (Droite) ------------------------------
#######################################################################
direction=1

#######################################################################
# Première pomme pour le jeu ------------------------------------------
#######################################################################
pose_pomme()
changecolor()

#######################################################################
# Création du serpent -------------------------------------------------
#######################################################################
tete=can.create_rectangle(100,100,110,110,fill=color_tete) ## On crée la tête au début avec des coordonnées précis
corps=can.create_rectangle(90,100,100,110,fill=color_corp) ## On crée le corp au début avec des coordonnées précis

snake.append(tete) ## On met les parties du serpent dans la liste Snake
snake.append(corps)

pos_x=[] ## Position de X et de Y
pos_y=[]

pos_x.append (can.coords(tete)[0])
pos_y.append (can.coords(tete)[1])
pos_x.append (can.coords(corps)[2])
pos_y.append (can.coords(corps)[3])

#######################################################################
# Lancement de l'animation --------------------------------------------
#######################################################################
move()
music()

#######################################################################
# Assignation des touches aux fonctions -------------------------------
#######################################################################
Fenetre.bind('<Up>', up)
Fenetre.bind('<Right>', right)
Fenetre.bind('<Left>', left)
Fenetre.bind('<Down>', down)

Fenetre.bind('<KeyPress-z>', up)
Fenetre.bind('<KeyPress-d>', right)
Fenetre.bind('<KeyPress-q>', left)
Fenetre.bind('<KeyPress-s>', down)
Fenetre.bind('<KeyPress-p>', pause)
Fenetre.bind('<space>', play)

Fenetre.bind('<KeyPress-Z>', up)
Fenetre.bind('<KeyPress-D>', right)
Fenetre.bind('<KeyPress-Q>', left)
Fenetre.bind('<KeyPress-S>', down)
Fenetre.bind('<KeyPress-P>', pause)

Fenetre.bind('<KeyPress-n>', lambda event : new_game()) ## Permet de mettre la fonction new_game en mode event quand on appuye sur N
Fenetre.bind('<KeyPress-N>', lambda event : new_game())

Fenetre.mainloop()
