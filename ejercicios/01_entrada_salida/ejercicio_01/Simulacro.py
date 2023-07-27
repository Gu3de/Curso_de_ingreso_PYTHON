import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre : Patricio Joaquin
Apellido : Guede

A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []


    def btn_cargar_on_click(self):
        for i in range (1,11,1):
            nombre = prompt("UTN", "Ingrese el nombre del pokemon")
            
            elemento = prompt("UTN", "Ingrese su elemento")
            while elemento != "Agua" and elemento != "Tierra" and elemento != "Psiquico" and elemento != "Fuego" and elemento != "Electrico":
                elemento = prompt("Error", "Reingrese un elemento valido")
                
            poder = prompt("UTN", "Ingrese el poder")
            while int(poder) < 49 or int(poder) > 201 :
                poder = prompt("Error", "Reingrese un poder valido")
            
            self.lista_nombre.append(nombre)
            self.lista_tipo.append(elemento)
            self.lista_poder.append(poder)
            
    def btn_mostrar_on_click(self):
        largo = len(self.lista_poder)
        tipo = self.lista_tipo
        poder_maximo = 0
        nombre_maximo_poder = ""
        tipo_maximo_poder = ""
        
        for i in range(largo) :
            match tipo [i]:
                case "Fuego" | "Agua":
                        if poder_maximo == 0 or poder_maximo < self.lista_poder[i] :
                            poder_maximo = self.lista_poder[i]
                            nombre_maximo_poder = self.lista_nombre[i]
                            tipo_maximo_poder = self.lista_tipo[i]
                            mensaje = f"El pokemon {tipo_maximo_poder} con mas poder es {nombre_maximo_poder}, y su poder es de {poder_maximo} "
        print (mensaje)
            
    def btn_informar_on_click(self):
        #dni 45304388 #Punto 8 y 1
        contador_electrico = 0
        poder_sumatoria = 0
        cantidad_poder = len(self.lista_poder)
        
        for i in self.lista_poder :
            poder_sumatoria += i
        promedio = poder_sumatoria / cantidad_poder
        alert (title = "Punto 8", message = f"El promedio de todo el poder es de {promedio}")
        for i in self.lista_tipo :
            if i == "Electrico" :
                contador_electrico += 1
        alert (title = "Punto 1", message= f"La cantidad de electricos son {contador_electrico} ")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()