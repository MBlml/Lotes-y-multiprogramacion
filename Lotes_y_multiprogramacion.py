import tkinter as tk
from tkinter import ttk
from threading import Thread
from queue import Queue
class Proceso:
    #se definen los atributos privados de cada proceso
    __nombre = ""
    __estado = ""
    __progressBar = any
    
    #definimos el contructor de la clase
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado
        

    #getters y setters para manipular atributos
    def setNombre (self, nombre):
        self.__nombre = nombre
        
    def getNombre (self):
        return self.__nombre 

    def setEstado (self, estado):
        self.__estado = estado
        
    def getEstado (self):
        return self.__estado
    
    def getProgressBar (self):
        return self.__progressBar
    
    def iniciarProceso ():
        pass
    
    #métodos para manipular la barra de carga de cada proceso
    #los parametros con row solo son contadores para desplazar la fila con cada proceso agregado
    def renderizarProceso (self, container, barRow, labelRow):
        var = tk.IntVar()
        var.set(0)
        etiquetaNombreProceso = ttk.Label(text=self.getNombre())
        etiquetaNombreProceso.grid(column=0, row=labelRow)
        self.__progressBar = ttk.Progressbar(container, variable = var, orient = tk.HORIZONTAL, length=300)
        self.__progressBar.grid(column=1, row=barRow)

    def iniciarProceso ():
        pass

class Lote:
    
    __cola_procesos = Queue(maxsize = 15)
    
    def agregarProceso (self, proceso):
        self.__cola_procesos.put(proceso)
        print(self.__cola_procesos)
        
    def getColaProcesos(self):
        return self.__cola_procesos


root = tk.Tk()
root.geometry("750x700")
root.title("Lotes y Multiprogramacion")

contadorProcesos = 0
barRowCounter = 2
labelRowCounter = 2

etiquetaNombreProceso = ttk.Label(text="Nombre del proceso: ")
etiquetaNombreProceso.grid(column=0, row=0)
entradaProceso = ttk.Entry()
entradaProceso.grid(column=1, row=0)

#definimos nuestro objeto de lote
lote = Lote()

#Funcion para mandar a imprimir los nombres en espacios de procesos
def mandarDato():
    global barRowCounter
    global labelRowCounter
    global inputRowCounter
    global contadorProcesos
    
    if (entradaProceso.get() == "") | (lote.getColaProcesos().full()):
        return
    else:
        proceso = Proceso(entradaProceso.get(), "")
        proceso.renderizarProceso(root, barRowCounter, labelRowCounter)
        
        labelRowCounter += 2
        barRowCounter += 2
        
        lote.agregarProceso(proceso)
        # print(barRowCounter)
    # if (contadorProcesos == 1):
    #     procesoActivo1.insert(0, entradaProceso.get() + " ")
    #     print("Proceso almacenado: " + entradaProceso.get())
        
    # if (contadorProcesos == 2):
    #     procesoActivo2.insert(0, entradaProceso.get() + " ")
    #     print("Proceso almacenado: " + entradaProceso.get())
        
    # if (contadorProcesos == 3):
    #     procesoActivo3.insert(0, entradaProceso.get() + " ")
    #     print("Proceso almacenado: " + entradaProceso.get())
        
    # if (contadorProcesos == 4):
    #     procesoActivo4.insert(0, entradaProceso.get() + " ")
    #     print("Proceso almacenado: " + entradaProceso.get())
        
    # if (contadorProcesos == 5):
    #     procesoActivo5.insert(0, entradaProceso.get() + " ")
    #     print("Proceso almacenado: " + entradaProceso.get())

def procesoLotes():
    actual = lote.getColaProcesos().get()
    print(actual.getProgressBar().start())
    pass
    # for i in range (contadorProcesos+1):
    #     if i == 1:
    #         progressbar1.start()
    #     if i == 2:
    #         progressbar2.start()
    #     if i == 3:
    #         progressbar3.start()
    #     if i == 4:
    #         progressbar4.start()
    #     if i == 5:
    #         progressbar5.start()
    #     i += 1
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
buttonAgregar = ttk.Button(text="Agregar proceso", command=mandarDato)
buttonAgregar.grid(column=2, row=0)

buttonLotes = ttk.Button(text="Lotes", command=procesoLotes)
buttonLotes.grid(column=3, row=0)

buttonMultiprogramacion = ttk.Button(text="Multiprogramacion",command=procesoMultiprogramacion)
buttonMultiprogramacion.grid(column=4, row=0)

# buttonCancelar = ttk.Button(text="Cancelar",command=cancelar)
# buttonCancelar.grid(column=3, row=1)





root.mainloop()

#Para evitar descargarlo y tardar en abrir en algun dispositivo, tienen la opcion de correr el programa en https://replit.com, se parece a VSCODE
#Faltantes: Funcion para "Lotes" que comience el siguiente proceso al finalizar el anterior, funcionalidad para detener todas las barras al llegar al 100%
# y añadir estilos a la GUI en general para verse mas PRO
#Si tienen duda mandan Whats xD, estare disponible el domingo para seguirle si hay mas cosas por hacer, segun yo solo queda eso jajaja
