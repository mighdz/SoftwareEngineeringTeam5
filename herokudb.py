import psycopg2

class HerokuConnect():
    def __init__(self):
        pass

    def playerAdd(self, id, Code):
        self.id = id
        self.Code = Code

        try:
            conn = psycopg2.connect(dbname="d8e3b1c4anp49e", user="xoyrvlttghwzit", password="510506114c54b4ea19e8d481bb4205f2ef0e11c6b4acb86f8f3e70daf3a7969e", host="ec2-44-207-133-100.compute-1.amazonaws.com")
            cur = conn.cursor()
        except:
            print("Couldn't Connect!")

        sqlInsert = "INSERT INTO player (id, Code) VALUES (%s, %s)"
        playerValues = (self.id, self.Code)

        if self.id is not None:
            try:
                cur.execute(sqlInsert, playerValues)
                conn.commit()
            except:
                print("Couldn't Add Player!")

        conn.close()
    
    def playerGet(self):
        try:
            conn_get = psycopg2.connect(dbname="d8e3b1c4anp49e", user="xoyrvlttghwzit", password="510506114c54b4ea19e8d481bb4205f2ef0e11c6b4acb86f8f3e70daf3a7969e", host="ec2-44-207-133-100.compute-1.amazonaws.com")
            cur_get = conn_get.cursor()
        except:
            print("Couldn't Connect to get!")
        
        try:
            cur_get.execute("SELECT * FROM player")
            record = cur_get.fetchall()
        except:
            print("Get failed")
        
        conn_get.close()
        return record