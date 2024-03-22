from random import sample
from modulos.dataBase.conexionBD import *  #Importando conexion BD
import json
import modulos.dataBase.identificadorDB

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

def update_cliente_celular(celularJSONSTR):
    mydb = connectionBD()
    cursor = mydb.cursor()
    celular_actual = modulos.dataBase.identificadorDB.celular
    nuevoCelular = json.loads(celularJSONSTR)['celular']
    
    try:
        # Preparamos la consulta SQL para actualizar el número de celular del cliente.
        query = "UPDATE clientes SET celular = %s WHERE celular = %s"
        values = (nuevoCelular, celular_actual)

        # Ejecutamos la consulta SQL.
        cursor.execute(query, values)

        # Confirmamos los cambios en la base de datos.
        mydb.commit()

        print(f"Celular actualizado exitosamente a {nuevoCelular} para el cliente.")
        modulos.dataBase.identificadorDB.celular = nuevoCelular
        return
    except mysql.connector.Error as error:
        print(f"Error al actualizar el celular del cliente: {error}")
    finally:
        cursor.close()
        mydb.close()

def insertar_CelularCliente(json_str):
    # Convierte el string JSON en un diccionario de Python.
    data = json.loads(json_str)
    
    # Establece la conexión a la base de datos.
    connection = connectionBD()
    if connection is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return
    
    try:
        cursor = connection.cursor()
        # Inserta una nueva entrada en la tabla `clientes`.
        sql = "INSERT INTO `clientes` (`celular`) VALUES (%s)"
        cursor.execute(sql, (data['celular'],))
        
        # Confirma la transacción.
        connection.commit()
        
        print("Cliente insertado exitosamente.")
        
        modulos.dataBase.identificadorDB.celular = data['celular']

    except mysql.connector.Error as error:
        print("Error al insertar el cliente: {}".format(error))
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("La conexión a la base de datos ha sido cerrada.")

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
    
def actualizar_cliente(json_str):
    # Convierte el string JSON en un diccionario de Python.
    data = json.loads(json_str)
    propiedad = list(data.keys())[0]
    valor = data[propiedad]

    # Valida la propiedad a actualizar para asegurar que está permitida.
    propiedades_permitidas = ['nombres', 'apellidos', 'edad', 'sexo', 'email']
    if propiedad not in propiedades_permitidas:
        print("Propiedad no permitida para actualización.")
        return

    # Usa la variable global `celular` para determinar la entrada a actualizar.
    celular = modulos.dataBase.identificadorDB.celular

    # Establece la conexión a la base de datos.
    connection = connectionBD()
    if connection is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return

    try:
        cursor = connection.cursor()
        # Prepara la consulta SQL para actualizar la propiedad dada.
        sql = f"UPDATE `clientes` SET `{propiedad}` = %s WHERE `celular` = %s"
        cursor.execute(sql, (valor, celular))
        
        # Confirma la transacción.
        connection.commit()
        
        print(f"Cliente actualizado exitosamente: {propiedad} = {valor}.")

    except mysql.connector.Error as error:
        print(f"Error al actualizar el cliente: {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("La conexión a la base de datos ha sido cerrada.")

def obtener_valor_cliente(campo):
    # Asumimos que el módulo y el objeto con el número de celular existen y lo importamos
    celular = modulos.dataBase.identificadorDB.celular
    
    # Nos conectamos a la base de datos
    mydb = connectionBD()
    
    # Creamos un cursor
    cursor = mydb.cursor()
    
    # Construimos la consulta SQL
    sql = f"SELECT {campo} FROM clientes WHERE celular = %s"
    val = (celular,)
    
    # Ejecutamos la consulta
    cursor.execute(sql, val)
    
    # Obtenemos el resultado
    resultado = cursor.fetchone()
    
    # Cerramos el cursor y la conexión
    cursor.close()
    mydb.close()
    
    # Si hay un resultado, lo retornamos; si no, retornamos None
    if resultado:
        return resultado[0]
    else:
        return None
    
def obtener_datosJSON_cliente():
    mydb = connectionBD()
    if mydb is None:
        return "No se pudo conectar a la base de datos."
    
    celular_cliente = modulos.dataBase.identificadorDB.celular  # Acceso a la variable global
    
    cursor = mydb.cursor(dictionary=True)  # Usar cursor como diccionario
    query = "SELECT * FROM clientes WHERE celular = %s"
    cursor.execute(query, (celular_cliente,))
    
    resultado = cursor.fetchone()
    
    cursor.close()
    mydb.close()
    
    if resultado:
        return resultado
    else:
        return "No se encontró al cliente."