import modulos.idActual as idActual
import modulos.dataBase.controller as controller
import modulos.dataBase.identificadorDB

from modulos.grafoChats.grafoChat import *

def extraerCelular(celular):
    """Extrae el número celular y lo coloca en el formato json estandar"""

    if controller.verificarExistencia(json.dumps({"celular": celular})):
        modulos.dataBase.identificadorDB.celular = celular
        idActual.global_id = 9
    else:
        print("No en la base de datos")
        controller.insertar_CelularCliente(json.dumps({"celular": celular}))
        idActual.global_id = 3


    return json.dumps({"celular": celular})

def getGrafoChatID8():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerCelular",
                "description": "Extrae el número de celular del usuario cuando este lo proporciona y pasa la conversación al siguiente bot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "celular": {
                            "type": "string",
                            "description": "Número celular del usuario"
                        },
                    },
                    "required": ["celular"]
                }
            }
        }
        ]

    available_functions = {
                "extraerCelular":extraerCelular
            }

    prompt = f"""Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Tu único trabajo informarlaes preguntarle al usuario cual es su número de celular meintras que le informas al usuario que esto lo haces con el propósito de identificarlo. 
    2. Debes verificar con cuidado si el usuario responde efectivmente a esta ultima pregunta, o si por otro lado, parece que no ha respondido a esta pregunta sino que se ha desviado en la conversación.
    3. Si el usuario se desvía en la conversación debes insistir en preguntarle cual es su número de celular. 
    4. Una vez que el usuario ha proporcionado su número de celular llamas a la función extraerCelular que almacenará el número de celular y hará que la conversación continua con el siguiente bot.
    """
    return grafoChat(8, available_functions, lista_de_tools, None, prompt)