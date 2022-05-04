import sqlite3 as sl
import csv

class Datenbank:
    def __init__(self):
        self.con=self.make_database()  

    def make_database(self):
        #Falls schon ein Datenbank Objekt vorhanden ist
        #TODO: Was wenn die Datenbank Datei vorhanden ist, aber die Tabellen nicht gemacht sind?
        try:
            con = sl.connect('file:mosaik.db?mode=rw', uri=True)
            return con
        #Sonst mache ein neues und fülle es
        except:
            con = sl.connect('file:mosaik.db?mode=rwc', uri=True)
            con=self.create_hefte(con)
            con=self.create_serie(con)
            con=self.fill_hefte(con,self.load_csv("Hefte"))
            con=self.fill_serie(con,self.load_csv("serien_namen"))
            return con

    def create_hefte(self,con):
        with con:
            con.execute("""
            CREATE TABLE Hefte (
                nummer INTEGER NOT NULL PRIMARY KEY,
                titel TEXT,
                jahr INTEGER,
                monat String,
                serien_id INTEGER
                );
            """)
        return con

    def create_serie(self,con):
        with con:
            con.execute("""
            CREATE TABLE Serie(
                serien_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name String
            )
            """)
        return con

    def fill_serie(self,con,data):
        sql = 'INSERT INTO Serie (name) values(?)'
        with con:
            con.executemany(sql,data) 
        con.commit()
        return con

    def fill_hefte(self,con,data):
        sql = 'INSERT INTO Hefte (nummer,titel, jahr,monat,serien_id) values(?,?,?,?,?)'
        with con:
            con.executemany(sql,data)
        con.commit()
        return con

    #nur für debugging Zwecke
    def get_table(self,name):
        with self.con:
            data = self.con.execute("SELECT * FROM "+name)
            for row in data:
                print(row)
    
    #lädt csv
    def load_csv(self,name):
        with open('Daten/'+name+'.csv', newline='', mode='r', encoding='utf-8-sig') as csvfile:
            text= csv.reader(csvfile, dialect="excel",delimiter=";")
            new_text=list(text)
        return new_text

    def change_binary_month_to_sql(self,array):
        months=["Januar","Feburar", "März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
        sql="("
        first=True
        for i,value in enumerate(array):
            if value==1:
                if first:
                    sql=sql+"monat=\""+str(months[i])+"\" "
                    first=False
                else:
                    sql=sql+"OR monat=\""+str(months[i])+"\" "
        sql=sql+")"
        return sql

    def change_binary_serie_to_sql(self,array):
        series=[]
        with self.con:
            data=self.con.execute("SELECT * FROM Serie").fetchall()
        for row in data:
            series.append(row[1])
        first=True
        sql="("
        for i,value in enumerate(array):
            if value==1:
                if first:
                    sql=sql+"name=\""+str(series[i])+"\" "
                    first=False
                else:
                    sql=sql+"OR name=\""+str(series[i])+"\" "
        sql=sql+")"
        return sql

    def change_years_to_sql(self,array):
        sql="( "
        for value in array:
            sql=sql+" ("+" jahr "+"BETWEEN "+value[:4]+" AND "+value[5:]+")"+" OR "
        sql=sql[:-3]    #Um das letzte OR weg zu bekommen
        sql=sql+" )"
        return sql

    def handle_request(self,months,serie,years):
        try:
            month_sql=self.change_binary_month_to_sql(months)
            series_sql=self.change_binary_serie_to_sql(serie)
            years_sql=self.change_years_to_sql(years)
            print(years_sql)
            sql=""" SELECT nummer,titel,jahr,monat,Serie.name 
                    FROM Hefte INNER JOIN Serie ON Hefte.serien_id = Serie.serien_id
                    WHERE """
            sql=sql+month_sql+"AND"+series_sql+"AND"+years_sql+";"
            with self.con:
                data=self.con.execute(sql).fetchall()
            return data
        except:
            return None

    def get_heft_by_id(self,id):
        print("id")
        try:
            sql=""" SELECT nummer,titel,jahr,monat,Serie.name 
                    FROM Hefte INNER JOIN Serie ON Hefte.serien_id = Serie.serien_id
                    WHERE nummer="""
            sql=sql+id+";"
            with self.con:
                data=self.con.execute(sql).fetchone()
            return data
        except:
            return None
