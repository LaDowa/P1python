# creation d'un blueprint
from flask import Blueprint, request, render_template
from app.services.geometrie import generer_motif
geogen_bp = Blueprint('geogen',__name__)

@geogen_bp.route('/')
def index(): 
    return render_template('index.html')

@geogen_bp.route('/generer_motif', methods=['POST'])
def generer_motif_route():
    try:
        #Récupérer les données envoyées par le formulaire
        cotes = int(request.form['cotes'])
        profondeur = int(request.form['profondeur'])
        taille = int(request.form['taille'])
        print(">> Taille reçue :", taille)
        angle_rotation = int(request.form['angle_rotation'])
        couleur = request.form['couleur']

        #Appeler la fonction generer_motif avec les paramètres reçus:
        fichier_image = generer_motif(cotes, profondeur, taille, angle_rotation, couleur)

        #Anciennement : Renvoie de l'image dans la balise img. Maintenant : Renvoie un template
        return render_template('generer_motif.html', chemin_image = fichier_image)
    
    except Exception as e: 
        #Gestion des errors; si une erreur se produit, on la stocke dans la variable e et on affiche un message personnalisé
        return f"Une_erreur_est_survenue : {str(e)}"
