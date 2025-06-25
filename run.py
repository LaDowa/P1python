from app import create_app
app = create_app() #Crée l'application flask 
if __name__=='__main__':
    app.run(debug=True) #Démarre le serveur en mode débug


#Pour tester notre application web, il faut se rendre sur : http://localhost:5000/ 