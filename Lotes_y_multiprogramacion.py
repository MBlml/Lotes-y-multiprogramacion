import tkinter as tk
from tkinter import ttk

<<<<<<< Updated upstream
root = tk.Tk()
root.geometry("500x500")
root.title("Lotes y multiprogramacion")

contadorProcesos = 0
=======
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
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
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
    
=======
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

>>>>>>> Stashed changes
#Boton para la funcion de enviar a imprimir
buttonAgregar = ttk.Button(text="Agregar proceso", command=mandarDato1)
buttonAgregar.grid(column=2, row=0)

buttonLotes = ttk.Button(text="Lotes", command=procesoLotes)
buttonLotes.grid(column=2, row=11)

<<<<<<< Updated upstream
buttonMultiprogramacion = ttk.Button(text="Multiprogramacion",command=procesoMultiprogramacion)
buttonMultiprogramacion.grid(column=2, row=13)

buttonCancelar = ttk.Button(text="Cancelar",command=cancelar)
buttonCancelar.grid(column=2, row=14)

root.mainloop()

#Para evitar descargarlo y tardar en abrir en algun dispositivo, tienen la opcion de correr el programa en https://replit.com, se parece a VSCODE
#Faltantes: Funcion para "Lotes" que comience el siguiente proceso al finalizar el anterior, funcionalidad para detener todas las barras al llegar al 100%
# y añadir estilos a la GUI en general para verse mas PRO
#Si tienen duda mandan Whats xD, estare disponible el domingo para seguirle si hay mas cosas por hacer, segun yo solo queda eso jajaja
=======
#Boton para empezar procesamiento por lotes
buttonMultiprogramacion = ttk.Button(text="Multiprogramacion", command=multiprogramacion)
buttonMultiprogramacion.grid(column=5, row=0)


root.mainloop()
>>>>>>> Stashed changes
