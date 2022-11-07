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
        codeName = playerValues["red1CodeName"]
        
        hdb.playerAdd(id, codeName)

        id = playerValues["green1ID"]
        codeName = playerValues["green1CodeName"]

        hdb.playerAdd(id, codeName)

    return jsonify(playerValues)

@app.route('/getPlayers', methods = ['GET'])
def getPlayers():
    if request.method == 'GET':
        dictionary = hdb.getPlayers()

        #Red1

        

if __name__ == '__main__':
    app.run(debug=True)