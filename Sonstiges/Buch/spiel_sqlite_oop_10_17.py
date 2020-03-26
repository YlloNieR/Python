class Highscore:
    # Highscore in DB speichern
    def speichern(self, name, zeit):
        # Highscore-DB micht vorhanden, erzeugen
        if not glob.glob("highscore.db"):
            con = sqlite3.connect("highscore.db")
            cursor = con.cursor()
            sql = "CREATE TABLE daten(" \
                "name TEXT, " \
                "zeit REAL)"
            cursor.execute(sql)
            con.close()

       # Datensatz in DB schreiben
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "INSERT INTO daten VALUES('" \
            + name + "'," + str(zeit) + ")"
        cursor.execute(sql)
        con.commit()
        con.close()

    # Highscore anzeigen
    def __str__(self):
        # Highscore-DB nicht vorhanden
        if not glob.glob("highscore.db"):
            return "Keine Highscores vorhanden"

        # Highscores laden
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
        cursor.execute(sql)

        # Ausgabe Highscore
        ausgabe = " P. Name             Zeit\n"
        i = 1
        for dsatz in cursor:
            ausgabe += f"{i:2d}. {dsatz[0]:10}" \
                f"{dsatz[1]:5.2f} sec \n"
            i = i + 1

        # Verbindung beenden
        con.close()
        return ausgabe
