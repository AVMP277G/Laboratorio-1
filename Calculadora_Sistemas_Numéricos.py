def decimal_to_binary(n, bits=8):
    return format(n, f'0{bits}b')

def decimal_to_hexadecimal(n):
    return hex(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def binary_to_decimal(b):
    return int(b, 2)

def hexadecimal_to_decimal(h):
    return int(h, 16)

def octal_to_decimal(o):
    return int(o, 8)

def complemento_a_2(n, bits=8):
    """Calcula el complemento a 2 de un número decimal con cierta cantidad de bits."""
    if n >= 0:
        return format(n, f'0{bits}b')
    else:
        return format((1 << bits) + n, f'0{bits}b')

if _name_ == "_main_":
    while True:
        print("\n Calculadora de Conversiones ")

        print("1. Decimal")
        print("2. Binario")
        print("3. Hexadecimal")
        print("4. Octal")
        print("5. Complemento a 2")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            decimal = int(input("Ingresa un número decimal: "))
            print("Binario:", decimal_to_binary(decimal))
            print("Hexadecimal:", decimal_to_hexadecimal(decimal))
            print("Octal:", decimal_to_octal(decimal))

        elif opcion == "2":
            binario = input("Ingresa un número binario: ")
            print("Decimal:", binary_to_decimal(binario))

        elif opcion == "3":
            hexadecimal = input("Ingresa un número hexadecimal: ")
            print("Decimal:", hexadecimal_to_decimal(hexadecimal))

        elif opcion == "4":
            octal = input("Ingresa un número octal: ")
            print("Decimal:", octal_to_decimal(octal))

        elif opcion == "5":
            decimal_str = input("Ingresa un número decimal (negativo): ")
            decimal = int(decimal_str.replace(" ", "")) # Remueve espacios despúes para convertirlo en int
            bits = int(input("Número de bits a usar (ej: 8, 16, 32): "))
            print("Complemento a 2:", complemento_a_2(decimal, bits))

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
