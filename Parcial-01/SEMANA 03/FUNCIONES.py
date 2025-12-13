# Función para ingresar las temperaturas de la semana
def ingresar_temperaturas():
    print("Ingrese las temperaturas de los 7 días de la semana:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]# arreglo con los días de la semana
    temperaturas = []

    for i in range(len(dias)):
        while True:
            try:
                temp = float(input(f"Temperatura día {dias[i]}: "))#permite ingresar el valor diario de la temperatura
                temperaturas.append(temp)#permite agreagar lo que tiene la variable temp a la lista temperatura

                break
            except ValueError:# permite manejar el error en caso de que el usuario inghrese un valor no númerico
                print("Entrada inválida. Por favor ingrese un número.")

    return temperaturas


# Función para calcular el promedio
def calcular_promedio(lista):
    suma = 0.0
    i = 1
    for dia in lista:# permite moverse por cada elemento de la lista
        suma = sum(lista)
        promedio = suma / len(lista)# permite calcular el promedio dividiendo la suma por la cantidad de elementos en la lista
    return promedio


# Función principal
def main():
    temps = ingresar_temperaturas()
    prom = calcular_promedio(temps)

    print("\nLas temperaturas ingresadas son:", temps)
    print(f"El promedio semanal es:{prom: .2f} °C")



# Llamada a la función principal
main()
