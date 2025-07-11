import pandas as pd
import pywhatkit
import time
from ventana import obtener_datos_ventana

def enviar_mensajes(archivo_excel, mensaje, hora, minuto):
    df = pd.read_excel(archivo_excel)
    waiting_time_to_send = 30
    close_tab = True
    waiting_time_to_close = 3

    for i in range(len(df)):
        telefono = f"+57{df.loc[i, 'NUMBERS']}"
        nombre = df.loc[i, "NAME"]
        mensaje_final = f"{nombre}, {mensaje}"

        print(f"Enviando a {telefono}: {mensaje_final}")
        pywhatkit.sendwhatmsg(
            telefono,
            mensaje_final,
            hora,
            minuto,
            waiting_time_to_send,
            close_tab,
            waiting_time_to_close
        )

        time.sleep(20)
        minuto += 1
        if minuto >= 60:
            minuto = 0
            hora += 1

if __name__ == "__main__":
    archivo, mensaje, hora, minuto = obtener_datos_ventana()
    if archivo and mensaje and hora is not None and minuto is not None:
        enviar_mensajes(archivo, mensaje, hora, minuto)
    else:
        print("No se ingresaron todos los datos necesarios.")
