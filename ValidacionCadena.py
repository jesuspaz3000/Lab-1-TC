# Definición del alfabeto y ejemplos de palabras
alfabeto = ['a', 'b', 'c', 'd']

# Definición de palabras de ejemplo
w1 = "a"
w2 = "ab"
w3 = "abc"
w4 = "bc"
w5 = "cd"

# Definición de lenguajes como conjuntos de palabras
L1 = [w1, w2]        # L1 = {"a", "ab"}
L2 = [w2, w3]        # L2 = {"ab", "abc"}
L3 = [w3, w4, w5]    # L3 = {"abc", "bc", "cd"}

# Función que implementa la operación de unión entre dos lenguajes
def union(LA, LB):
    resultado = []
    for elemento in LA + LB:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

# Función que implementa la operación de concatenación entre dos lenguajes
def concatenar(LA, LB):
    resultado = []
    for a in LA:
        for b in LB:
            concatenado = a + b
            if concatenado not in resultado:
                resultado.append(concatenado)
    return resultado

# Función que implementa la cerradura de Kleene con un límite práctico de longitud
def cerradura_kleene(L, max_len=3):
    resultado = [""]

    def generar_combinaciones(elementos, longitud, actual="", resultados=None):
        if resultados is None:
            resultados = []

        if longitud == 0:
            if len(actual) <= max_len and actual not in resultados:
                resultados.append(actual)
            return

        for elem in elementos:
            nueva_cadena = actual + elem
            if len(nueva_cadena) <= max_len:
                generar_combinaciones(elementos, longitud - 1, nueva_cadena, resultados)

        return resultados

    palabras_generadas = []
    for r in range(1, 4):
        nuevas_palabras = generar_combinaciones(L, r)
        if nuevas_palabras:
            palabras_generadas.extend(nuevas_palabras)

    for palabra in palabras_generadas:
        if palabra not in resultado:
            resultado.append(palabra)

    return resultado

# Cálculo de operaciones entre lenguajes
union_L1_L2 = union(L1, L2)
union_L1_L3 = union(L1, L3)
union_L2_L3 = union(L2, L3)

# Concatenación sin límite de caracteres
concat_L1_L2 = concatenar(L1, L2)
concat_L2_L3 = concatenar(L2, L3)
concat_L1_L3 = concatenar(L1, L3)

kleene_L1 = cerradura_kleene(L1)

# Visualización de resultados de las operaciones básicas
print("Unión:")
print("L1 U L2:", union_L1_L2)
print("L1 U L3:", union_L1_L3)
print("L2 U L3:", union_L2_L3)

print("\nConcatenación:")
print("L1 ⋅ L2:", concat_L1_L2)
print("L2 ⋅ L3:", concat_L2_L3)
print("L1 ⋅ L3:", concat_L1_L3)

print("\nCerradura de Kleene de L1 (≤3 caracteres):")
print("L1*:", kleene_L1)

print("\nCerradura de Kleene de L2 (≤3 caracteres):")
print("L2*:", cerradura_kleene(L2))

print("\nCerradura de Kleene de L3 (≤3 caracteres):")
print("L3*:", cerradura_kleene(L3))

# ====================== PARTE DE VALIDACIÓN DE CADENAS ======================
print("\n\n--- DESCRIPCIONES DE LENGUAJES ---")

# Descripción 1: "Todas las cadenas que comienzan con 'a'"
# Esta función evalúa si una cadena comienza con la letra 'a'
def lenguaje1(cadena):
    return cadena.startswith("a")

# Descripción 2: "Todas las cadenas que contienen al menos una 'b'"
# Esta función evalúa si una cadena contiene al menos una letra 'b'
def lenguaje2(cadena):
    return "b" in cadena

# Evaluación de cadenas para el Lenguaje 1
print("\nLenguaje 1: Todas las cadenas que comienzan con 'a'")
print("Validación de palabras existentes:")
palabras_existentes = union(union(L1, L2), L3)
for palabra in palabras_existentes:
    print(f"'{palabra}': {'Válida' if lenguaje1(palabra) else 'Inválida'}")

# Ejemplos adicionales para el Lenguaje 1
print("\nEjemplos válidos adicionales para Lenguaje 1:")
ejemplos_validos_l1 = ["a", "ab", "abc"]
for ejemplo in ejemplos_validos_l1:
    print(f"'{ejemplo}': Válida")

print("\nEjemplos inválidos para Lenguaje 1:")
ejemplos_invalidos_l1 = ["bc", "cd", "d"]
for ejemplo in ejemplos_invalidos_l1:
    print(f"'{ejemplo}': Inválida")

# Evaluación de cadenas para el Lenguaje 2
print("\nLenguaje 2: Todas las cadenas que contienen al menos una 'b'")
print("Validación de palabras existentes:")
for palabra in palabras_existentes:
    print(f"'{palabra}': {'Válida' if lenguaje2(palabra) else 'Inválida'}")

# Ejemplos adicionales para el Lenguaje 2
print("\nEjemplos válidos adicionales para Lenguaje 2:")
ejemplos_validos_l2 = ["b", "abc", "bc"]
for ejemplo in ejemplos_validos_l2:
    print(f"'{ejemplo}': Válida")

print("\nEjemplos inválidos para Lenguaje 2:")
ejemplos_invalidos_l2 = ["a", "cd", "acd"]
for ejemplo in ejemplos_invalidos_l2:
    print(f"'{ejemplo}': Inválida")

# Descripción 3: "Cadenas con número par de caracteres"
# Esta función evalúa si una cadena tiene un número par de caracteres
def lenguaje3(cadena):
    return len(cadena) % 2 == 0

# Evaluación de cadenas para el Lenguaje 3
print("\nLenguaje 3: Cadenas con número par de caracteres")
print("Validación de palabras existentes:")
for palabra in palabras_existentes:
    print(f"'{palabra}': {'Válida' if lenguaje3(palabra) else 'Inválida'}")

# Ejemplos adicionales para el Lenguaje 3
print("\nEjemplos válidos adicionales para Lenguaje 3:")
ejemplos_validos_l3 = ["ab", "cd", "abcd"]
for ejemplo in ejemplos_validos_l3:
    print(f"'{ejemplo}': Válida")

print("\nEjemplos inválidos para Lenguaje 3:")
ejemplos_invalidos_l3 = ["a", "abc", "abcde"]
for ejemplo in ejemplos_invalidos_l3:
    print(f"'{ejemplo}': Inválida")