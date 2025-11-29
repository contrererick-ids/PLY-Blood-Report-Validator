# Importa el analizador léxico definido en lexer.py y el analizador sintáctico definido en parser.py
from lexer import lexer
from parser import parser
import json

# Prueba a realizar
archivo = "ejemplo.json"
with open(archivo, 'r', encoding = 'utf-8') as json_archivo:
    data = json_archivo.read()

# Array que almacena la cantidad de errores encontrados
errores_totales = []

# Cadena de entrada
lexer.input(data) # Se analiza la cadena por el analizador léxico

print(f"Analizando: \n{data}")
print("\n======== ANÁLISIS LÉXICO ========")
print("Tokens:")
for token in lexer:
    print(f'Token: {token.type}, Valor: {token.value}') #Se imprimen los tokens generados por el analizador

print("\n======== ANÁLISIS SINTÁCTICO ========")
result = parser.parse(data) # Se analiza la cadena por el parser sintáctico
print("\nResultado del análisis sintáctico: ")
print(result) # Se imprime el analisis

# print(f"\n======== Validación del archivo {archivo} ========")
# if errores_totales > 10:
#     print(f"❌ Estructura general no válida, se han encontrado {errores_totales} errores en el archivo")
# else:
#     print("✅ Estructura general válida")
#     # Aqui tmb se tienen que imprimir todos los errores sintacticos, semanticos o lexicos que aparezcan durante la ejecucion del codigo
#     print(f"✅ Archivo verificado con {errores_totales} advertencias")