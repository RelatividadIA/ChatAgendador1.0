import os.path
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def getCreds():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        return creds
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open("token.json", "w") as token:
            token.write(creds.to_json())
            return creds

def consultarDisponibilidad(fechaInicial, duracionEnHoras):
    creds = getCreds()
    try:
        service = build("calendar", "v3", credentials=creds)
        
        #A la fecha asignarle una hora
        

        pass
    except:
        pass

def crearEvento(titulo, descripcion, fechaHoraInicial, duracionEnHoras=1):
    creds = getCreds()
    try:
        service = build("calendar", "v3", credentials=creds)

        #Programar la duración de un evento, por defecto una hora
        time = datetime.fromisoformat(fechaHoraInicial)
        fechaHoraFinal = (time + timedelta(hours=duracionEnHoras)).isoformat()

        event = {
            "summary": titulo,
            "description":descripcion,
            "colorId": 5,
            "start": {
                "dateTime": fechaHoraInicial,
                "timeZone": "America/Guayaquil"
            },
            "end": {
                "dateTime": fechaHoraFinal,
                "timeZone": "America/Guayaquil"
            },
        }

        """
        Ejemplo de sintáxis de un evento

        event = {
            "summary": "Título del evento",
            "description": "descripción",
            "colorId": 5,
            "start": {
                "dateTime": "2024-03-27T21:10:51",
                "timeZone": "America/Guayaquil"
            },
            "end": {
                "dateTime": "2024-03-27T23:10:51",
                "timeZone": "America/Guayaquil"
            },
        }
        """
        
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Evento creado {event.get('htmlLink')}")

    except HttpError as error:
        print("Se ha dado un error:", error)

if __name__ == "__main__":
    #crearEvento("a", "b", "c")
    pass