import tkinter as tk
from tkinter import simpledialog, filedialog

def obtener_datos_ventana():
    ventana = tk.Tk()
    ventana.withdraw()  # Oculta la ventana principal

    archivo = filedialog.askopenfilename(
        title="Selecciona archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )

    mensaje = simpledialog.askstring("Mensaje", "Escribe el mensaje a enviar")
    hora = simpledialog.askinteger("Hora", "¿A qué hora enviar? (24h)")
    minuto = simpledialog.askinteger("Minuto", "¿En qué minuto enviar?")

    return archivo, mensaje, hora, minuto
 