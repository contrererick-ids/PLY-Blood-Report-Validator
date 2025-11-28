# Importa el analizador léxico definido en lexer.py y el analizador sintáctico definido en parser.py
from lexer import lexer
from parser import parser

# Prueba a realizar
data = """
{
    "folio": 12345678,
    "fecha_forma": "01/10/2023 14:30:12",
    "fecha_validacion": "02/10/2023 10:00:27",
    "paciente": {
        "nombre": "Juan Pérez",
        "fecha_nacimiento": "15/05/1980",
        "sexo": "M",
        "edad": 43
    },
    "medico_solicitante": "Dra. María López",
    "seccion": "Biometría Hemática",
    "parametros": [
     ],
    "firma": {
        "responsable": "Dra. María López",
        "cedula": "12345678"
    }
}
"""

# Cadena de entrada
lexer.input(data) # Se analiza la cadena por el analizador léxico

print(f"Analizando: {data}")
print("======== ANÁLISIS LÉXICO ========")
print("Tokens:")
for token in lexer:
    print(f'Token: {token.type}, Valor: {token.value}') #Se imprimen los tokens generados por el analizador

print("\n======== ANÁLISIS SINTÁCTICO ========")
result = parser.parse(data) # Se analiza la cadena por el parser sintáctico
print("\nResultado del análisis sintáctico: ")
print(result) # Se imprime el analisis
