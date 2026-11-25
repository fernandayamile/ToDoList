from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):
      
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)
        ###################################################################
        self.lstTareas.itemClicked.connect(self.MostrarTarea)

    #añadir elementos
    #def lista(self):
        #texto = "tarea"
        #self.lstTareas.addItem(texto) 

    #Eliminar un elemento
    #def lista(self):
        #indice = 3
        #self.lstTareas.takeItem(indice)    

    #def lista(self):
        #indice = 3
        #print("La tarea presionada es la que tiene el indice: ", indice)

    #Obtener el valor seleccionado
    #def lista(self):
        #indice = self.lstTareas.currentRow()    
        #print("La tarea presionada es la que tiene el indice: ", indice)

    #Configuración y despliegue
    #def lista(self):
        #indice = self.lstTareas.currentRow()
        #QMessageBox.information(self, "Notificacion", f"La tarea presionada es la que tiene el indice: {indice}")

#Esta        

    def AgregarTarea(self):
        tarea = self.edtTarea.text() 
        ###########################################################################################
        if tarea !="":   
            self.lstTareas.addItem(tarea)
            self.edtTarea.clear()
        else:
            QMessageBox.information(self, "Aviso", "Escribe una tarea antes de agregar")
        ################################################################################################
        #Seleccionar el campo
        self.edtTarea.setFocus()
        #los tacos de pastor aprueban este código
        #TODO AGREGAR VALIDACION DE CAMPO NO VACIO
        
         

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)

    #############################################################################
    def ActualizarTarea(self):
        indice = self.lstTareas.currentRow()  
        nuevoTexto = self.edtTarea.text()   

        if indice != -1:
            if nuevoTexto != "":
                self.lstTareas.takeItem(indice)
                self.lstTareas.addItem(nuevoTexto)
                self.edtTarea.clear()   


    def MostrarTarea(self):
        self.edtTarea.setText(self.lstTareas.currentItem().text())                
    ####################################################################################