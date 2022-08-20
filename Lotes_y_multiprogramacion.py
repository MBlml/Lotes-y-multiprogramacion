import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.title("Lotes y multiprogramacion")

contadorProcesos = 0

etiquetaNombreProceso = ttk.Label(text="Nombre del proceso: ")
etiquetaNombreProceso.grid(column=0, row=0)
entradaProceso = ttk.Entry()
entradaProceso.grid(column=1, row=0)

#Procesos a ejecutar (Numero,nombre y barra de progreso)
etiquetaNombreProcesoActivo1 = ttk.Label(text="Proceso 1: ")
etiquetaNombreProcesoActivo1.grid(column=0, row=1)
procesoActivo1 = ttk.Entry()
procesoActivo1.grid(column=0, row=2)
progressbar1 = ttk.Progressbar(orient=tk.HORIZONTAL, length=200)
progressbar1.grid(column=1, row=2)

etiquetaNombreProcesoActivo2 = ttk.Label(text="Proceso 2: ")
etiquetaNombreProcesoActivo2.grid(column=0, row=3)
procesoActivo2 = ttk.Entry()
procesoActivo2.grid(column=0, row=4)
progressbar2 = ttk.Progressbar(orient=tk.HORIZONTAL, length=200)
progressbar2.grid(column=1, row=4)

etiquetaNombreProcesoActivo3 = ttk.Label(text="Proceso 3: ")
etiquetaNombreProcesoActivo3.grid(column=0, row=5)
procesoActivo3 = ttk.Entry()
procesoActivo3.grid(column=0, row=6)
progressbar3 = ttk.Progressbar(orient=tk.HORIZONTAL, length=200)
progressbar3.grid(column=1, row=6)

etiquetaNombreProcesoActivo4 = ttk.Label(text="Proceso 4: ")
etiquetaNombreProcesoActivo4.grid(column=0, row=7)
procesoActivo4 = ttk.Entry()
procesoActivo4.grid(column=0, row=8)
progressbar4 = ttk.Progressbar(orient=tk.HORIZONTAL, length=200)
progressbar4.grid(column=1, row=8)

etiquetaNombreProcesoActivo5 = ttk.Label(text="Proceso 5: ")
etiquetaNombreProcesoActivo5.grid(column=0, row=9)
procesoActivo5 = ttk.Entry()
procesoActivo5.grid(column=0, row=10)
progressbar5 = ttk.Progressbar(orient=tk.HORIZONTAL, length=200)
progressbar5.grid(column=1, row=10)

#Funcion para mandar a imprimir los nombres en espacios de procesos
def mandarDato1():
    global contadorProcesos
    contadorProcesos += 1
    if (contadorProcesos == 1):
        procesoActivo1.insert(0, entradaProceso.get() + " ")
        print("Proceso almacenado: " + entradaProceso.get())
        
    if (contadorProcesos == 2):
        procesoActivo2.insert(0, entradaProceso.get() + " ")
        print("Proceso almacenado: " + entradaProceso.get())
        
    if (contadorProcesos == 3):
        procesoActivo3.insert(0, entradaProceso.get() + " ")
        print("Proceso almacenado: " + entradaProceso.get())
        
    if (contadorProcesos == 4):
        procesoActivo4.insert(0, entradaProceso.get() + " ")
        print("Proceso almacenado: " + entradaProceso.get())
        
    if (contadorProcesos == 5):
        procesoActivo5.insert(0, entradaProceso.get() + " ")
        print("Proceso almacenado: " + entradaProceso.get())

def procesoLotes():
    for i in range (contadorProcesos+1):
        if i == 1:
            progressbar1.start()
        if i == 2:
            progressbar2.start()
        if i == 3:
            progressbar3.start()
        if i == 4:
            progressbar4.start()
        if i == 5:
            progressbar5.start()
        i += 1
        #Aqui agregar la funcion para que comience uno al finalizar el anterior
        #Agregar funcionalidad para detener todas las barras al llegar al 100%

def procesoMultiprogramacion():
    for i in range (contadorProcesos+1):
        if i == 1:
            progressbar1.start(100)
        if i == 2:
            progressbar2.start(90)
        if i == 3:
            progressbar3.start(110)
        if i == 4:
            progressbar4.start(95)
        if i == 5:
            progressbar5.start(105)
        i += 1
    #Agregar funcionalidad para detener todas las barras al llegar al 100%

def cancelar():
    progressbar1.stop()
    progressbar2.stop()
    progressbar3.stop()
    progressbar4.stop()
    progressbar5.stop()
    print("Procesos cancelados")
    
#Boton para la funcion de enviar a imprimir
buttonAgregar = ttk.Button(text="Agregar proceso", command=mandarDato1)
buttonAgregar.grid(column=2, row=0)

buttonLotes = ttk.Button(text="Lotes", command=procesoLotes)
buttonLotes.grid(column=2, row=11)

buttonMultiprogramacion = ttk.Button(text="Multiprogramacion",command=procesoMultiprogramacion)
buttonMultiprogramacion.grid(column=2, row=13)

buttonCancelar = ttk.Button(text="Cancelar",command=cancelar)
buttonCancelar.grid(column=2, row=14)

root.mainloop()

#Para evitar descargarlo y tardar en abrir en algun dispositivo, tienen la opcion de correr el programa en https://replit.com, se parece a VSCODE
#Faltantes: Funcion para "Lotes" que comience el siguiente proceso al finalizar el anterior, funcionalidad para detener todas las barras al llegar al 100%
# y añadir estilos a la GUI en general para verse mas PRO
#Si tienen duda mandan Whats xD, estare disponible el domingo para seguirle si hay mas cosas por hacer, segun yo solo queda eso jajaja
