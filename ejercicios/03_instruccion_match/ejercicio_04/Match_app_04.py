import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre : Patricio Joaquin
Apellido : Guede

Enuciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si tiene 28 días
    Si tiene 30 días
    Si tiene 31 días
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        meses = self.combobox_mes.get()
        
        match meses :
            case "Enero" : 
                mensaje = "Tiene 31 días"
            case "Febrero" : 
                mensaje = "Tiene 28 días"
            case "Marzo" : 
                mensaje = "Tiene 31 días"
            case "Abril" : 
                mensaje = "Tiene 30 días"
            case "Mayo" : 
                mensaje = "Tiene 31 días"
            case "Junio" : 
                mensaje = "Tiene 30 días"
            case "Julio" : 
                mensaje = "Tiene 31 días"
            case "Agosto" : 
                mensaje = "Tiene 31 días"
            case "Septiembre" : 
                mensaje = "Tiene 30 días"
            case "Octubre" : 
                mensaje = "Tiene 31 días"
            case "Noviembre" : 
                mensaje = "Tiene 30 días"
            case "Diciembre" : 
                mensaje = "Tiene 31 días"
                
        alert("EJ04", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()