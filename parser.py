#1.  Se importa el módulo yacc de la biblioteca PLY, que se utiliza para definir el analizador sintáctico.
import ply.yacc as yacc
from lexer import tokens # importar los tokens definidos en lexer.py

#2. Definición de las funciones asociadas con las reglas de producción
def p_S(p):
    'S : LKEY A RKEY'
    p[0] = (p[1], p[3])

def p_folio(p):
    'A : FOLIO COLON NUM COMMA B'
    p[0] = (p[1], p[2], p[3], p[4])

def p_fecha_forma(p):
    'B : FECHA_FORMA COLON FECHA_HORA COMMA C'
    p[0] = (p[1], p[2], p[3], p[4])

def p_fecha_validacion(p):
    'C : FECHA_VALIDACION COLON FECHA_HORA COMMA D'
    p[0] = (p[1], p[2], p[3], p[4])

def p_paciente(p):
    'D : PACIENTE COLON LKEY E RKEY'
    p[0] = (p[1], p[2], p[3], p[5])

def p_nombre(p):
    'E : NOMBRE COLON CADENA COMMA F'
    p[0] = (p[1], p[2], p[3], p[4])

def p_fecha_nac(p):
    'F : FECHA_NAC COLON FECHA COMMA G'
    p[0] = (p[1], p[2], p[3], p[4])

def p_sexo(p):
    'G : SEXO COLON CARACTER COMMA H'
    p[0] = (p[1], p[2], p[3], p[4])

def p_edad(p):
    'H : EDAD COLON NUM'
    p[0] = (p[1], p[2], p[3])

# 3. Definición de la función para manejar errores de sintaxis
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")  # Imprime el token donde ocurrió el error
    else:
        print("Syntax error at EOF")  # Indica un error al final de la entrada

#4. Construcción del analizador sintáctico
parser = yacc.yacc() #se crea instancia del analizador sintáctico
