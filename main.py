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

        # id = playerValues["red3ID"]
        # Code = playerValues["red3Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green3ID"]
        # Code = playerValues["green3Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red4ID"]
        # Code = playerValues["red4Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green4ID"]
        # Code = playerValues["green4Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red5ID"]
        # Code = playerValues["red5Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green5ID"]
        # Code = playerValues["green5Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red6ID"]
        # Code = playerValues["red6Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green6ID"]
        # Code = playerValues["green6Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red7ID"]
        # Code = playerValues["red7Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green7ID"]
        # Code = playerValues["green7Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red8ID"]
        # Code = playerValues["red8Code"]
        # hdb.playerAdd(id, Code)
        
        # id = playerValues["green8ID"]
        # Code = playerValues["green8Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red9ID"]
        # Code = playerValues["red9Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green9ID"]
        # Code = playerValues["green9Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red10ID"]
        # Code = playerValues["red10Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green10ID"]
        # Code = playerValues["green10Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red11ID"]
        # Code = playerValues["red11Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green11ID"]
        # Code = playerValues["green11Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red12ID"]
        # Code = playerValues["red12Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green12ID"]
        # Code = playerValues["green12Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red13ID"]
        # Code = playerValues["red13Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green13ID"]
        # Code = playerValues["green13Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red14ID"]
        # Code = playerValues["red14Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green14ID"]
        # Code = playerValues["green14Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["red15ID"]
        # Code = playerValues["red15Code"]
        # hdb.playerAdd(id, Code)

        # id = playerValues["green15ID"]
        # Code = playerValues["green15Code"]
        # hdb.playerAdd(id, Code)

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
        r3ID = -1
        r4ID = -1
        r5ID = -1
        r6ID = -1
        r7ID = -1
        r8ID = -1
        r9ID = -1
        r10ID = -1
        r11ID = -1
        r12ID = -1
        r13ID = -1
        r14ID = -1
        r15ID = -1
        g1ID = -1
        g2ID = -1
        g3ID = -1
        g4ID = -1
        g5ID = -1
        g6ID = -1
        g7ID = -1
        g8ID = -1
        g9ID = -1
        g10ID = -1
        g11ID = -1
        g12ID = -1
        g13ID = -1
        g14ID = -1
        g15ID = -1
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

        try:
            r3ID = getStuff[4][0]
            r3Code = getStuff[4][1]
            dictionary["red3ID"]=r3ID
            dictionary["red3Code"]=r3Code
        except IndexError:
            print("No value here!")

        try:
            g3ID = getStuff[5][0]
            g3Code = getStuff[5][1]
            dictionary["green3ID"]=g3ID
            dictionary["green3Code"]=g3Code
        except IndexError:
            print("No value here!")

        try:
            r4ID = getStuff[6][0]
            r4Code = getStuff[6][1]
            dictionary["red4ID"]=r4ID
            dictionary["red4Code"]=r4Code
        except IndexError:
            print("No value here!")

        try:
            g4ID = getStuff[7][0]
            g4Code = getStuff[7][1]
            dictionary["green4ID"]=g4ID
            dictionary["green4Code"]=g4Code
        except IndexError:
            print("No value here!")

        try:
            r5ID = getStuff[8][0]
            r5Code = getStuff[8][1]
            dictionary["red5ID"]=r5ID
            dictionary["red5Code"]=r5Code
        except IndexError:
            print("No value here!")

        try:
            g5ID = getStuff[9][0]
            g5Code = getStuff[9][1]
            dictionary["green5ID"]=g5ID
            dictionary["green5Code"]=g5Code
        except IndexError:
            print("No value here!")

        try:
            r6ID = getStuff[10][0]
            r6Code = getStuff[10][1]
            dictionary["red6ID"]=r6ID
            dictionary["red6Code"]=r6Code
        except IndexError:
            print("No value here!")

        try:
            g6ID = getStuff[11][0]
            g6Code = getStuff[11][1]
            dictionary["green6ID"]=g6ID
            dictionary["green6Code"]=g6Code
        except IndexError:
            print("No value here!")

        try:
            r7ID = getStuff[12][0]
            r7Code = getStuff[12][1]
            dictionary["red7ID"]=r7ID
            dictionary["red7Code"]=r7Code
        except IndexError:
            print("No value here!")

        try:
            g7ID = getStuff[13][0]
            g7Code = getStuff[13][1]
            dictionary["green7ID"]=g7ID
            dictionary["green7Code"]=g7Code
        except IndexError:
            print("No value here!")

        try:
            r8ID = getStuff[14][0]
            r8Code = getStuff[14][1]
            dictionary["red8ID"]=r8ID
            dictionary["red8Code"]=r8Code

        except IndexError:
            print("No value here!")

        try:
            g8ID = getStuff[15][0]
            g8Code = getStuff[15][1]
            dictionary["green8ID"]=g8ID
            dictionary["green8Code"]=g8Code
        except IndexError:
            print("No value here!")

        try:
            r9ID = getStuff[16][0]
            r9Code = getStuff[16][1]
            dictionary["red9ID"]=r9ID
            dictionary["red9Code"]=r9Code

        except IndexError:
            print("No value here!")

        try:
            g9ID = getStuff[17][0]
            g9Code = getStuff[17][1]
            dictionary["green9ID"]=g9ID
            dictionary["green9Code"]=g9Code
        except IndexError:
            print("No value here!")

        try:
            r10ID = getStuff[18][0]
            r10Code = getStuff[18][1]
            dictionary["red10ID"]=r10ID
            dictionary["red10Code"]=r10Code

        except IndexError:
            print("No value here!")

        try:
            g10ID = getStuff[19][0]
            g10Code = getStuff[19][1]
            dictionary["green10ID"]=g10ID
            dictionary["green10Code"]=g10Code
        except IndexError:
            print("No value here!")

        try:
            r11ID = getStuff[20][0]
            r11Code = getStuff[20][1]
            dictionary["red11ID"]=r11ID
            dictionary["red11Code"]=r11Code

        except IndexError:
            print("No value here!")

        try:
            g11ID = getStuff[21][0]
            g11Code = getStuff[21][1]
            dictionary["green11ID"]=g11ID
            dictionary["green11Code"]=g11Code
        except IndexError:
            print("No value here!")

        try:
            r12ID = getStuff[22][0]
            r12Code = getStuff[22][1]
            dictionary["red12ID"]=r12ID
            dictionary["red12Code"]=r12Code
        except IndexError:
            print("No value here!")

        try:
            g12ID = getStuff[23][0]
            g12Code = getStuff[23][1]
            dictionary["green12ID"]=g12ID
            dictionary["green12Code"]=g12Code
        except IndexError:
            print("No value here!")

        try:
            r13ID = getStuff[24][0]
            r13Code = getStuff[24][1]
            dictionary["red13ID"]=r13ID
            dictionary["red13Code"]=r13Code

        except IndexError:
            print("No value here!")

        try:
            g13ID = getStuff[25][0]
            g13Code = getStuff[25][1]
            dictionary["green13ID"]=g13ID
            dictionary["green13Code"]=g13Code
        except IndexError:
            print("No value here!")

        try:
            r14ID = getStuff[26][0]
            r14Code = getStuff[26][1]
            dictionary["red14ID"]=r14ID
            dictionary["red14Code"]=r14Code
        except IndexError:
            print("No value here!")

        try:
            g14ID = getStuff[27][0]
            g14Code = getStuff[27][1]
            dictionary["green14ID"]=g14ID
            dictionary["green14Code"]=g14Code
        except IndexError:
            print("No value here!")

        try:
            r15ID = getStuff[28][0]
            r15Code = getStuff[28][1]
            dictionary["red15ID"]=r15ID
            dictionary["red15Code"]=r15Code
        except IndexError:
            print("No value here!")

        try:
            g15ID = getStuff[29][0]
            g15Code = getStuff[29][1]
            dictionary["green15ID"]=g15ID
            dictionary["green15Code"]=g15Code
        except IndexError:
            print("No value here!")

        c_msg = str(dictionary)
        bytesToSend = str.encode(c_msg)
        client_socket.sendto(bytesToSend, serverPort)

        s_msg = client_socket.recvfrom(7501)
        msg = "{}".format(s_msg[0])

        s_msg = client_socket.recvfrom(7501)
        redPoints = "{}".format(s_msg[0])

        s_msg = client_socket.recvfrom(7501)
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

        if r3ID != -1:
            dictionaryWithPoints["red3ID"]=r3ID
            dictionaryWithPoints["red3Code"]=r3Code

        if g3ID != -1:
            dictionaryWithPoints["green3ID"]=g3ID
            dictionaryWithPoints["green3Code"]=g3Code

        if r4ID != -1:
            dictionaryWithPoints["red4ID"]=r4ID
            dictionaryWithPoints["red4Code"]=r4Code

        if g4ID != -1:
            dictionaryWithPoints["green4ID"]=g4ID
            dictionaryWithPoints["green4Code"]=g4Code

        if r5ID != -1:
            dictionaryWithPoints["red5ID"]=r5ID
            dictionaryWithPoints["red5Code"]=r5Code

        if g5ID != -1:
            dictionaryWithPoints["green5ID"]=g5ID
            dictionaryWithPoints["green5Code"]=g5Code

        if r6ID != -1:
            dictionaryWithPoints["red6ID"]=r6ID
            dictionaryWithPoints["red6Code"]=r6Code

        if g6ID != -1:
            dictionaryWithPoints["green6ID"]=g6ID
            dictionaryWithPoints["green6Code"]=g6Code

        if r7ID != -1:
            dictionaryWithPoints["red7ID"]=r7ID
            dictionaryWithPoints["red7Code"]=r7Code

        if g7ID != -1:
            dictionaryWithPoints["green7ID"]=g7ID
            dictionaryWithPoints["green7Code"]=g7Code

        if r8ID != -1:
            dictionaryWithPoints["red8ID"]=r8ID
            dictionaryWithPoints["red8Code"]=r8Code

        if g8ID != -1:
            dictionaryWithPoints["green8ID"]=g8ID
            dictionaryWithPoints["green8Code"]=g8Code

        if r9ID != -1:
            dictionaryWithPoints["red9ID"]=r9ID
            dictionaryWithPoints["red9Code"]=r9Code

        if g9ID != -1:
            dictionaryWithPoints["green9ID"]=g9ID
            dictionaryWithPoints["green9Code"]=g9Code

        if r10ID != -1:
            dictionaryWithPoints["red10ID"]=r10ID
            dictionaryWithPoints["red10Code"]=r10Code

        if g10ID != -1:
            dictionaryWithPoints["green10ID"]=g10ID
            dictionaryWithPoints["green10Code"]=g10Code

        if r11ID != -1:
            dictionaryWithPoints["red11ID"]=r11ID
            dictionaryWithPoints["red11Code"]=r11Code

        if g11ID != -1:
            dictionaryWithPoints["green11ID"]=g11ID
            dictionaryWithPoints["green11Code"]=g11Code

        if r12ID != -1:
            dictionaryWithPoints["red12ID"]=r12ID
            dictionaryWithPoints["red12Code"]=r12Code

        if g12ID != -1:
            dictionaryWithPoints["green12ID"]=g12ID
            dictionaryWithPoints["green12Code"]=g12Code

        if r13ID != -1:
            dictionaryWithPoints["red13ID"]=r13ID
            dictionaryWithPoints["red13Code"]=r13Code

        if g13ID != -1:
            dictionaryWithPoints["green13ID"]=g13ID
            dictionaryWithPoints["green13Code"]=g13Code

        if r14ID != -1:
            dictionaryWithPoints["red14ID"]=r14ID
            dictionaryWithPoints["red14Code"]=r14Code

        if g14ID != -1:
            dictionaryWithPoints["green14ID"]=g14ID
            dictionaryWithPoints["green14Code"]=g14Code

        if r15ID != -1:
            dictionaryWithPoints["red15ID"]=r15ID
            dictionaryWithPoints["red15Code"]=r15Code

        if g15ID != -1:
            dictionaryWithPoints["green15ID"]=g15ID
            dictionaryWithPoints["green15Code"]=g15Code

        dictionaryWithPoints["events"]=msg
        dictionaryWithPoints["redPoints"]=redPoints
        dictionaryWithPoints["greenPoints"]=greenPoints
        return jsonify(dictionaryWithPoints)

if __name__ == '__main__':
    app.run(debug=True)