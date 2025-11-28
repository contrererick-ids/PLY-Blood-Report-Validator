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
        {"nombre": "Leucocitos", "resultado": 5.9, "unidad": "10^3/μL", "limite": "[4.5 - 10.0]"},
        {"nombre": "Eritrocitos", "resultado": 4.82, "unidad": "10^6/μL", "limite": "[4.3 - 5.8]"},
        {"nombre": "Hemoglobina", "resultado": 14.2, "unidad": "g/dL", "limite": "[12.0 - 16.0]"},
        {"nombre": "Hematocrito", "resultado": 42.5, "unidad": "%", "limite": "[36.0 - 46.0]"},
        {"nombre": "Plaquetas", "resultado": 210, "unidad": "10^3/μL", "limite": "[150 - 400]", "nota": "+"}
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
