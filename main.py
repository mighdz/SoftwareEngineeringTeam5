from flask import Flask, render_template, request, jsonify, json
from herokudb import HerokuConnect

app = Flask(__name__)

#Declare class from herokudb.py
hdb = HerokuConnect()

@app.route("/")
def entryScreen():
    return render_template("SplashScreen.html")

@app.route("/entry_screen")
def home():
    return render_template("EntryScreen.html")

@app.route('/submit', methods = ['POST'])
def enterPlayers():

    playerInformation = []

    if request.method == 'POST':

        playerValues = request.get_json(force=True)
        for i in playerValues.keys():
            for j in playerValues.values():
                playerInformation.append(i)
                playerInformation.append(j)
        
        id = playerValues["red1ID"]
        firstName = playerValues["red1FirstName"]
        lastName = playerValues["red1LastName"]
        codeName = playerValues["red1CodeName"]
        
        hdb.playerAdd(id, firstName, lastName, codeName)

        id = playerValues["green1ID"]
        firstName = playerValues["green1FirstName"]
        lastName = playerValues["green1LastName"]
        codeName = playerValues["green1CodeName"]

        hdb.playerAdd(id, firstName, lastName, codeName)

    return jsonify(playerValues)

if __name__ == '__main__':
    app.run(debug=True)