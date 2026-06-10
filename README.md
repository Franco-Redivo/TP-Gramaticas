# Compilador de Control de Residuos Peligrosos con ANTLR4

## Descripción 

Trabajo práctico desarrollado para la materia Teoría de la Computación y Lenguajes.

El objetivo del proyecto es construir un compilador utilizando ANTLR4 capaz de procesar un lenguaje diseñado para representar algoritmos relacionados con el control de residuos peligrosos.

### El compilador realiza:  

- Análisis léxico mediante un Lexer generado por ANTLR4.
- Análisis sintáctico mediante un Parser generado por ANTLR4.
- Construcción del árbol sintáctico (Parse Tree).
- Detección de errores sintácticos.

### Estructura del Proyecto
.
\
├── Residuos.g4\
├── main.py\
├── test_correcto.txt\
├── test_error_sintactico.txt\
├── test_error_sintactico2.txt\
├── ResiduosLexer.py\
├── ResiduosParser.py\
└── README.md\

### Gramática Implementada

El lenguaje soporta:

- Definición de funciones.
- Parámetros.
- Variables.
- Asignaciones.
- Expresiones.
- Llamadas a funciones.
- Sentencias condicionales (if / else).
- Retorno de valores (return).

Ejemplo:

```
function generar_codigo_residuo(
    nivel_peligrosidad,
    cantidad_kilos,
    destino
)
{
    if (cantidad_kilos > 450)
    {
        return "Error";
    }

    codigo =
        upper(slice(nivel_peligrosidad,3))
        + "-"
        + cantidad_kilos
        + "-"
        + upper(slice(destino,3));

    return codigo;
}
````

### Requisitos
Python 3.x\
Java\
ANTLR4

Instalar dependencias:

pip install -r requirements.txt

### Generar Archivos de ANTLR
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Residuos.g4

### Ejecutar
python main.py

El programa leerá el archivo de prueba seleccionado dentro de main.py y mostrará el árbol sintáctico generado.
