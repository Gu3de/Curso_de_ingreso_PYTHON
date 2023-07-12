import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Patricio Joaquin
Apellido: Guede
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
    
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        Numero_uno = int(self.txt_importe_1.get())
        numero_dos = int(self.txt_importe_2.get())
        numero_tres = int(self.txt_importe_3.get())
        
        suma = Numero_uno + numero_dos + numero_tres
        
        alert(title = "Suma de los productos", message = suma)
    

    def btn_promedio_on_click(self):
        Numero_uno = int(self.txt_importe_1.get())
        numero_dos = int(self.txt_importe_2.get())
        numero_tres = int(self.txt_importe_3.get())
        
        suma = Numero_uno + numero_dos + numero_tres
        
        promedio = suma/ 3
        
        alert (title = "Promedio de los productos", message = promedio)

    def btn_total_iva_on_click(self):
        Numero_uno = int(self.txt_importe_1.get())
        numero_dos = int(self.txt_importe_2.get())
        numero_tres = int(self.txt_importe_3.get())
        
        suma = Numero_uno + numero_dos + numero_tres
        
        aumento = suma * 21/100
        
        iva = suma + aumento
        
        alert (title = "Total con iva", message = iva)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()