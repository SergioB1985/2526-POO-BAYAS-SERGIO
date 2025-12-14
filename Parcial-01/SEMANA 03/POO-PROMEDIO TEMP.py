from abc import ABC, abstractmethod # para clase abstracta

# ===============================
# 1. ABSTRACCIÓN
# ===============================
class RegistroClima(ABC): # clase base abstracta
    def __init__(self, dia):
        self._dia = dia   # protegido (encapsulamiento)
    # función abstracta para obtener temperaturas
    @abstractmethod
    def obtener_temperatura(self):
        pass # metodo abstracto

    @abstractmethod
    def mostrar(self):
        pass


# ===============================
# 2. HERENCIA
# ===============================
class ClimaDiario(RegistroClima): # clase concreta que implimenta la abstracción
    def __init__(self, dia, temperatura):
        super().__init__(dia) # llama al constructor de la clase base
        self.__temperatura = temperatura   # privado (encapsulamiento)

    # ===============================
    # 3. ENCAPSULAMIENTO
    # ===============================
    def obtener_temperatura(self):
        return self.__temperatura # devuelve la temperatura del día
    # función para mostrar el día y la temperatura
    def mostrar(self):
        return f"{self._dia}: {self.__temperatura} °C" # muestra el día y la temperatura


# ===============================
# Clase que gestiona la semana
# ===============================
class SemanaClimatica:
    def __init__(self):
        self.__registros = []  # lista privada
    # función para agregar un registro diario
    def agregar_dia(self, clima):
        self.__registros.append(clima) # agrega el registro diario a la lista privado
    # función para calcular el promedio semanal
    def calcular_promedio(self):
        total = 0
        for registro in self.__registros: # iteración sobre los registros día a día
            total += registro.obtener_temperatura()  # POLIMORFISMO
        return total / len(self.__registros) # devuelve el promedio semanal
    # función para mostrar todas las temperaturas de la semana
    def mostrar_semana(self):
        for registro in self.__registros: # iteración sobre los registros día a día
            print(registro.mostrar())  # POLIMORFISMO


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
def main():
    semana = SemanaClimatica()
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    for i in range(len(dias)):
        temp = float(input(f"Ingrese la temperatura del día {dias[i]}: "))
        dia = f"Día {dias[i]}"
        clima = ClimaDiario(dia, temp)
        semana.agregar_dia(clima)

    print("\n--- TEMPERATURAS REGISTRADAS ---")
    semana.mostrar_semana()

    promedio = semana.calcular_promedio()
    print(f"\nPromedio semanal: {promedio:.2f} °C")

# ejecuta el programa principal
if __name__ == "__main__":
    main()