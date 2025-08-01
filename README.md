# P1python
Projet Python ISEN 2025
Générateur de motifs géométriques avec Flask

Ce programme permet à un utilisateur de générer une forme géométrique depuis la page web dont le lien est : http://localhost:5000/

L'utilisateur peut alors choisir les paramètres comme il le souhaite, c'est-à-dire qu'il peut entrer une valeur entière pour la taille initiale de la forme, le nombre de répétitions de cette forme ( aussi appelée profondeur) ainsi que le nombre de côté de celle-ci. Il peut également choisir une couleur parmis la palette proposée ou via la pipette (color picker tool), s'il n'en choisit pas alors la couleur bleue sera automatiquement attribuée au motif. 
Une fois que l'utilisateur a entrer tous les paramètres, il appuie sur le bouton générer (ou sur la touche "entrée" de son clavier) et une nouvelle page web est affichée montrant le motif généré. Il y a également un lien en dessous de la forme permettant de revenir à la page d'acceuil pour pouvoir faire une nouvelle forme. 

## Fonctionnalités
Formulaire web pour saisir les paramètres du motif ( taille initiale, angle de rotation, nombre de répétitions, couleur, nombre de côtés)
Génération d'une image via la librairie Matplotlib
Visualisation du motif généré dans le navigateur
Sauvegarde de l'image dans le dossier images (se trouvant dans le dossier static) 
Lien de passage entre la page d'affichage du motif et la page d'accueil

## Installation
git clone https://github.com/LaDowa/P1python.git
cd P1python

installer les dépendances via requirements.txt avec : pip intsall -r requirements.txt

## Notes
Démarrer le serveur en exécutant le fihcier run.py

## Auteur
PERRY Eva 
LaDowa ( nom d'utilisateur sur github)