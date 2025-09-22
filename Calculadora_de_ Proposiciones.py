import itertools

def reemplazar_simbolos(expresion):
    """Reemplaza los símbolos lógicos por operadores de Python."""
    return (expresion
            .replace('¬', ' not ')
            .replace('∧', ' and ')
            .replace('∨', ' or ')
            .replace('→', ' or not ')  
            .replace('↔', ' == '))

def extraer_variables(expresion):
    """Extrae las variables únicas de la expresión."""
    return sorted(set(filter(str.isalpha, expresion)))

def generar_tabla_verdad(expresion):
    try:
        variables = extraer_variables(expresion)
        expresion_convertida = reemplazar_simbolos(expresion.strip())

        ancho_col = 5
        encabezado = " ".join(f"{var:^{ancho_col}}" for var in variables) + f" | {expresion}"
        separador = "-" * len(encabezado)

        print("\nTabla de Verdad:")
        print(encabezado)
        print(separador)

        for valores in itertools.product([0, 1], repeat=len(variables)):
            # Convertir 0 y 1 a False y True
            contexto = dict(zip(variables, map(bool, valores)))
            resultado = int(eval(expresion_convertida, {}, contexto))
            valores_str = " ".join(f"{v:^{ancho_col}}" for v in valores)
            print(f"{valores_str} | {resultado}")

    except SyntaxError:
        print("Error: Expresión lógica inválida. Verifique los símbolos y la sintaxis.")
    except Exception as e:
        print(f"Error al evaluar la expresión: {e}")

if _name_ == "_main_":
    expresion = input("Ingrese la expresión lógica (ej: (p∧q)∨(r↔¬q) ): ")
    generar_tabla_verdad(expresion)
