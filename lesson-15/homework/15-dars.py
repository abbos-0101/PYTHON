import sqlite3

# Yangi ma'lumotlar bazasini yaratish (yoki mavjud bo'lsa ochish)
with sqlite3.connect('new_roster.db') as con:
    cursor = con.cursor()

    # Jadval yaratish
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)


cursor.execute("DELETE FROM Roster")
    
    # Yangi ma'lumotlarni qo'shamiz
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
    con.commit()

    # Tekshirib ko'rsatamiz
    cursor.execute("SELECT * FROM Roster")
    print(cursor.fetchall())


import sqlite3

with sqlite3.connect('homework15.db') as con:
    cursor = con.cursor()
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    con.commit()

    # Natijani tekshirish uchun:
    cursor.execute("SELECT * FROM Roster")
    result = cursor.fetchall()
    print(result)


import sqlite3

with sqlite3.connect('homework15.db') as con:
    cursor = con.cursor()
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    result = cursor.fetchall()
    print(result)
