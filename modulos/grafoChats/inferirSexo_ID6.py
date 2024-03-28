import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerSexo(sexo):
    """Lee toda la conversación, infiere el sexo del usuario y lo coloca en formato json estándar"""
    
    controller.actualizar_cliente(json.dumps({"sexo": sexo}))
    idActual.global_id = 9
    
    return json.dumps({"sexo": sexo})

def getGrafoChatID6():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerSexo",
                "description": "Extrae el sexo del usuario cuando lee la conversación y pasa la conversación al siguiente bot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sexo": {
                            "type": "string",
                            "description": "Sexo de la persona, debe ser o masculino o femenino."
                        },
                    },
                    "required": ["sexo"]
                }
            }
        }
        ]

    available_functions = {
                "extraerSexo":extraerSexo
            }

    prompt = """Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Tu único trabajo es recibir una conversación y siempre llamar a la función extraerSexo determinando el sexo del usuario. 
    2. Una vez que se haya determinado el sexo del usuario, se pasará la conversación a otro bot
    """
    return grafoChat(6, available_functions, lista_de_tools, None, prompt)