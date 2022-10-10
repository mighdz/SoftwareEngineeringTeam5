import code
import psycopg2

class Heroku():
    def __init__(self):
        pass

    def playerAdd(self, id, firstName, lastName, codename):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.codeName = codename

        try:
            conn = psycopg2.connect(dbname="d8e3b1c4anp49e", user="xoyrvlttghwzit", password="510506114c54b4ea19e8d481bb4205f2ef0e11c6b4acb86f8f3e70daf3a7969e", host="ec2-44-207-133-100.compute-1.amazonaws.com")
            cur = conn.cursor()
        except:
            print("Couldn't Connect!")

        sqlInsert = "INSERT INTO player (id, firstName, lastName, codename) VALUES (%s, %s, %s, %s)"
        playerValues = (self.id, self.firstName, self.lastName, self.codeName)

        try:
            cur.execute(sqlInsert, playerValues)
            conn.commit()
        except:
            print("Couldn't Add Player!")

        conn.close()