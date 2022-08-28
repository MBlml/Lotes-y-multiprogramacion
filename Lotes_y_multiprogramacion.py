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
        self.__value= 100
        

    #getters y setters para manipular atributos
    def setNombre (self, nombre):
        self.__nombre = nombre
        
    def getNombre (self):
        return self.__nombre 

    #el estado del proceso puede servir para multiprogramación
    def setEstado (self, estado):
        self.__estado = estado
        
    def getEstado (self):
        return self.__estado
    
    def getProgressBar (self):
        return self.__progressBar
    

    def setValue (self, value):
        self.__value = value
        
    def getValue (self):
        return self.__value

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
root.title("Multiprogramacion")

#contadores de row para barra de carga y etiquetas de proceso
processRowCounter = 2

etiquetaNombreProceso = ttk.Label(text="Nombre del proceso: ")
etiquetaNombreProceso.grid(column=0, row=0)
entradaProceso = ttk.Entry()
entradaProceso.grid(column=1, row=0, padx=100, pady=10)

#definimos nuestro objeto de lote
lote = Lote()

#Funcion para mandar a imprimir los nombres en espacios de procesos
def mandarDato():
    global processRowCounter
    
    #limitamos los procesos a 15
    if (entradaProceso.get() == "") | (lote.getCantProcesos() >= 15):
        return
    else:
        #Inicializamos el objeto proceso con el constructor
        proceso = Proceso(entradaProceso.get(), "")
        #Renderizamos el proceso en la UI, necesitamos un contador de filas para que se vea bien cada proceso agregado
        proceso.renderizarProceso(root, processRowCounter, processRowCounter)
        #Aumentamos los contadores de fila para la progress bar y la etiqueta
        processRowCounter += 2
        
        #Usando nuestro objeto de la clase lote, agregamos el proceso a la cola
        lote.agregarProceso(proceso)
        #Eliminamos la entrada del usuario para mas comodidad
        entradaProceso.delete(0, len(entradaProceso.get()))

def lotes():
    j = 0
    cant = lote.getCantProcesos()
    #El while externo itera sobre cada proceso de la lista
    while (j < cant):
        i = 0
        actual = lote.getColaProcesos()[0].getProgressBar()
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

def multiprogramacion():
    #Definimos variables
    i=0
    nProceso=0
    tiempoPorProceso=4
    #Iteramos mientras haya elementos en la cola de procesos
    while(len(lote.getColaProcesos())>0):
        #Obtenemos los valores del proceso a ejecutar
        procesoActual= lote.getColaProcesos()[nProceso]
        valorRestante= procesoActual.getValue()
        #Si el proceso aun no de terminar de completar lo 'ejecutamos'
        if(valorRestante>0):
            time.sleep(0.5)
            #Se actualiza el valor restante del proceso y su barra de progreso
            procesoActual.getProgressBar()['value'] += 10
            procesoActual.setValue(valorRestante-10)
            i += 1
            #Se actualiza la pantalla para animación de carga
            root.update_idletasks()
        else:
            #Si el proceso se completa lo sacamos de la cola y continuamos con los siguientes
            lote.getColaProcesos().pop(nProceso)
            i=0
            if(nProceso> lote.getCantProcesos()-1):
                nProceso=0
        #Si el proceso consumio su tiempo en el procesador encontes avanzamos el siguiente proceso
        if(i==tiempoPorProceso):
            i=0
            if(nProceso>= lote.getCantProcesos()-1):
                nProceso=0
            else:
                nProceso+=1

#Boton para la funcion de enviar a imprimir
buttonAgregar = ttk.Button(text="Agregar proceso", command=mandarDato)
buttonAgregar.grid(column=2, row=0)

#Boton para empezar procesamiento por lotes
buttonLotes = ttk.Button(text="Lotes", command=lotes)
buttonLotes.grid(column=3, row=0)

#Boton para empezar procesamiento por lotes
buttonMultiprogramacion = ttk.Button(text="Multiprogramacion", command=multiprogramacion)
buttonMultiprogramacion.grid(column=5, row=0)


root.mainloop()