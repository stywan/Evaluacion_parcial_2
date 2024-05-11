
def main(nombre):
   #nombre = input("ingrese su nombre: ")

    print("1. operadores Matematicos")
    print("2. operadores Relacionales")
    print("3. validador de tipos de datos")

    opcion = int(input("ingrese su opcion: "))

    if opcion == 1:
        operadores_matematicos(nombre)
    elif opcion == 2:
        operadores_relacionales(nombre)
    elif opcion == 3:
        validador_tipos_datos(nombre)
    else:
        print(f"{nombre}, opción no válida.")

def operadores_matematicos(nombre):
  
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. división")
    print("5. modulo (resto)")
    print("6. potencia")

    operacion = int(input("ingrese su opcion: "))

    if operacion in [1, 2, 3, 4, 6]:
        numero1 = float(input(f"{nombre}, ingrese el primer numero: "))
        numero2 = float(input(f"{nombre}, ingrese el segundo numero: "))
    elif operacion == 5:
        numero1 = int(input(f"{nombre}, ingrese el primer numero (dividendo): "))
        numero2 = int(input(f"{nombre}, ingrese el segundo numero (divisor): "))
    else:
        print(f"{nombre}, opcion no valida.")
        return

    if operacion == 1:
        resultado = numero1 + numero2
    elif operacion == 2:
        resultado = numero1 - numero2
    elif operacion == 3:
        resultado = numero1 * numero2
    elif operacion == 4:
        if numero2 == 0:
            print(f"{nombre}, no se puede dividir por cero.")
            return
        resultado = numero1 / numero2
    elif operacion == 5:
        resultado = numero1 % numero2
    elif operacion == 6:
        resultado = numero1 ** numero2


    print(f"{nombre}, el resultado de la operación es: {resultado}")

def operadores_relacionales(nombre):

    numero1 = float(input(f"{nombre}, ingrese el primer número: "))
    numero2 = float(input(f"{nombre}, ingrese el segundo número: "))

    if numero1 > numero2:
        mayor = numero1
        menor = numero2
        comparacion = "mayor"
    elif numero1 < numero2:
        mayor = numero2
        menor = numero1
        comparacion = "mayor"
    else:
        mayor = numero1
        menor = numero2
        comparacion = "igual"

    print(f"{nombre}, el número {mayor} es {comparacion} que el número {menor}.")

def validador_tipos_datos(nombre):

    dato = input(f"{nombre}, ingrese un dato: ")

    tipo_dato = type(dato)
    if tipo_dato == str:
        tipo_da = "cadena de texto"
    elif tipo_dato == int:
        tipo_da = "número entero"
    elif tipo_dato == float:
        tipo_da = "número decimal"
    elif tipo_dato == bool:
        tipo_da = "valor booleano"
    else:
        tipo_da = "tipo desconocido"

    print(f"{nombre}, el dato ingresado es de tipo {tipo_da}.")
    
main("victor")


