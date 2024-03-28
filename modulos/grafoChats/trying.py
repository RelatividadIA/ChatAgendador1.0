from datetime import datetime

# Obtener la hora actual
now = datetime.now()

# Formatear la hora en el formato HH:MM:SS
horaActual = now.strftime('%H-%M-%S')
