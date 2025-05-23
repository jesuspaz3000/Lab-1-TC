# Lab-1-TC: Operaciones sobre Alfabetos y Lenguajes Formales

## Descripción del Laboratorio
Este laboratorio implementa distintas operaciones sobre alfabetos y lenguajes formales como parte del curso de Teoría de la Computación. Se trabaja con operaciones básicas sobre conjuntos de cadenas, validación de pertenencia a lenguajes según descripciones formales, y se implementan operaciones como unión, concatenación y cerradura de Kleene.

## Archivos del laboratorio

### Alfabeto.py
- Define un alfabeto `['a', 'b', 'c', 'd']` y varios lenguajes (L1, L2, L3)
- Implementa operaciones fundamentales sobre lenguajes:
  - Unión de lenguajes
  - Concatenación de lenguajes
  - Cerradura de Kleene (con límite de caracteres)
- Muestra ejemplos de cada operación con los lenguajes definidos

### ValidacionCadena.py
- Utiliza las definiciones de alfabeto y lenguajes del archivo Alfabeto.py
- Implementa funciones para validar si una cadena pertenece a un lenguaje según descripciones formales
- Define tres lenguajes formales con sus respectivas descripciones:
  1. "Todas las cadenas que comienzan con 'a'"
  2. "Todas las cadenas que contienen al menos una 'b'"
  3. "Cadenas con número par de caracteres"
- Para cada lenguaje muestra:
  - Validación de las palabras existentes en L1, L2 y L3
  - 3 ejemplos de cadenas válidas adicionales
  - 3 ejemplos de cadenas inválidas

## Operaciones Implementadas
- **Unión**: combina dos lenguajes sin duplicar elementos
- **Concatenación**: genera nuevas cadenas concatenando cada elemento del primer lenguaje con cada elemento del segundo
- **Cerradura de Kleene**: genera todas las posibles combinaciones de palabras del lenguaje (con un límite práctico de longitud)
- **Validación**: determina si una cadena pertenece a un lenguaje según criterios específicos

## Cómo Ejecutar
Para ver los resultados de las operaciones sobre alfabetos:
```
python Alfabeto.py
```

Para ver la validación de cadenas según descripciones de lenguajes:
```
python ValidacionCadena.py
```
