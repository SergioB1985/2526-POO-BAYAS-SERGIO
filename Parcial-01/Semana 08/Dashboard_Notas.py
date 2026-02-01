# ======================================================
# SISTEMA DE CÁLCULO DE NOTAS CON MENÚS
# Autor: ---
# Descripción:
# Este programa permite ingresar notas por unidades,
# calcular el promedio y determinar si el estudiante
# aprueba o reprueba, utilizando un menú interactivo.
# ======================================================


def mostrar_menu():
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    notas = {
        'Unidad 1': [],
        'Unidad 2': []
    }

    while True:
        print("\nMENÚ PRINCIPAL - SISTEMA DE NOTAS")
        for key in unidades: # Utiliza un bucle para imprimir las opciones del menu
            print(f"{key} - {unidades[key]}") # Imprime las unidades
        print("0 - Salir")

        opcion = input("Seleccione una unidad: ")

        if opcion == '0':
            print("👋 Saliendo del sistema de notas.")
            break
        elif opcion in unidades: # Opción válida para ingresar a una unidad
            mostrar_sub_menu(unidades[opcion], notas)
        else: # Control de errores para opciones invalidas
            print(" ⚠️ Opción no válida.")


def mostrar_sub_menu(unidad, notas): # Muestra el submenú para una unidad especifica
    while True:
        print(f"\nSUBMENÚ - {unidad}")
        print("1 - Ingresar notas")
        print("2 - Calcular promedio")
        print("0 - Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break
        elif opcion == '1':
            ingresar_notas(unidad, notas)
        elif opcion == '2':
            calcular_promedio(unidad, notas)
        else:
            print("Opción no válida.")


def ingresar_notas(unidad, notas):
    try:
        cantidad = int(input("¿Cuántas notas desea ingresar?: "))
        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if 0 <= nota <= 10: # Control de ingreso de notas validas
                notas[unidad].append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Error: Ingrese valores numéricos.")


def calcular_promedio(unidad, notas): # Calcula y muestra el promedio de las notas ingresadas
    if len(notas[unidad]) == 0:
        print("No hay notas registradas.")
        return

    promedio = sum(notas[unidad]) / len(notas[unidad]) # Calcula el promedio de las notas
    print(f"\nPromedio de {unidad}: {promedio:.2f}")

    if promedio >= 7:
        print("Estado: APROBADO ✅")
    else:
        print("Estado: REPROBADO ❌")


# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()