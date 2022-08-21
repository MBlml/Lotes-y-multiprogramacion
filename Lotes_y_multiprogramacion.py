import tkinter as tk
from tkinter import ttk
import time

class Proceso:
    #se definen los atributos privados de cada proceso en constructor
    #definimos el contructor de la clase
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado
        self.__progressBar = any 
        

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
    
    #métodos para manipular la barra de carga de cada proceso
    #los parametros con row solo son contadores para desplazar la fila con cada proceso agregado
    def renderizarProceso (self, container, barRow, labelRow):
        var = tk.IntVar()
        var.set(0)
        etiquetaNombreProceso = ttk.Label(text=self.getNombre())
        etiquetaNombreProceso.grid(column=0, row=labelRow)
        self.__progressBar = ttk.Progressbar(container, variable = var, orient = tk.HORIZONTAL, length=300)
        self.__progressBar.grid(column=1, row=barRow, pady=10)
        
            
class Lote:
    
    #se define la cola de procesos por lote    
    def __init__ (self):
        self.__contadorProcesos = 0
        self.__cola_procesos = []
    
    #Aqui se agrega un proceso a la cola
    def agregarProceso (self, proceso):
        self.__cola_procesos.append(proceso)
        self.__contadorProcesos += 1
    
    #Getter de queue de procesos
    def getColaProcesos(self):
        return self.__cola_procesos
    
    def getCantProcesos(self):
        return self.__contadorProcesos
    
    #metodo que hace pop a la lista
    def pop(self):
        self.__cola_procesos.pop(0)
        self.__contadorProcesos -= 1
            

                
root = tk.Tk()
root.geometry("750x700")
root.title("Lotes y Multiprogramacion")

#contadores de row para barra de carga y etiquetas de proceso
barRowCounter = 2
labelRowCounter = 2

etiquetaNombreProceso = ttk.Label(text="Nombre del proceso: ")
etiquetaNombreProceso.grid(column=0, row=0)
entradaProceso = ttk.Entry()
entradaProceso.grid(column=1, row=0, padx=100, pady=10)

#definimos nuestro objeto de lote
lote = Lote()

#Funcion para mandar a imprimir los nombres en espacios de procesos
def mandarDato():
    global barRowCounter
    global labelRowCounter
    
    #limitamos los procesos a 15
    if (entradaProceso.get() == "") | (lote.getCantProcesos() == 15):
        return
    else:
        #Inicializamos el objeto proceso con el constructor
        proceso = Proceso(entradaProceso.get(), "")
        #Renderizamos el proceso en la UI, necesitamos un contador de filas para que se vea bien cada proceso agregado
        proceso.renderizarProceso(root, barRowCounter, labelRowCounter)
        #Aumentamos los contadores de fila para la progress bar y la etiqueta
        labelRowCounter += 2
        barRowCounter += 2
        
        #Usando nuestro objeto de la clase lote, agregamos el proceso a la cola
        lote.agregarProceso(proceso.getProgressBar())
        #Eliminamos la entrada del usuario para mas comodidad
        entradaProceso.delete(0, len(entradaProceso.get()))

def lotes():
    j = 0
    cant = lote.getCantProcesos()
    #El while externo itera sobre cada proceso de la lista
    while (j < cant):
        i = 0
        actual = lote.getColaProcesos()[0]
        #el while interno sirve para rellenar las barras de cada proceso
        while (i < 10):
            time.sleep(0.5)
            #'value' es un atributo del objeto de ProgressBar que nos permite manipular el avance
            actual['value'] += 10
            i += 1
            #Se actualiza la pantalla para animación de carga
            root.update_idletasks()
        j += 1
        lote.pop()
        

def procesoMultiprogramacion():
    pass
    # for i in range (contadorProcesos+1):
    #     if i == 1:
    #         progressbar1.start(100)
    #     if i == 2:
    #         progressbar2.start(90)
    #     if i == 3:
    #         progressbar3.start(110)
    #     if i == 4:
    #         progressbar4.start(95)
    #     if i == 5:
    #         progressbar5.start(105)
    #     i += 1
    #Agregar funcionalidad para detener todas las barras al llegar al 100%

def cancelar():
    pass
#     progressbar1.stop()
#     progressbar2.stop()
#     progressbar3.stop()
#     progressbar4.stop()
#     progressbar5.stop()
#     print("Procesos cancelados")

#Boton para la funcion de enviar a imprimir
buttonAgregar = ttk.Button(text="Agregar proceso", command=mandarDato)
buttonAgregar.grid(column=2, row=0)

#Boton para empezar procesamiento por lotes
buttonLotes = ttk.Button(text="Lotes", command=lotes)
buttonLotes.grid(column=3, row=0)

# buttonMultiprogramacion = ttk.Button(text="Multiprogramacion",command=procesoMultiprogramacion)
# buttonMultiprogramacion.grid(column=4, row=0)

# buttonCancelar = ttk.Button(text="Cancelar",command=cancelar)
# buttonCancelar.grid(column=3, row=1)


root.mainloop()

#Para evitar descargarlo y tardar en abrir en algun dispositivo, tienen la opcion de correr el programa en https://replit.com, se parece a VSCODE
#Faltantes: Funcion para "Lotes" que comience el siguiente proceso al finalizar el anterior, funcionalidad para detener todas las barras al llegar al 100%
# y añadir estilos a la GUI en general para verse mas PRO
#Si tienen duda mandan Whats xD, estare disponible el domingo para seguirle si hay mas cosas por hacer, segun yo solo queda eso jajaja
