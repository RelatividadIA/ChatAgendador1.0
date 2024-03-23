import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def determinarArrepentimiento(seccion):
    """
    Analiza el contenido de la conversación para identificar si el usuario desea modificar algún dato previamente proporcionado.
    Si es así, redirige la conversación a la sección correspondiente basándose en el ID proporcionado.

    Parámetros:
    seccion (int): ID numérico de la sección a la cual redirigir. Los valores posibles son:
                2 (número de teléfono), 3 (apellidos), 4 (nombres), 5 (email).
    Retorna:
    str: Mensaje indicando si hubo o no redirección, y el destino de la redirección si la hubo.
    """
    if seccion >= idActual.global_id:
        return("No hubo redirección")
    else:
        idActual.global_id = seccion
        idActual.global_redirrecion = True
        return f"Redirección realizada al grafoChat con ID {seccion}."
    
    

def getGrafoChatID7():
    #
    lista_de_tools = [
        {
            "type": "function",
            "function": {
                "name": "determinarArrepentimiento",
                "description": "Identifica si el usuario desea modificar un dato y redirige la conversación según el ID de la sección especificada.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "seccion": {
                            "type": "number",
                            "description": """
                            ID numérico de la sección para corrección de datos:
                            2: Corrección de número de teléfono.
                            3: Corrección de apellidos.
                            4: Corrección de nombres.
                            5: Corrección de email.
                            """
                        },
                    },
                    "required": ["seccion"]
                }
            }
        }

        ]

    available_functions = {
                "determinarArrepentimiento":determinarArrepentimiento
            }

    prompt = """
    Como bot de atención al cliente para agendamiento de citas, tu tarea es gestionar conversaciones y corregir datos del usuario cuando sea necesario.
    Debes:
    1. Recibir la conversación y leerla
    2. En caso de que el cliente manifieste que quiere corregir algún dato, o que se ha equivocado cuando dio un dato vas a llamar a la función determinarArrepentimiento
    
    """
    return grafoChat(7, available_functions, lista_de_tools, None, prompt, False, True)