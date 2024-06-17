# Clase base
class Material:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.ano_publicacion}"

# Clase derivada Libro
class Libro(Material):
    def __init__(self, titulo, autor, ano_publicacion, numero_paginas):
        super().__init__(titulo, autor, ano_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Páginas: {self.numero_paginas}"

# Clase derivada Revista
class Revista(Material):
    def __init__(self, titulo, autor, ano_publicacion, numero_edicion):
        super().__init__(titulo, autor, ano_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Edición: {self.numero_edicion}"

# Función principal para demostrar el polimorfismo
def main():
    materiales = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 417),
        Revista("National Geographic", "Varios", 2021, 5),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 1072),
        Revista("Scientific American", "Varios", 2022, 12)
    ]

    for material in materiales:
        print(material.mostrar_info())


   

def pex4():
     main()
    