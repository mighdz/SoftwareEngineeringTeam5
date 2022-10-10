from flask import Flask, render_template, request
from herokudb import Heroku

app = Flask(__name__)

#Declare class from herokudb.py
herokudb = Heroku()

# @app.route("/")
# def home():
#     return render_template("EntryScreen.html")

@app.route("/entry_screen")
def entryScreen():
    return render_template("EntryScreen.html")



if __name__ == '__main__':
    app.run(debug=True)