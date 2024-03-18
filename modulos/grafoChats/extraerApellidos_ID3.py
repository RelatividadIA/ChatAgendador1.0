import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerApellidos(apellidos):
    """Extrae los apellidos y lo coloca en el formato json estandar"""
    if controller.verificarExistencia(json.dumps({"apellidos": apellidos})):
        pass
    else:
        print("No en la base de datos")
        #idActual.global_id = 3
    

    return json.dumps({"apellidos": apellidos})

def getGrafoChatID3():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerApellidos",
                "description": "Después de que al usuario se le pregunte cuales son sus apellidos y que este responda, se pasa su/s apellido/s para que se lo/s reserve",
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
                "extraerCelular":extraerApellidos
            }

    prompt = """Eres un experto en el agendamiento de citas, ahora tu único trabajo es preguntarle al usuario cual es su número celular. Bajo ninguna otra condición harás cualquier otra acción, considera que puede que recibas una conversación de antemano, evalúa esta conversación y únicamente enfócate en obtener el número de celular del usuario."""

    return grafoChat(3, available_functions, lista_de_tools, None, prompt)