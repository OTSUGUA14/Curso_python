import json

class Libro:
    def __init__(self,titulo,autor,año_publicacion,unidades):
        
        self.titulo=titulo
        self.autor=autor
        self.año_publicacion=año_publicacion
        self.disponible=True
        self.unidades=unidades



class Biblioteca1():
  
    libros = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967,
        "disponible": True,
        "unidades": 10
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "año_publicacion": 1949,
        "disponible": True,
        "unidades": 8
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año_publicacion": 1605,
        "disponible": True,
        "unidades": 5
    },
    {
        "titulo": "El amor en los tiempos del cólera",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1985,
        "disponible": True,
        "unidades": 7
    },
    {
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "año_publicacion": 1813,
        "disponible": True,
        "unidades": 12
    }
    ]
    
    def mostrar_libros(self,):
        contador=1
        for i in self.libros:
            print(contador, end=": ")
            for j in i:
                
                if j=="disponible":
                    pass
                else:
                    print(j,end=": ")
                    print(i[j] ,end=" ")
                    print("")
            print("")
            contador+=1
        with open("biblio.json", "w") as archivo:
            json.dump(self.libros, archivo, indent=4)


    
    def prestar(self,nombre):
       
            encontro=False
            for libro in self.libros:
                if libro["titulo"].lower()==nombre:
                    encontro=True
                    if libro["unidades"]==0:
                        libro["disponible"]=False
                        print("No hay libros disponibles")
                        
                    else:
                        libro["unidades"]-=1
                        print("Libro entregado con exitos")
            if not encontro:
                print("No se encontro el Titulo del libro ,ingrese un titulo valido")

    def recibir(self,titulo):
        encontro=False  
        for libro in self.libros:
            if libro["titulo"].lower()==titulo:
                encontro=True
                libro["disponible"]=True
                libro["unidades"]+=1
                print("Recibido el libro con exito")
                
        if not encontro:
            print("No se encontro el Titulo del libro ,ingrese un titulo valido")

    
    def arg(self,agre):
        agregar={}
        agregar.update({"titulo":agre.titulo,"autor":agre.autor,"año_publicacion":agre.año_publicacion,"disponible":agre.disponible,"unidades":agre.unidades})
        self.libros.append(agregar)
class Biblioteca2():
  
    libros = [
    {
        "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "año_publicacion": 2001,
        "disponible": True,
        "unidades": 15
    },
    {
        "titulo": "Los pilares de la Tierra",
        "autor": "Ken Follett",
        "año_publicacion": 1989,
        "disponible": True,
        "unidades": 12
    },
    {
        "titulo": "El alquimista",
        "autor": "Paulo Coelho",
        "año_publicacion": 1988,
        "disponible": True,
        "unidades": 18
    },
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año_publicacion": 1997,
        "disponible": True,
        "unidades": 20
    },
    {
        "titulo": "La casa de los espíritus",
        "autor": "Isabel Allende",
        "año_publicacion": 1982,
        "disponible": True,
        "unidades": 10
    }
]

    def mostrar_libros(self,):
        contador=1
        for i in self.libros:
            print(contador, end=": ")
            for j in i:
                
                if j=="disponible":
                    pass
                else:
                    print(j,end=": ")
                    print(i[j] ,end=" ")
                    print("")
            print("")
            contador+=1
        with open("biblio.json", "w") as archivo:
            json.dump(self.libros, archivo, indent=4)

    
    def prestar(self,nombre):
        encontro=False
        for libro in self.libros:
            
            if libro["titulo"].lower()==nombre:
                encontro=True
                if libro["unidades"]==0:
                    libro["disponible"]=False
                    print("No hay libros disponibles")
                    break
                else:
                    libro["unidades"]-=1
                    print("Libro entregado con exitos")
        if not encontro:
            print("No se encontro el Titulo del libro ,ingrese un titulo valido")
    def recibir(self,titulo):
        encontro=False
        for libro in self.libros:
            if libro["titulo"].lower()==titulo:
                encontro=True
                libro["disponible"]=True
                libro["unidades"]+=1
                print("Recibido el libro con exito")
        if not encontro:
            print("No se encontro el Titulo del libro ,ingrese un titulo valido")

    
    def arg(self,agre):
        agregar={}
        agregar.update({"titulo":agre.titulo,"autor":agre.autor,"año_publicacion":agre.año_publicacion,"disponible":agre.disponible,"unidades":agre.unidades})
        self.libros.append(agregar)


def biblio(valor):
    bibio1=Biblioteca1()
    bibio2=Biblioteca2()
    while True:
        print("""
    1-Mostrar lista de libros
    2-Agregar libro
    3-Quitar libro
    4-Salir 
""")
        try:
            opcion=int(input("Ingrese la opcion que desee: "))

        except :
            print("Debes ingresar un número")
        else:
            if opcion==1:
                if valor==1:
                    
                    bibio1.mostrar_libros()
                elif valor==2:
                    bibio2.mostrar_libros()

            elif opcion==2:
                titulo=input("ingrese el titulo del libro: ")
                autor=input("ingrese el autor del libro: ")
                año_publicacion=input("ingrese el año de publicacion del libro: ")
                unidades=input("ingrese las unidades del libro: ")
                libro=Libro(titulo,autor,año_publicacion,unidades)
                if valor==1:
                    bibio1.arg(libro)
                elif valor==2:
                    bibio2.arg(libro)
            elif opcion==3:
                if valor==1:
                    bibio1.mostrar_libros()
                    li=input("Ingrese el libro que se quiere llevar segun su Titulo: ").lower()
                    bibio1.prestar(li)
                
                elif valor==2:
                    bibio2.mostrar_libros()
                    li=input("Ingrese el libro que se quiere llevar segun su Titulo: ").lower()
                    bibio1.prestar(li)
            elif opcion==4:
                break
                    


while True:
    print("""
    CON QUE BIBLIOTECA QUIERE TRABAJAR?
    1-BIBLIOTECA OTSU
    2-BIBLIOTECA GUA
    3-TERMINAR 
          """)
    while True:
        try:
            opcion=int(input("Ingrese con que biblioteca quiere trabajar segun el número: "))

        except :
            print("Debes ingresar un número")
        else:
                if opcion==1:
                    biblio(opcion)
                elif opcion==2:
                    biblio(opcion)
                elif opcion==3:
                    print("ADIOS")
                    break
                else:
                    print("Numero ingresado no valido")



