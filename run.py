from app import create_app
app = create_app() #Crée l'application flask 
if __name__=='__main__':
    app.run(debug=True) #Démarre le serveur en mode débug
