# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Método que será sobrescrito por clases derivadas

# Definición de la clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hacer_sonido(self):
        return "Guau!"  # Polimorfismo: método sobrescrito de la clase base

# Creación de instancias y uso de métodos
mi_perro = Perro("Fido", "Labrador")
print(f"Nombre del perro: {mi_perro.nombre}")
print(f"Raza del perro: {mi_perro.raza}")
print(f"Sonido que hace: {mi_perro.hacer_sonido()}")

# Clase con encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
    
    # Métodos de acceso (getter y setter)
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

# Creación de instancia y uso de métodos
persona1 = Persona("Juan", 30)
print(f"Nombre: {persona1.get_nombre()}")
print(f"Edad: {persona1.get_edad()}")

# Modificar edad utilizando setter
persona1.set_edad(35)
print(f"Nueva Edad: {persona1.get_edad()}")
