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
            conn = psycopg2.connect(dbname="dc97213o4m7k5p", user="vktqphxyullurz", password="144c8c9e523fd6a3061d83559e3ffee9a7f78e4e83f7932f44000204b82fee9e", host="ec2-34-239-81-70.compute-1.amazonaws.com")
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