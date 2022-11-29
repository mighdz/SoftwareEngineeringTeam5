import socket
import subprocess
from flask import Flask, render_template, request, jsonify, json
from herokudb import HerokuConnect


app = Flask(__name__)

subprocess.Popen(['python', 'server.py'])

#Declare class from herokudb.py
hdb = HerokuConnect()

serverPort = ("127.0.0.1", 7500)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
        
        id = playerValues["green1ID"]
        Code = playerValues["green1Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["red2ID"]
        Code = playerValues["red2Code"]
        hdb.playerAdd(id, Code)

        id = playerValues["green2ID"]
        Code = playerValues["green2Code"]
        hdb.playerAdd(id, Code)

    return jsonify(playerValues)

@app.route('/ActionScreen')
def action_screen():
    return render_template('ActionScreen.html')

@app.route('/getPlayers', methods = ['GET'])
def getPlayers():
    if request.method == 'GET':
        getStuff = hdb.playerGet()
        r1ID = -1
        r2ID = -1
        g1ID = -1
        g2ID = -1
        dictionary = {}
        try:
            r1ID = getStuff[0][0]
            r1Code = getStuff[0][1]
            dictionary["red1ID"]=r1ID
            dictionary["red1Code"]=r1Code
        except IndexError:
            print("No value here!")

        try:
            g1ID = getStuff[1][0]
            g1Code = getStuff[1][1]
            dictionary["green1ID"]=g1ID
            dictionary["green1Code"]=g1Code
        except IndexError:
            print("No value here!")

        try:
            r2ID = getStuff[2][0]
            r2Code = getStuff[2][1]
            dictionary["red2ID"]=r2ID
            dictionary["red2Code"]=r2Code
        except IndexError:
            print("No value here!")

        try:
            g2ID = getStuff[3][0]
            g2Code = getStuff[3][1]
            dictionary["green2ID"]=g2ID
            dictionary["green2Code"]=g2Code
        except IndexError:
            print("No value here!")

        c_msg = str(dictionary)
        bytesToSend = str.encode(c_msg)
        client_socket.sendto(bytesToSend, serverPort)

        s_msg = client_socket.recvfrom(1024)
        msg = "{}".format(s_msg[0])

        s_msg = client_socket.recvfrom(1024)
        redPoints = "{}".format(s_msg[0])

        s_msg = client_socket.recvfrom(1024)
        greenPoints = "{}".format(s_msg[0])

        dictionaryWithPoints = {}
        if r1ID != -1: 
            dictionaryWithPoints["red1ID"]=r1ID
            dictionaryWithPoints["red1Code"]=r1Code

        if g1ID != -1:
            dictionaryWithPoints["green1ID"]=g1ID
            dictionaryWithPoints["green1Code"]=g1Code

        if r2ID != -1:
            dictionaryWithPoints["red2ID"]=r2ID
            dictionaryWithPoints["red2Code"]=r2Code

        if g2ID != -1:
            dictionaryWithPoints["green2ID"]=g2ID
            dictionaryWithPoints["green2Code"]=g2Code

        dictionaryWithPoints["events"]=msg
        dictionaryWithPoints["redPoints"]=redPoints
        dictionaryWithPoints["greenPoints"]=greenPoints
        return jsonify(dictionaryWithPoints)

if __name__ == '__main__':
    app.run(debug=True)