# Cronómetro con customtkinter
import customtkinter as ctk

# Crear la ventana principal
ventana = ctk.CTk()
ventana.geometry("300x200")
ventana.title("Cronómetro")

# Crear una etiqueta para mostrar el tiempo
tiempo_label = ctk.CTkLabel(ventana, text="00:00:00", font=("Helvetica", 48))
tiempo_label.pack(pady=20)

# Variables para el cronómetro
segundos = 0
ejecutando = False

def actualizar_tiempo():
    global segundos
    if ejecutando:
        segundos += 1
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segs = segundos % 60
        tiempo_label.configure(text=f"{horas:02}:{minutos:02}:{segs:02}")
        ventana.after(1000, actualizar_tiempo)

def iniciar():
    global ejecutando
    if not ejecutando:
        ejecutando = True
        actualizar_tiempo()

def detener():
    global ejecutando
    if ejecutando:
        ejecutando = False

def reiniciar():
    global segundos
    segundos = 0
    tiempo_label.configure(text="00:00:00")
    detener()

# Botón de iniciar
iniciar_boton = ctk.CTkButton(ventana, text="Iniciar", command=iniciar)
iniciar_boton.pack(side=ctk.LEFT, padx=20)

# Botón de detener
detener_boton = ctk.CTkButton(ventana, text="Detener", command=detener)
detener_boton.pack(side=ctk.LEFT, padx=20)

# Botón de reiniciar
reiniciar_boton = ctk.CTkButton(ventana, text="Reiniciar", command=reiniciar)
reiniciar_boton.pack(side=ctk.LEFT, padx=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()