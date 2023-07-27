'''
Nombre : Patricio Joaquin
Apellido : Guede

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = False
        mas_votos = None
        nombre_mas_votos = ""
        edad_menos_votos = ""
        menos_votos = None
        nombre_menos_votos = ""
        total_votos = 0
        sumatoria_de_edades = 0
        contador = 0
        while flag == False :
            nombre = prompt(title = "TP06", prompt = "Ingrese un candidato")
            while nombre == None or not nombre.isalpha():
                nombre = prompt(title = "ERROR", prompt = "Reingrese un nombre valido")
                
            edad = prompt(title = "TP06", prompt = "Ingrese la edad")
            while int(edad) < 26 or edad == None or not edad.isdigit():
                edad = prompt(title = "ERROR", prompt = "Reingrese una edad valida")   
            edad = int(edad)
            
            votos = prompt(title = "TP06", prompt = "Ingrese la cantidad de votos")
            while int(votos) < 0 or votos == None or not votos.isdigit():
                votos = prompt(title = "ERROR", prompt = "Reingrese una cantidad valida")
            votos = int(votos)
                
            if  mas_votos == None or votos > mas_votos :
                mas_votos = votos
                nombre_mas_votos = nombre
            
            if menos_votos == None or votos < menos_votos :
                menos_votos = votos 
                nombre_menos_votos = nombre
                edad_menos_votos = edad
            
            sumatoria_de_edades += edad
            contador += 1
            
            total_votos += votos
            
            continuar = question ("TP06", "Desea continuar?")
            if continuar == False :
                flag = True
        promedio = sumatoria_de_edades/contador

        print (f"El candidato con mas votos es {nombre_mas_votos} \nEl candidato con menos votos es {nombre_menos_votos}, su edad es de {edad_menos_votos} \nEl promedio de las edades es de {promedio} \nY la suma total de votos fue de {total_votos}") 
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
