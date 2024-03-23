import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerApellidos(apellidos):
    """Extrae los apellidos y lo coloca en el formato json estandar"""
    if idActual.global_redirrecion:
        controller.actualizar_cliente(json.dumps({"apellidos": apellidos}))
        idActual.resetRedirreccion()
    else:
        controller.actualizar_cliente(json.dumps({"apellidos": apellidos}))
        idActual.global_id = 4
    return json.dumps({"apellidos": apellidos})
    


def getGrafoChatID3():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerApellidos",
                "description": "Esta función extrae los apellidos del usuario en un string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "apellidos": {
                            "type": "string",
                            "description": "Apellidos del usuario."
                        },
                    },
                    "required": ["apellidos"]
                }
            }
        }
        ]

    available_functions = {
                "extraerApellidos":extraerApellidos
            }

    prompt = f"""Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Tu único trabajo es preguntar al usuario cuales son sus apellidos. (e.g. 'Ayúdame con tus apellidos por favor.')
    2. Debes verificar con cuidado si el usuario responde efectivmente a esta ultima pregunta, o si por otro lado, parece que se ha desviado en la conversación.
    3. Si el usuario se desvía en la conversación debes insistir en preguntarle cuales son sus apellidos. 
    4. Una vez que el usuario ha proporcionado sus apellidos llamas a la función extraerApellidos, lo cual hará que la conversación continue con el siguiente bot que le pedirá sus nombres.
    5. No te dirijas al usuario por sus apellidos ya que esto es un poco grosero.
    6. En el caso que la conversación regrese a este bot porque el usuario pidió correcciones, asegúrate que el nuevo valor reservado sea diferente de {controller.obtener_valor_cliente('nombres')}.
    7. En caso de que el usuario solicite una corección de otro dato y provea el nuevo dato directamente, agrádecele e infórmale que su dato fue corregido
    """
    return grafoChat(3, available_functions, lista_de_tools, None, prompt, True)