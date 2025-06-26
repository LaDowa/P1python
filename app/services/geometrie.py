import matplotlib.pyplot as plt  #pour dessiner les formes et générer une image
import numpy as np #pour faire des calculs mathématiques
import datetime #pour générer un nom de fichier unique basé sur la date et l'heure
import os  # pour faire des opérations dans les fichiers du pc. On l'utilisera pour trouver des chemins de fichier et créer des dossiers

def generer_motif(cotes, profondeur, taille, angle_rotation, couleur):
    """
    cotes : le nombre de côtés de la forme. 
    profondeur : combien de fois on répète la forme.
    taille : la taille de chaque côté <=> rayon du polynôme inscrit. 
    angle_rotation : l'angle de rotation (en degrés) entre chaque forme répétée.
    Couleur : la couleur du trait.
    """
    fig, ax= plt.subplots() #crée une feuille blanche pour dessiner. 
    ax.set_aspect('equal','box') #assure que les formes ne seront pas déformées.
    ax.axis('off') #cache les axes pour un rendu plus propre.ax. => objet  et set_aspect=> nom de la fonction

    for i in range(0,profondeur): #boucle de dessin
        #profondeur = nombre de répétition du motif et 0 : point de départ 
        angle_debut = np.radians(i*angle_rotation)
        #np.radian => on convertit l'angle de rotation en radian pour utiliser cos et sin. On multiplie par i pour que  chaque forme soit tournée un peu plus que la précédente.
        angles = np.linspace(0, 2 * np.pi, cotes + 1) + angle_debut # +1 pour fermer la forme
        #np.linspace génère un tableau (liste) de nombres (angles) régulièrement espacés autour d'un cercle. But : permettre de placer les sommets.
        #np <=> bibliothèque NumPy.  and np.pi est une constante representant la valeur du nombre pi
        x = taille * np.cos(angles)
        y = taille * np.sin(angles) 
        #x et y sont des tableaux contenant les coorodonées de chaque sommet de la forme
        ax.plot(x, y, color= couleur) #trace les lignes entre les points(x, y). couleur correspond au paramètre de générer_motif

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #chaine de caractères représentant la date et l'heure au moment de l'éxécution du programme. strftime formate ceux-ci tels que:
    # %Y => années (4chiffres entiers) 
    # %m => mois sur 2 chiffres ( 01 à 12)
    # %d => jour du moi ( 01 à 31)
    # %H => heure de la journée (00 à 23)
    # %M : minute (00 à 59)
    # %s : secondes depuis l'époque UNIX
    DOSSIER_IMAGES = "app/static/images/generated" #definit le dossier dans lequelles images générées seront enregistrées.
    #Le dossier est dans static/ ce qui permet à Flask de rendre les images accesssibles via une URL accessibl depuis le navigateur.
    os.makedirs(DOSSIER_IMAGES, exist_ok=True) #créer un soddier dans le chemin est le premier paramètre.Deuxième paramètre sert à éviter les erreurs si le fichier existe déjà.

    nom_fichier = f"motif_{timestamp}.png" #f-string indique une chaîne formatée 
    #crée un nom unique de fichier basé sur date et heure
    chemin_complet = os.path.join(DOSSIER_IMAGES, nom_fichier) #construit le chemin complet du fichier à enregister dans le dossier spécifié
    plt.savefig(chemin_complet) #sauvegarde l'image dans le chemin complet

    plt.close () #ferme la figure  Matplotlib pour libérer la mémoire et éviter l'accumulation de figures

    return "static/images/generated/" + nom_fichier
    #permet de récupérer le nom du fichier pour l'utiliser ( par Flask).
