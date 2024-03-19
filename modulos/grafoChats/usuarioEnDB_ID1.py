import modulos.idActual as idActual
import openai

from modulos.grafoChats.grafoChat import *

def determinarBoolRespuestaDelUsuario(respuesta):
    """Extrae el mensaje del usuario y determina su carácter booleano."""
    print(respuesta+respuesta+respuesta+respuesta+respuesta)
    if (respuesta == False):
        idActual.global_id = 2
    
    return "True"





def getGrafoChatID1():

    lista_de_tools = [
    {
        
        "type": "function",
        "function": {
            "name": "determinarBoolRespuestaDelUsuario",
            "description": "Esta función extrae un boolean que indica si el usuario ya ha agendado una cita por este medio de mensajería. La función recibe True si el usuario ya ha agendado una cita por este medio de mensajería. Si el usuario no ha utilizado este medio para agendar una cita la función recibe el parámetro False.",
            "parameters": {
                "type": "object",
                "properties": {
                    "respuesta": {
                        "type": "boolean",
                        "description": "Debe ser True si el usuario ha utilizado antes este medio para agendar una cita. Debe ser False si el usuario no ha utilizado antes este medio para agendar una cita."
                    }
                },
                "required": ["respuesta"]
            }
        }
    }
    ]

    available_functions = {
                "determinarBoolRespuestaDelUsuario":determinarBoolRespuestaDelUsuario
            }

    prompt = """Eres un bot que agenda citas por una aplicación de chats. Eres muy amable y eres experto en atención al cliente.
    1. Tu único trabajo es saludar al usuario diciendo "Hola, soy Jarvis y te ayudaré agendando tu cita.". Y luego preguntarle si ya ha usado este medio de mensajería para agendar una cita antes. 
    2. El usuario básicamente debe responderte que sí o que no, o alguna cosa equivalente como "no todavía", "nunca", "por supuesto", "claro", "aun no", "ya lo he hecho", etc.
    3. Si el usuario se desvía en la conversación en lugar de responder (esto es algo que rara vez ocurrirá), debes insistir con mucha amabilidad en preguntarle si ha agendado una cita por este medio de mensajería hasta que el usuario responda. 
    4. Una vez que el usuario ha respondido a la pregunta y sepas si ya ha agendado una cita por este medio de mensajería antes o si no lo ha hecho, llamas a la función determinarBoolRespuestaDelUsuario que hará que la conversación contigo termine y pase al siguiente bot.
    """


    return grafoChat(1, available_functions, lista_de_tools, None, prompt)

