#1.  Se importa el módulo yacc de la biblioteca PLY, que se utiliza para definir el analizador sintáctico.
import ply.yacc as yacc
from lexer import tokens # importar los tokens definidos en lexer.py

#2. Definición de las funciones asociadas con las reglas de producción
def p_S(p):
    'S : LKEY A RKEY'
    p[0] = (p[1], p[3])

def p_folio(p):
    'A : FOLIO COLON NUM_FOLIO COMMA B'
    p[0] = (p[1], p[2], p[3], p[4])

def p_fecha_forma(p):
    'B : FECHA_FORMA COLON FECHA_HORA COMMA C'
    p[0] = (p[1], p[2], p[3], p[4])

def p_fecha_validacion(p):
    'C : FECHA_VALIDACION COLON FECHA_HORA COMMA D'
    p[0] = (p[1], p[2], p[3], p[4])

def p_paciente(p):
    'D : PACIENTE COLON LKEY E RKEY COMMA I'
    p[0] = (p[1], p[2], p[3], p[5], p[6])

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
    'H : EDAD COLON NUM_EDAD'
    p[0] = (p[1], p[2], p[3])

def p_medico_solicitante(p):
    'I : MEDICO_SOLICIANTE COLON CADENA COMMA J'
    p[0] = (p[1], p[2], p[3], p[4])

def p_seccion(p):
    'J : SECCION COLON BIOMETRIA_HEMATICA COMMA K'
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_parametros(p):
    'K : PARAMETROS COLON LTKEY O RTKEY COMMA L'
    p[0] = (p[1], p[2], p[3], p[4])

def p_firma(p):
    'L : FIRMA COLON LKEY M RKEY'
    p[0] = (p[1], p[2], p[3], p[5])

def p_responsable(p):
    'M : RESPONSABLE COLON CADENA COMMA N'
    p[0] = (p[1], p[2], p[3], p[4])

def p_cedula(p):
    'N : CEDULA COLON NUM_CEDULA'
    p[0] = (p[1], p[2], p[3])

def p_leucocitos_parametro(p):
    'O : LKEY NOMBRE COLON LEUCOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES RKEY COMMA P'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18])

def p_eritrocitos_parametro(p):
    'O : LKEY NOMBRE COLON ERITROCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES RKEY COMMA P'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18])

def p_hemoglobina_parametro(p):
    'O : LKEY NOMBRE COLON HEMOGLOBINA COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_GPD COMMA LIMITE COLON LIMITE_VALUES RKEY COMMA P'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18])

def p_hematrocito_parametro(p):
    'O : LKEY NOMBRE COLON PLAQUETAS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_PORCENTAJE COMMA LIMITE COLON LIMITE_VALUES RKEY COMMA P'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18])

def p_plaquetas_parametro(p):
    'O : LKEY NOMBRE COLON PLAQUETAS COMMA RESULTADO COLON NUM_PLAQUETAS COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES RKEY COMMA P'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18])

def p_nota_opcional(p):
    'P : NOTA COLON SIMBOLOS_NOTA'
    p[0] = p[3]

def p_nota_vacia(p):
    'P : '
    p[0] = None

# 3. Definición de la función para manejar errores de sintaxis
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")  # Imprime el token donde ocurrió el error
    else:
        print("Syntax error at EOF")  # Indica un error al final de la entrada

#4. Construcción del analizador sintáctico
parser = yacc.yacc() #se crea instancia del analizador sintáctico
