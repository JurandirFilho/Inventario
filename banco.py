# importando SQLite
import sqlite3 as lite 

# criando consexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute('''
                CREATE TABLE inventario(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE ,
                    local TEXT NOT NULL,
                    descricao NOT NULL,
                    marca TEX NOT NULL,
                    data_da_compra DATE NOT NULL,
                    valor_da_compra DECIMAL NOT NULL,
                    serie TEXT,
                    imagem TEXT
                )
                ''')