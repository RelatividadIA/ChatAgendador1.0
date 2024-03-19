
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="314159",
        database = "crud_clientes"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
    

    
connectionBD()

