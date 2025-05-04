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
# La unión de dos lenguajes es el conjunto de todas las cadenas que están
# en al menos uno de los dos lenguajes, sin repeticiones
def union(LA, LB):
    resultado = []
    for elemento in LA + LB:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

# Función que implementa la operación de concatenación entre dos lenguajes
# La concatenación de dos lenguajes es el conjunto de todas las cadenas 
# que se pueden formar concatenando una cadena del primer lenguaje con 
# una cadena del segundo lenguaje
def concatenar(LA, LB):
    resultado = []
    for a in LA:
        for b in LB:
            concatenado = a + b
            if concatenado not in resultado:
                resultado.append(concatenado)
    return resultado

# Función que implementa la cerradura de Kleene con un límite práctico de longitud
# La cerradura de Kleene de un lenguaje L es el conjunto de todas las cadenas que se pueden
# formar concatenando cualquier número (incluso cero) de cadenas de L
def cerradura_kleene(L, max_len=3):
    # Incluimos la cadena vacía que siempre está en L*
    resultado = [""]

    # Función recursiva para generar combinaciones de palabras hasta cierta longitud
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

# Cerradura de Kleene limitada a palabras de hasta 3 caracteres
kleene_L1 = cerradura_kleene(L1)

# Visualización de resultados
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