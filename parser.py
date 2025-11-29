# parser.py — versión actualizada conservando tu gramática y tokens
import ply.yacc as yacc
from lexer import tokens
from errors import add_error  # lo añadimos para registrar errores sintácticos


# ==== Helpers ====

def strip_quotes(val):
    """Quita comillas de valores string."""
    if isinstance(val, str) and len(val) >= 2:
        if (val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'"):
            return val[1:-1]
    return val

def to_number(val):
    """Convierte un número encerrado en string a int o float."""
    v = strip_quotes(val)
    try:
        if "." in v:
            return float(v)
        return int(v)
    except:
        return v


# ==== PRODUCCIONES ====

def p_S(p):
    'S : LKEY A RKEY'
    p[0] = p[2]  # A ya será un dict completo


# ---------------------- A: FOLIO ----------------------
def p_folio(p):
    'A : FOLIO COLON NUM_FOLIO COMMA B'
    folio = int(strip_quotes(p[3]))
    dic = p[5]
    dic["folio"] = folio
    p[0] = dic


# ---------------------- B: FECHA_FORMA ----------------------
def p_fecha_forma(p):
    'B : FECHA_FORMA COLON FECHA_HORA COMMA C'
    dic = p[5]
    dic["fecha_forma"] = strip_quotes(p[3])
    p[0] = dic


# ---------------------- C: FECHA_VALIDACION ----------------------
def p_fecha_validacion(p):
    'C : FECHA_VALIDACION COLON FECHA_HORA COMMA D'
    dic = p[5]
    dic["fecha_validacion"] = strip_quotes(p[3])
    p[0] = dic


# ---------------------- D: PACIENTE ----------------------
def p_paciente(p):
    'D : PACIENTE COLON LKEY E RKEY COMMA I'
    paciente = p[4]
    dic = p[7]
    dic["paciente"] = paciente
    p[0] = dic


# ---------------------- E: NOMBRE ----------------------
def p_nombre(p):
    'E : NOMBRE COLON CADENA COMMA F'
    paciente = p[5]
    paciente["nombre"] = strip_quotes(p[3])
    p[0] = paciente


# ---------------------- F: FECHA_NACIMIENTO ----------------------
def p_fecha_nac(p):
    'F : FECHA_NAC COLON FECHA COMMA G'
    paciente = p[5]
    paciente["fecha_nacimiento"] = strip_quotes(p[3])
    p[0] = paciente


# ---------------------- G: SEXO ----------------------
def p_sexo(p):
    'G : SEXO COLON CARACTER COMMA H'
    paciente = p[5]
    paciente["sexo"] = strip_quotes(p[3])
    p[0] = paciente


# ---------------------- H: EDAD ----------------------
def p_edad(p):
    'H : EDAD COLON NUM_EDAD'
    paciente = {}
    paciente["edad"] = int(strip_quotes(p[3]))
    p[0] = paciente


# ---------------------- I: MEDICO_SOLICITANTE ----------------------
def p_medico_solicitante(p):
    'I : MEDICO_SOLICIANTE COLON CADENA COMMA J'
    dic = p[5]
    dic["medico_solicitante"] = strip_quotes(p[3])
    p[0] = dic


# ---------------------- J: SECCION ----------------------
def p_seccion(p):
    'J : SECCION COLON BIOMETRIA_HEMATICA COMMA K'
    dic = p[5]
    dic["seccion"] = strip_quotes(p[3])
    p[0] = dic


# ---------------------- K: PARAMETROS + FIRMA ----------------------
def p_parametros(p):
    'K : PARAMETROS COLON LTKEY O RTKEY COMMA L'
    dic = p[7]
    dic["parametros"] = p[4]
    p[0] = dic


# ---------------------- L: FIRMA ----------------------
def p_firma(p):
    'L : FIRMA COLON LKEY M RKEY'
    p[0] = p[4]  # M contiene responsable+cedula


# ---------------------- M: RESPONSABLE + CEDULA ----------------------
def p_responsable(p):
    'M : RESPONSABLE COLON CADENA COMMA N'
    p[0] = {
        "responsable": strip_quotes(p[3]),
        "cedula": p[5]
    }


# ---------------------- N: CEDULA ----------------------
def p_cedula(p):
    'N : CEDULA COLON NUM_CEDULA'
    p[0] = strip_quotes(p[3])


# ---------------------- LISTAS DE PARÁMETROS ----------------------
def p_lista_parametros_multiple(p):
    'O : O COMMA PARAMETRO'
    p[0] = p[1] + [p[3]]

def p_lista_parametros_simple(p):
    'O : PARAMETRO'
    p[0] = [p[1]]


# ---------------------- DEFINICIÓN DE CADA PARÁMETRO ----------------------
# Cada parámetro devuelve:  dict(nombre, resultado, unidad, limite, nota)

def _armar_parametro(nombre, resultado, unidad, limite, nota):
    return {
        "nombre": strip_quotes(nombre),
        "resultado": to_number(resultado),
        "unidad": strip_quotes(unidad),
        "limite": strip_quotes(limite),
        "nota": strip_quotes(nota) if nota else None
    }

def p_parametro_leucocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON LEUCOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_eritrocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON ERITROCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_hemoglobina(p):
    'PARAMETRO : LKEY NOMBRE COLON HEMOGLOBINA COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_GPD COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_hematocrito(p):
    'PARAMETRO : LKEY NOMBRE COLON HEMATOCRITO COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_PORCENTAJE COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_plaquetas(p):
    'PARAMETRO : LKEY NOMBRE COLON PLAQUETAS COMMA RESULTADO COLON NUM_PLAQUETAS COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_neutrofilos(p):
    'PARAMETRO : LKEY NOMBRE COLON NEUTROFILOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_linfocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON LINFOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])

def p_parametro_monocitos(p):
    'PARAMETRO : LKEY NOMBRE COLON MONOCITOS COMMA RESULTADO COLON NUM_RESULTADO COMMA UNIDAD COLON SIMBOLO_UNIDAD_MCPL COMMA LIMITE COLON LIMITE_VALUES P RKEY'
    p[0] = _armar_parametro(p[4], p[8], p[12], p[16], p[17])


# ---------------------- NOTA ----------------------
def p_nota_con_coma(p):
    'P : COMMA NOTA COLON SIMBOLOS_NOTA'
    p[0] = strip_quotes(p[4])

def p_nota_vacia(p):
    'P : '
    p[0] = None


# ---------------------- ERRORES ----------------------
def p_error(p):
    if p:
        add_error("sintacticos", f"Token inesperado: '{p.value}'")
    else:
        add_error("sintacticos", "Error de sintaxis: fin inesperado del archivo")


#4. Construcción del analizador sintáctico
parser = yacc.yacc()
