import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerNombres(nombres):
    """Extrae los nombres y lo coloca en el formato json estandar"""
    if idActual.global_redirrecion:
        controller.actualizar_cliente(json.dumps({"nombres": nombres}))        
        idActual.resetRedirreccion()
    else:
        controller.actualizar_cliente(json.dumps({"nombres": nombres}))
        idActual.global_id = 5

    return json.dumps({"nombres": nombres})
    


def getGrafoChatID4():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerNombres",
                "description": "Esta función extrae los nombres (sin apellidos) del usuario en un string.",
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

    prompt = f"""Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Eres un chat que ya conoce los apellidos del usuario, estos son {controller.obtener_valor_cliente("apellidos")} pero todavía no sus nombres. Tu único trabajo es preguntar al usuario cuales son sus nombres. (e.g. 'Ayúdame con tus nombres por favor.')
    2. Debes verificar con cuidado si el usuario responde efectivamente a esta ultima pregunta, o si por otro lado, parece que se ha desviado en la conversación.
    3. Si el usuario se desvía en la conversación debes insistir en preguntarle cuales son sus nombres. 
    4. Una vez que el usuario ha proporcionado sus nombres llamas a la función extraerNombres, pasando únicamente sus nombres y no sus apellidos (LOS NOMBRES SON DIFERENTES A SUS APELLIDOS), lo cual hará que la conversación continue con el siguiente bot que le pedirá un correo electrónico.
    5. En caso de que el usuario solicite una corección de otro dato y provea el nuevo dato directamente, agrádecele e infórmale que su dato fue corregido
    """
    return grafoChat(4, available_functions, lista_de_tools, None, prompt, True)