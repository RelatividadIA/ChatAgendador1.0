import idActual

from grafoChat import *

def extraerCelular(celular):
    """Extrae el número celular y lo coloca en el formato json estandar"""
    return json.dumps({"celular": celular})

def getGrafoChatID2():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerCelular",
                "description": "Después de que al usuario se le pregunte cual es su número celular y que este responda, se pasa su número celular para que se lo reserve",
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

    prompt = """Eres un experto en el agendamiento de citas, ahora tu único trabajo es preguntarle al usuario cual es su número celular. Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una conversación de antemano, evalúa esta conversación y únicamente enfócate en obtener el número de celular del usuario."""

    return grafoChat(2, available_functions, lista_de_tools, None, prompt)