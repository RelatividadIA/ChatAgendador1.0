import modulos.idActual as idActual
import modulos.dataBase.controller as controller

from modulos.grafoChats.grafoChat import *

def extraerEmail(email):
    """Extrae los email y lo coloca en el formato json estandar"""
    if idActual.global_redirrecion:
        controller.actualizar_cliente(json.dumps({"email": email}))
        idActual.resetRedirreccion()
    else:
        controller.actualizar_cliente(json.dumps({"email": email}))
        idActual.global_id = 6

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
    2. Debes verificar con cuidado si el usuario responde efectivamente a esta ultima pregunta, o si por otro lado, parece que se ha desviado en la conversación.
    3. Bajo ninguna situación el email son solo números o palabras sin un dominio, para ayudarte a identificar su email, recuerda que cada email tiene un '@' en el.
    4. Si el usuario se desvía en la conversación debes insistir en preguntarle cual es su email (o correo electrónico). 
    5. Una vez que el usuario ha proporcionado su email llamas a la función extraerEmail, lo cual hará que la conversación continue con el siguiente bot que le preguntará el día que desea agendar su cita.
    6. En caso de que retomes la conversación, pregunta nuevamente por el email del usuario y asegúrate de llamar a la función para reservar la nueva información.
    """
    return grafoChat(5, available_functions, lista_de_tools, None, prompt)