import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre : Patricio Joaquin
Apellido : Guede
entregado
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cantidad_par = 0
        numero = prompt(title = "EJ06", prompt = "Ingrese un numero")
        for i in range (1, int(numero) + 1) :
            if int(i) % 2 == 0 :
                cantidad_par += 1
                alert (title = "Ej 06", message = i)
        alert (title = "EJ06", message = f"los numeros pares son {cantidad_par}")
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()