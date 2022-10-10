import psycopg2

class HerokuConnect():
    def __init__(self):
        pass

    def playerAdd(self, id, first_name, last_name, codename):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.codename = codename

        try:
            conn = psycopg2.connect(dbname="d8e3b1c4anp49e", user="xoyrvlttghwzit", password="510506114c54b4ea19e8d481bb4205f2ef0e11c6b4acb86f8f3e70daf3a7969e", host="ec2-44-207-133-100.compute-1.amazonaws.com")
            cur = conn.cursor()
        except:
            print("Couldn't Connect!")

        sqlInsert = "INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s)"
        playerValues = (self.id, self.first_name, self.last_name, self.codename)

        try:
            cur.execute(sqlInsert, playerValues)
            conn.commit()
        except:
            print("Couldn't Add Player!")

        conn.close()