# main.py — versión final integrada con análisis léxico, sintáctico y semántico

from lexer import lexer
from parser import parser
from semantic import validar_semantica
from errors import errors, print_errors

# Archivo a validar
archivo = "ejemplo.json"

with open(archivo, 'r', encoding='utf-8') as json_archivo:
    data = json_archivo.read()

print("\n=================================================")
print(f" Validando archivo: {archivo}")
print("=================================================\n")

# ---------------------- ANÁLISIS LÉXICO ----------------------
print("======== ANÁLISIS LÉXICO ========")
lexer.input(data)

for token in lexer:
    print(f"Token: {token.type:15} Valor: {token.value}")

# ---------------------- ANÁLISIS SINTÁCTICO ----------------------
print("\n======== ANÁLISIS SINTÁCTICO ========")
resultado = parser.parse(data)

if resultado is None:
    print("❌ Error: No se pudo generar el árbol sintáctico.\n")
else:
    print("✔ Estructura general válida.\n")
    print("Árbol sintáctico:")
    print(resultado)

# ---------------------- ANÁLISIS SEMÁNTICO ----------------------
print("\n======== ANÁLISIS SEMÁNTICO ========")

if resultado:
    validar_semantica(resultado)
    print("\nNo se encontraron errores semánticos en el archivo")
else:
    print("\n❌ No se ejecutó el análisis semántico debido a errores sintácticos.\n")

# ---------------------- REPORTE FINAL ----------------------
print_errors()

total_errores = (
    len(errors["lexicos"]) +
    len(errors["sintacticos"]) +
    len(errors["semanticos"])
)

print("\n=================================================")
print(f" Archivo: {archivo}")
print("-------------------------------------------------")
if total_errores == 0:
    print("✔ Archivo totalmente válido.")
else:
    print(f"❌ Archivo con {total_errores} error(es) encontrados.")

print("=================================================\n")
