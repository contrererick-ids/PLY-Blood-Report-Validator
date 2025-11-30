#1.  Se importa el módulo yacc de la biblioteca PLY, que se utiliza para definir el analizador sintáctico.
import ply.yacc as yacc
from lexer import tokens # importar los tokens definidos en lexer.py

# 1.5 Implementación del automáta de pila
# Se crea la pila que va a almacenar los valores del AP
AP = []

# Función para validar si el símbolo de cierre es el correcto (dependiendo del de inicio)
def validar_simbs(sim_cierre):
    if sim_cierre == '}':
        sim_inicio = '{'
    elif sim_cierre == ']':
        sim_inicio = '['
    else:
        print("\n❗Símbolo no válido")

    # Si hay un símbolo de cierre sin que haya uno inicial
    if not AP:
        print("\n❌ Error en el AP: No puede haber un símbolo de cierre sin uno de apertura")

    # En base al último símbolo guardado en la pila... 
    tope_AP = AP[-1]

    # Se desapila el símbolo final si coincide (es el par) del inicial
    if tope_AP == sim_inicio:
        AP.pop()
        print(f"↓ Despilando símbolo '{tope_AP}'")

    else:
        print(f"\n❌ Error en el AP: El símbolo de cierre no concuerda con el último cierre almacenado")

#2. Definición de las funciones asociadas con las reglas de producción
def p_S(p):
    'S : LKEY A RKEY'

    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = (p[1], p[3])

    validar_simbs('}') # se desapila el símbolo }

    # Revisa si quedan símbolos en el AP una vez terminada la ejecución
    if len(AP) == 0:
        print("\n✅ Automáta de Pila finalizado correctamente! La pila está vacía")
    else:
        print("\n❌ Error en el AP: Quedan símbolos en el AP, por lo que el automáta no es válido")

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

    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = (p[1], p[2], p[3], p[5], p[6])

    validar_simbs('}') # se desapila el símbolo }

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

    AP.append('[') # se agrega [ al AP
    print("↑ Apilando símbolo '['")

    p[0] = (p[1], p[2], p[3], p[4])

    validar_simbs(']') # se desapila el símbolo ]

def p_firma(p):
    'L : FIRMA COLON LKEY M RKEY'

    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = (p[1], p[2], p[3], p[5])

    validar_simbs('}') # se desapila el símbolo }

def p_responsable(p):
    'M : RESPONSABLE COLON CADENA COMMA N'
    p[0] = (p[1], p[2], p[3], p[4])

def p_cedula(p):
    'N : CEDULA COLON NUM_CEDULA'
    p[0] = (p[1], p[2], p[3])

def p_lista_parametros_multiple(p):
    'O : O COMMA PARAMETRO'
    p[0] = p[1] + [p[3]]

def p_lista_parametros_simple(p):
    'O : PARAMETRO'
    p[0] = [p[1]]

def p_parametro_leucocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON LEUCOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('leucocitos', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_eritrocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON ERITROCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('eritrocitos', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_hemoglobina(p):
    'PARAMETRO : LKEY NOMBRE COLON HEMOGLOBINA COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_GPD COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('hemoglobina', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_hematocrito(p):
    'PARAMETRO : LKEY NOMBRE COLON HEMATOCRITO COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_PORCENTAJE COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('hematocrito', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_plaquetas(p):
    'PARAMETRO : LKEY NOMBRE COLON PLAQUETAS COMMA RESULTADO COLON NUM_PLAQUETAS COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('plaquetas', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_neutrofilos(p):
    'PARAMETRO : LKEY NOMBRE COLON NEUTROFILOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('neutrofilos', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_linfocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON LINFOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('linfocitos', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_parametro_monocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON MONOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    
    AP.append('{') # se agrega { al AP
    print("↑ Apilando símbolo '{'")

    p[0] = ('monocitos', p[4], p[8], p[12], p[16], p[17])

    validar_simbs('}') # se desapila el símbolo }

def p_nota_con_coma(p):
    'P : COMMA NOTA COLON SIMBOLOS_NOTA'
    p[0] = p[4]

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