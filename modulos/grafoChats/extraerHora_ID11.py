import modulos.idActual as idActual
import modulos.dataBase.controller as controller
import modulos.dataBase.identificadorDB as identificadorDB
import modulos.googleCalendar.googleCalendar as googleCalendar
import datetime

from modulos.grafoChats.grafoChat import *

def extraerHora(hora):
    """Extrae la hora en el formato HH:MM:SS"""
    try:
        identificadorDB.hora = hora
        googleCalendar.crearEvento(f"Cita con {controller.obtener_valor_cliente('nombres')}", "Esto es una cita", f"{identificadorDB.fecha}T{identificadorDB.hora}")
    except:
        print("Hora inválida")
    return hora


def getGrafoChatID11():

    # Obtener la hora actual
    now = datetime.datetime.now()
    
    # Formatear la hora en el formato HH:MM:SS
    horaActual = now.strftime('%H:%M:%S')

    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerHora",
                "description": "Esta función extrae la Hora en la que el usuario desea agendar una cita.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hora": {
                            "type": "string",
                            "description": "Hora en la que en el usuario desea agendar una cita el formato HH:MM:SS"
                        },
                    },
                    "required": ["hora"]
                }
            }
        }
        ]

    available_functions = {
                "extraerHora":extraerHora
            }

    prompt = f"""Eres un bot programado para asistir en el proceso de agendar citas a través de una aplicación de mensajería. Tu trato es amable y te especializas en la atención al cliente. Tus responsabilidades incluyen:

        1. Tu ÚNICO trabajo es preguntar al usuario por la hora específica (e.g. 'Ayúdame con la hora para tu cita por favor.') en que desea agendar una cita, asegurándote de entender tanto horas explícitas (como '13:20:00') como relativas ('a la tres de la tarde', 'en tres horas', 'a la misma hora que ahora').
        2. Si el usuario proporciona una hora relativa, utiliza la hora actual como referencia para calcular la hora exacta. Por ejemplo, si ahora es {horaActual} y el usuario dice 'en tres horas', debes ser capaz de determinar la hora exacta a la que se refiere.
        3. Verifica cuidadosamente si el usuario ha respondido a tu pregunta sobre la fecha de la cita. Si la conversación se desvía, gentilmente redirígela hacia la programación de la cita.
        4. Una vez obtenida la hora, sea directa o calculada a partir de una referencia relativa, llama a la función extraerHora.
        5. Ten en cuenta que la hora actual es {horaActual}.
        6. La conversación debe ser lo más humana posible, no le digas al usuario cuál es el formato de las horas.

    Recuerda, tu objetivo es facilitar el proceso de agendamiento siendo preciso y atento a las necesidades de tiempo del usuario."""
    
    return grafoChat(11, available_functions, lista_de_tools, None, prompt, True)