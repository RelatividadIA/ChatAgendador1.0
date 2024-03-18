from random import sample
from modulos.dataBase.conexionBD import *  #Importando conexion BD
import json


#Creando una funcion para obtener la lista de guardias.
def listarDatos():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM clientes ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def registrarEntrada(datos_cliente):       
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
        
    # Crear la consulta SQL de inserción con todos los campos.
    sql = """
    INSERT INTO clientes(nombre, edad, sexo, teléfono, cedula, email) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    # Desempaquetar los valores del JSON para pasarlos como parámetros.
    valores = (
        datos_cliente.get('nombre', ''),
        datos_cliente.get('edad', ''),
        datos_cliente.get('sexo', ''),
        datos_cliente.get('teléfono', ''),
        datos_cliente.get('cedula', ''),
        datos_cliente.get('email', '')
    )
    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    
    resultado_insert = cursor.rowcount # Retorna 1 o 0 si se insertó el registro.
    ultimo_id = cursor.lastrowid # Retorna el ID del último registro insertado.
    
    cursor.close() # Cerrando conexión SQL
    conexion_MySQLdb.close() # Cerrando conexión de la BD
    print("Push exitoso")
    print(listarDatos())
    
    return resultado_insert, ultimo_id

def verificarExistencia(data):
    # Asumir que 'data' es un diccionario con una sola clave-valor
    data = json.loads(data)
    
    if not data or len(data) != 1:
        print("Datos inválidos. Se requiere un diccionario con un solo par clave-valor.")
        return False
    
    

    column_name, value = next(iter(data.items()))
    
    mydb = connectionBD()
    if mydb is None:
        return False

    try:
        cursor = mydb.cursor()
        query = f"SELECT EXISTS(SELECT 1 FROM clientes WHERE {column_name} = %s)"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        
        cursor.close()
        mydb.close()
        
        return result[0] == 1
    except mysql.connector.Error as err:
        print(f"Error en la base de datos: {err}")
        return False
    
