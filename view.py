# importando SQLite
import sqlite3 as lite 

# criando consexão
con = lite.connect('dados.db')


#---------------------------------------------

#inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query =  '''
        INSERT INTO inventario(
            nome,
            local,
            descricao,
            marca,
            data_da_compra,
            valor_da_compra,
            serie,
            imagem
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cur.execute(query, i)
 
 #--------------------------------

# visualizar banco
def vw_form():
    vw_dados = []
    with con:
        cur = con.cursor()
        query =  'SELECT * FROM inventario'
        cur.execute(query)
        
        rows = cur.fetchall()
        for row in rows:
            vw_dados.append(row)
    return vw_dados
        
#----------------------------------------

# atualizar dados
def atualizar_(i):
    with con:
        cur = con.cursor()
        query =  '''
        UPDATE 
            inventario
        SET
            nome = ?,
            local = ?,
            descricao = ?,
            marca = ?,
            data_da_compra = ?,
            valor_da_compra = ?,
            serie = ?,
            imagem = ?
        
        WHERE
            id = ?
        '''
        cur.execute(query, i)

#-------------------------------------------

# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query =  'DELETE FROM inventario WHERE id = ?'
        cur.execute(query, i)
    
# -------------------------------------------   

# visualizar dados individuais
def vw_item(id):
    vw_dados_idividual = []
    with con:
        cur = con.cursor()
        query =  'SELECT * FROM inventario WHERE id = ?'
        cur.execute(query, id)
        
        rows = cur.fetchall()
        for row in rows:
            vw_dados_idividual.append(row)
    
    return vw_dados_idividual
            
   