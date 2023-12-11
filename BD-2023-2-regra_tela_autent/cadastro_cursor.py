import sqlite3

comn = sqlite3.connect("sgmld_sem_heranca_alim.db")
cursor = comn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS USUARIO(
        ID_USER INTEGER PRIMARY KEY,
        Nome TEXT,
        Sobrenome TEXT,
        Login TEXT,
        Senha TEXT,
        URI_foto_user TEXT,
        Funcao TEXT
        );
    """)