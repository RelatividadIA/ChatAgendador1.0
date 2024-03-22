global_id = None
global_idPrevio = None
global_redirrecion = False

global_msgs = []

def resetRedirreccion():
    global global_id
    global global_redirrecion
    global global_idPrevio

    global_id = global_idPrevio
    global_idPrevio = None
    global_redirrecion = False
