# ==========================================
# Clase base: Empleado
# Demuestra encapsulación y herencia
# ==========================================
# Programa que registra Empleados y Gerentes, demostrando los conceptos de POO: Clase, Objeto, Herencia, Encapsulado y Polimorfismo
class Empleado:
    # Constructor de la clase Empleado
    def __init__(self, nombre, salario):
        self.nombre = nombre # Atributo público
        self.__salario = salario  # Atributo protegido (encapsulación)

    # metodo getter que permite aceder al salario de un atributo protegido
    def get_salario(self):
        return self.__salario

    # metodo Setter que permite modificar el salario de un atributo protegido, controla que el salario no sea negativo ni cero
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Error: el salario debe ser mayor que cero")

    # Método polimórfico que se comporta diferente en la clase derivada, calcula el bono del empleado
    def calcular_bono(self):
        return self.__salario * 0.10

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario: {self.__salario}")


# ==========================================
# Clase derivada: Gerente
# Demuestra herencia y polimorfismo
# ==========================================

class Gerente(Empleado):
    # Constructor de la clase Gerente que hereda de Empleado
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Sobrescritura del método (polimorfismo)
    def calcular_bono(self):
        return self.get_salario() * 0.20 # Metodo get que permite leer o acceder al atributo salario protegido

    def mostrar_informacion(self):
        print(f"Gerente: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario: {self.get_salario()}") # imprime el salario usando el metodo get que permite acceder al atributo protegido


# ==========================================
# Función que demuestra polimorfismo
# ==========================================
# metodo que recibe un objeto de tipo Empleado o Gerente y muestra el bono correspondiente
def mostrar_bono(persona):
    print(f"Bono asignado: {persona.calcular_bono()}")


# ==========================================
# Programa principal
# ==========================================
def main ():
    print("=== Registro de Empleado ===")
    nombre_emp = input("Ingrese el nombre del empleado: ")
    salario_emp = float(input("Ingrese el salario del empleado: "))

    empleado = Empleado(nombre_emp, salario_emp) # crea un objeto de la clase Empleado

    print("\n=== Registro de Gerente ===")
    nombre_ger = input("Ingrese el nombre del gerente: ")
    salario_ger = float(input("Ingrese el salario del gerente: "))
    departamento_ger = input("Ingrese el departamento del gerente: ")

    gerente = Gerente(nombre_ger, salario_ger, departamento_ger) # crea un objeto de la Clase Gerente

    print("\n=== Información Ingresada ===")
    empleado.mostrar_informacion() # muestra información del Empleado
    mostrar_bono(empleado) # muestra el bono del Empleado

    print("\n----------------------------")

    gerente.mostrar_informacion() # muestra la información del Gerente
    mostrar_bono(gerente) # muestra el bono del Gerente

# ==========================================
# Punto de entrada del programa
# ==========================================

if __name__ == "__main__":
    main()