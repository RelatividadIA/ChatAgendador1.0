import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerNombres(nombres):
    """Extrae los nombres y lo coloca en el formato json estandar"""
    if controller.verificarExistencia(json.dumps({"nombres": nombres})):
        pass
    else:
        print("No está en la base de datos")
        idActual.global_id = 5
    

    return json.dumps({"nombres": nombres})

def getGrafoChatID4():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerNombres",
                "description": "Esta función extrae los nombres del usuario en un string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nombres": {
                            "type": "string",
                            "description": "nombres del usuario."
                        },
                    },
                    "required": ["nombres"]
                }
            }
        }
        ]

    available_functions = {
                "extraerNombres":extraerNombres
            }

    prompt = """Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Ere un chat que ya conoce los apellidos del usuario pero todavía no sus nombres. Tu único trabajo es preguntar al usuario cuales son sus nombres. (e.g. 'Ayúdame con tus nombres por favor.')
    2. Debes verificar con cuidado si el usuario responde efectivmente a esta ultima pregunta, o si por otro lado, parece que se ha desviado en la conversación.
    3. Si el usuario se desvía en la conversación debes insistir en preguntarle cuales son sus nombres. 
    4. Una vez que el usuario ha proporcionado sus nombres llamas a la función extraerNombres, lo cual hará que la conversación continue con el siguiente bot que le pedirá un correo electrónico.
    """
    return grafoChat(4, available_functions, lista_de_tools, None, prompt)