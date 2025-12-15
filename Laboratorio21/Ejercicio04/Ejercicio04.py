class Libro:
    
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__disponible = True
        
    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False
        
    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            return True
        return False
        
    def mostrar_datos(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return (
            f"\n--- DATOS LIBRO ---\n"
            f"Titulo: {self.__titulo}\n"
            f"Autor: {self.__autor}\n"
            f"Año: {self.__año}\n"
            f"Estado: {estado}"
        )
    

class LibroDigital(Libro):
    
    def __init__(self, titulo, autor, año, formato, tamaño):
        super().__init__(titulo, autor, año)
        self.__formato = formato
        self.__tamaño = tamaño
        self.__veces_prestado = 0
        
    def prestar(self):
        self.__veces_prestado += 1
        return True
    
    def devolver(self):
        return True
    
    def mostrar_datos(self):
        return (
            super().mostrar_datos() +
            f"\nFormato: {self.__formato}\n"
            f"Tamaño: {self.__tamaño} MB\n"
            f"Veces prestado: {self.__veces_prestado}"
        )
    

class Biblioteca:
    
    def __init__(self):
        self.__lista_libros = {} 
        
    def agregar_libro(self, libro):
        self.__lista_libros[libro.titulo] = libro
        
    def listar_libros(self):
        print("\n--- LISTA DE LIBROS ---")
        for libro in self.__lista_libros.values():
            print(libro.mostrar_datos())
            
    def prestar_libro(self, titulo):
        libro = self.__lista_libros.get(titulo)
        if libro:
            if libro.prestar():
                print(f"Libro '{titulo}' prestado correctamente")
            else:
                print(f"El libro '{titulo}' ya está prestado")
        else:
            print("Libro no encontrado")
        
    def devolver_libro(self, titulo):
        libro = self.__lista_libros.get(titulo)
        if libro and libro.devolver():
            print(f"Libro '{titulo}' devuelto correctamente")
        else:
            print("No se pudo devolver el libro")
            
    def buscar_por_autor(self, autor):
        print(f"\nLibros del autor {autor}:")
        for libro in self.__lista_libros.values():
            if libro.autor.lower() == autor.lower():
                print(libro.mostrar_datos())
biblioteca = Biblioteca()


l1 = Libro("El Quijote", "Cervantes", 1605)
l2 = Libro("Cien años de soledad", "García Márquez", 1967)
l3 = Libro("La ciudad y los perros", "Vargas Llosa", 1963)


d1 = LibroDigital("Python Básico", "Guido", 2020, "PDF", 5)
d2 = LibroDigital("POO en Python", "Guido", 2021, "EPUB", 3)

biblioteca.agregar_libro(l1)
biblioteca.agregar_libro(l2)
biblioteca.agregar_libro(l3)
biblioteca.agregar_libro(d1)
biblioteca.agregar_libro(d2)

biblioteca.listar_libros()
biblioteca.prestar_libro("El Quijote")
biblioteca.prestar_libro("El Quijote")
for _ in range(5):
    biblioteca.prestar_libro("Python Básico")
biblioteca.buscar_por_autor("Guido")