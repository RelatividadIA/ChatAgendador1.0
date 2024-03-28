import modulos.idActual as idActual
import modulos.dataBase.controller as controller
import modulos.dataBase.identificadorDB 

import datetime

from modulos.grafoChats.grafoChat import *

def extraerFecha(fecha):
    """Extrae la fecha en el formato YYYY-MM-DD"""
    modulos.dataBase.identificadorDB.fecha = fecha
    idActual.global_id = 11
    return fecha


def getGrafoChatID9():

    fecha_actual = datetime.date.today()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d')

    dia_semana_numero = fecha_actual.weekday()

    # Mapeo de número a nombre del día en español
    dias_espanol = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    lista_de_tools = [
        {
            
            "type": "function",
            "function": {
                "name": "extraerFecha",
                "description": "Esta función extrae la fecha en la que el usuario desea agendar una cita.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fecha": {
                            "type": "string",
                            "description": "fecha en la que en el usuario desea agendar una cita el formato YYYY-MM-DD"
                        },
                    },
                    "required": ["fecha"]
                }
            }
        }
        ]

    available_functions = {
                "extraerFecha":extraerFecha
            }

    prompt = f"""Eres un bot programado para asistir en el proceso de agendar citas a través de una aplicación de mensajería. Tu trato es amable y te especializas en la atención al cliente. Tus responsabilidades incluyen:

        Importante, si al leer la conversación notas que el usuario menciona que ya ha usado este servicio, le vas a decir que es un placer volver a darle una experiencia de calidad y mencionarás su nombre {controller.obtener_valor_cliente('nombres')} (e.g. David! Es un placer volver a darte una experiencia de calidad)

        1. Tu ÚNICO trabajo es preguntar al usuario por la fecha específica (e.g. 'Ayúdame con la fecha para tu cita por favor.') en que desea agendar una cita, asegurándote de entender tanto fechas explícitas (como '2024-04-15') como relativas ('el miércoles', 'el siguiente viernes', 'pasado mañana').
        2. Si el usuario proporciona una fecha relativa, utiliza la fecha y el día de la semana actual como referencia para calcular la fecha exacta. Por ejemplo, si hoy es {fecha_formateada} y el usuario dice 'el próximo viernes', debes ser capaz de determinar la fecha exacta a la que se refiere.
        3. Verifica cuidadosamente si el usuario ha respondido a tu pregunta sobre la fecha de la cita. Si la conversación se desvía, gentilmente redirígela hacia la programación de la cita.
        4. Una vez obtenida la fecha, sea directa o calculada a partir de una referencia relativa, llama a la función extraerFecha.
        5. Ten en cuenta que la fecha actual es {fecha_formateada}, que corresponde a un {dias_espanol[dia_semana_numero]}. Utiliza esta información para interpretar correctamente referencias temporales como 'mañana', 'el próximo lunes', etc.
        6. La conversación debe ser lo más humana posible, no le digas al usuario cuál es el formato de las fechas.
        7. Si el usario proveé una fecha que ya ha pasado, infórmaselo y vuelve a pedirle amablemente una fecha para su cita.

    Recuerda, tu objetivo es facilitar el proceso de agendamiento siendo preciso y atento a las necesidades de tiempo del usuario."""
    
    return grafoChat(9, available_functions, lista_de_tools, None, prompt, True)