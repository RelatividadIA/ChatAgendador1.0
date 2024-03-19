import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerEmail(email):
    """Extrae los email y lo coloca en el formato json estandar"""
    if controller.verificarExistencia(json.dumps({"email": email})):
        pass
    else:
        print("No está en la base de datos")
        #idActual.global_id = 6
    

    return json.dumps({"email": email})

def getGrafoChatID5():
    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerEmail",
                "description": "Esta función extrae el email del usuario en un string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "email del usuario."
                        },
                    },
                    "required": ["email"]
                }
            }
        }
        ]

    available_functions = {
                "extraerEmail":extraerEmail
            }

    prompt = """Eres un bot que ayuda en el proceso de agendamiento de citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Tu único trabajo es preguntar al usuario cual es su email. (e.g. 'Ayúdame con tus email por favor.' o 'Ahora indícame tu correo electrónico por favor')
    2. Debes verificar con cuidado si el usuario responde efectivmente a esta ultima pregunta, o si por otro lado, parece que se ha desviado en la conversación.
    3. Si el usuario se desvía en la conversación debes insistir en preguntarle cual es su email (o correo electrónico). 
    4. Una vez que el usuario ha proporcionado su email llamas a la función extraerEmail, lo cual hará que la conversación continue con el siguiente bot que le preguntará el día que desea agendar su cita.
    """
    return grafoChat(5, available_functions, lista_de_tools, None, prompt)