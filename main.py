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
        Code = playerValues["red1Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red2ID"]
        Code = playerValues["red2Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red3ID"]
        Code = playerValues["red3Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red4ID"]
        Code = playerValues["red4Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red5ID"]
        Code = playerValues["red5Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red6ID"]
        Code = playerValues["red6Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red7ID"]
        Code = playerValues["red7Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red8ID"]
        Code = playerValues["red8Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red9ID"]
        Code = playerValues["red9Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red10ID"]
        Code = playerValues["red10Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red11ID"]
        Code = playerValues["red11Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red12ID"]
        Code = playerValues["red12Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red13ID"]
        Code = playerValues["red13Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red14ID"]
        Code = playerValues["red14Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red15ID"]
        Code = playerValues["red15Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green1ID"]
        Code = playerValues["green1Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green2ID"]
        Code = playerValues["green2Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green3ID"]
        Code = playerValues["green3Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green4ID"]
        Code = playerValues["green4Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green5ID"]
        Code = playerValues["green5Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green6ID"]
        Code = playerValues["green6Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green7ID"]
        Code = playerValues["green7Code"]
        hdb.playerAdd(id, Code)
        
        id = playerValues["green8ID"]
        Code = playerValues["green8Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green9ID"]
        Code = playerValues["green9Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green10ID"]
        Code = playerValues["green10Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green11ID"]
        Code = playerValues["green11Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green12ID"]
        Code = playerValues["green12Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green13ID"]
        Code = playerValues["green13Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green14ID"]
        Code = playerValues["green14Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green15ID"]
        Code = playerValues["green15Code"]
        hdb.playerAdd(id, Code)

    return jsonify(playerValues)

@app.route('/ActionScreen', methods = ['GET'])
def action_screen():
    return render_template('ActionScreen.html')

@app.route('/getPlayers', methods = ['GET'])
def getPlayers():
    if request.method == 'GET':
        getStuff = hdb.getPlayers()

        red1ID = getStuff[0][0]
        red1Code = getStuff[0][1]

        red2ID = getStuff[2][0]
        red2Code = getStuff[2][1]

        red3ID = getStuff[4][0]
        red3Code = getStuff[4][1]

        red4ID = getStuff[6][0]
        red4Code = getStuff[6][1]

        red5ID = getStuff[8][0]
        red5Code = getStuff[8][1]

        red6ID = getStuff[10][0]
        red6Code = getStuff[10][1]

        red7ID = getStuff[12][0]
        red7Code = getStuff[12][1]

        red8ID = getStuff[14][0]
        red8Code = getStuff[14][1]

        red9ID = getStuff[16][0]
        red9Code = getStuff[16][1]

        red10ID = getStuff[18][0]
        red10Code = getStuff[18][1]

        red11ID = getStuff[20][0]
        red11Code = getStuff[20][1]

        red12ID = getStuff[22][0]
        red12Code = getStuff[22][1]

        red13ID = getStuff[24][0]
        red13Code = getStuff[24][1]

        red14ID = getStuff[26][0]
        red14Code = getStuff[26][1]

        red15ID = getStuff[28][0]
        red15Code = getStuff[28][1]

        green1ID = getStuff[1][0]
        green1Code = getStuff[1][1]

        green2ID = getStuff[3][0]
        green2Code = getStuff[3][1]

        green3ID = getStuff[5][0]
        green3Code = getStuff[5][1]

        green4ID = getStuff[7][0]
        green4Code = getStuff[7][1]

        green5ID = getStuff[9][0]
        green5Code = getStuff[9][1]

        green6ID = getStuff[11][0]
        green6Code = getStuff[11][1]

        green7ID = getStuff[13][0]
        green7Code = getStuff[13][1]

        green8ID = getStuff[15][0]
        green8Code = getStuff[15][1]

        green9ID = getStuff[17][0]
        green9Code = getStuff[17][1]

        green10ID = getStuff[19][0]
        green10Code = getStuff[19][1]

        green11ID = getStuff[21][0]
        green11Code = getStuff[21][1]

        green12ID = getStuff[23][0]
        green12Code = getStuff[23][1]

        green13ID = getStuff[25][0]
        green13Code = getStuff[25][1]

        green14ID = getStuff[27][0]
        green14Code = getStuff[27][1]

        green15ID = getStuff[29][0]
        green15Code = getStuff[29][1]

        dictionary = {
            "red1ID" : red1ID,
            "red1Code" : red1Code,
            "red2ID" : red2ID,
            "red2Code" : red2Code,
            "red3ID" : red3ID,
            "red3Code" : red3Code,
            "red4ID" : red4ID,
            "red4Code" : red4Code,
            "red5ID" : red5ID,
            "red5Code" : red5Code,
            "red6ID" : red6ID,
            "red6Code" : red6Code,
            "red7ID" : red7ID,
            "red7Code" : red7Code,
            "red8ID" : red8ID,
            "red8Code" : red8Code,
            "red9ID" : red9ID,
            "red9Code" : red9Code,
            "red10ID" : red10ID,
            "red10Code" : red10Code,
            "red11ID" : red11ID,
            "red11Code" : red11Code,
            "red12ID" : red12ID,
            "red12Code" : red12Code,
            "red13ID" : red13ID,
            "red13Code" : red13Code,
            "red14ID" : red14ID,
            "red14Code" : red14Code,
            "red15ID" : red15ID,
            "red15Code" : red15Code,
            "green1ID" : green1ID,
            "green1Code" : green1Code,
            "green2ID" : green2ID,
            "green2Code" : green2Code,
            "green3ID" : green3ID,
            "green3Code" : green3Code,
            "green4ID" : green4ID,
            "green4Code" : green4Code,
            "green5ID" : green5ID,
            "green5Code" : green5Code,
            "green6ID" : green6ID,
            "green6Code" : green6Code,
            "green7ID" : green7ID,
            "green7Code" : green7Code,
            "green8ID" : green8ID,
            "green8Code" : green8Code,
            "green9ID" : green9ID,
            "green9Code" : green9Code,
            "green10ID" : green10ID,
            "green10Code" : green10Code,
            "green11ID" : green11ID,
            "green11Code" : green11Code,
            "green12ID" : green12ID,
            "green12Code" : green12Code,
            "green13ID" : green13ID,
            "green13Code" : green13Code,
            "green14ID" : green14ID,
            "green14Code" : green14Code,
            "green15ID" : green15ID,
            "green15Code" : green15Code,

        }   

if __name__ == '__main__':
    app.run(debug=True)