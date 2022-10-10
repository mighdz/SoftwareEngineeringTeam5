from flask import Flask, render_template, request, jsonify, json
from herokudb import Heroku

app = Flask(__name__)

#Declare class from herokudb.py
herokudb = Heroku()

@app.route("/")
def entryScreen():
    return render_template("SplashScreen.html")

@app.route("/entry_screen")
def home():
    return render_template("EntryScreen.html")

@app.route("/link", methods = ['POST'])
def enterPlayers():
    
    playerInformation = []

    if request.method == 'POST':

        playerData = request.get_json(force = True)
        for i in playerData.keys():
            for j in playerData.values():
                playerInformation.append(i)
                playerInformation.append(j)
        
        id = playerData["red1ID"]
        firstName = playerData["red1fname"]
        lastName = playerData["red1lname"]
        codename = playerData["red1code"]

        herokudb.playerAdd(id,firstName,lastName,codename)

        id = playerData["green1ID"]
        firstName = playerData["green1fname"]
        lastName = playerData["green1lname"]
        codename = playerData["green1code"]

        herokudb.playerAdd(id,firstName,lastName,codename)

    return jsonify(playerData)

if __name__ == '__main__':
    app.run(debug=True)