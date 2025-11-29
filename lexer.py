#1.  Se importa el módulo lex de la biblioteca PLY, que se utiliza para definir el analizador léxico.
import ply.lex as lex

#2.  Se define una lista de tokens que el analizador léxico reconocerá.
tokens = ('FOLIO', 'NUM_FOLIO', 'FECHA_FORMA', 'FECHA_VALIDACION', 'PACIENTE', 'NOMBRE', 'FECHA_NAC', 'SEXO', 'EDAD',
          'MEDICO_SOLICIANTE', 'SECCION', 'BIOMETRIA_HEMATICA', 'PARAMETROS', 'RESULTADO', 'UNIDAD', 'LIMITE', 
          'LEUCOCITOS', 'ERITROCITOS', 'HEMOGLOBINA', 'HEMATOCRITO', 'PLAQUETAS', 'NEUTROFILOS', 'LINFOCITOS', 'MONOCITOS',
          'SIMBOLO_UNIDAD_MCPL', 'SIMBOLO_UNIDAD_GPD', 'SIMBOLO_UNIDAD_PORCENTAJE', 'NUM_RESULTADO', 'NUM_PLAQUETAS', 'LIMITE_VALUES', 'NOTA', 'SIMBOLOS_NOTA',
          'FIRMA', 'RESPONSABLE', 'CEDULA', 'NUM_CEDULA',
          'NUM_EDAD', 'FECHA', 'FECHA_HORA', 'CADENA', 'CARACTER', 'LKEY', 'RKEY', 'LTKEY', 'RTKEY', 'COLON', 'COMMA')

# 3. Se definen las expresiones regulares para cada token a través de una función
# Palabras reservadas
def t_FOLIO(t):
    r'"folio"'          # Patrón: palabra reservada FOLIO
    print("→ Reconocí la PALABRA RESERVADA FOLIO")
    return t

def t_FECHA_FORMA(t):
    r'"fecha_forma"'    # Patrón: palabra reservada FECHA_FORMA
    print("→ Reconocí la PALABRA RESERVADA FECHA_FORMA")
    return t

def t_FECHA_VALIDACION(t):
    r'"fecha_validacion"'       # Patrón: palabra reservada FECHA_VALIDACION
    print("→ ReconocÍ la PALABRA RESERVADA FECHA_VALIDACION")
    return t

def t_PACIENTE(t):
    r'"paciente"'       # Patrón: palabra reservada PACIENTE
    print("→ ReconocÍ la PALABRA RESERVADA PACIENTE")
    return t

def t_NOMBRE(t):
    r'"nombre"'         # Patrón: palabra reservada NOMBRE
    print("→ ReconocÍ la PALABRA RESERVADA NOMBRE")
    return t

def t_FECHA_NAC(t):
    r'"fecha_nacimiento"'       # Patrón: palabra reservada FECHA_NAC
    print("→ ReconocÍ la PALABRA RESERVADA FECHA_NAC")
    return t

def t_SEXO(t):
    r'"sexo"'           # Patrón: palabra reservada SEXO
    print("→ ReconocÍ la PALABRA RESERVADA SEXO")
    return t

def t_EDAD(t):
    r'"edad"'           # Patrón: palabra reservada EDAD
    print("→ ReconocÍ la PALABRA RESERVADA EDAD")
    return t

def t_MEDICO_SOLICIANTE(t):
    r'"medico_solicitante"'     # Patrón: palabra reservada MEDICO_SOLICIANTE
    print("→ ReconocÍ la PALABRA RESERVADA MEDICO_SOLICIANTE")
    return t

def t_SECCION(t):
    r'"seccion"'       # Patrón: palabra reservada SECCION
    print("→ ReconocÍ la PALABRA RESERVADA SECCION")
    return t

def t_BIOMETRIA_HEMATICA(t):
    r'"Biometría\sHemática"'     # Patrón: palabra reservada BIOMETRIA_HEMATICA
    print("→ ReconocÍ la PALABRA RESERVADA BIOMETRIA_HEMATICA")
    return t

def t_PARAMETROS(t):
    r'"parametros"'     # Patrón: palabra reservada PARAMETROS
    print("→ ReconocÍ la PALABRA RESERVADA PARAMETROS")
    return t

def t_LEUCOCITOS(t):
    r'"Leucocitos"'     # Patrón: palabra reservada LEUCOCITOS
    print("→ ReconocÍ la PALABRA RESERVADA LEUCOCITOS")
    return t

def t_ERITROCITOS(t):
    r'"Eritrocitos"'    # Patrón: palabra reservada ERITROCITOS
    print("→ ReconocÍ la PALABRA RESERVADA ERITROCITOS")
    return t

def t_HEMOGLOBINA(t):
    r'"Hemoglobina"'    # Patrón: palabra reservada HEMOGLOBINA
    print("→ ReconocÍ la PALABRA RESERVADA HEMOGLOBINA")
    return t

def t_HEMATOCRITO(t):
    r'"Hematocrito"'    # Patrón: palabra reservada HEMATOCRITO
    print("→ ReconocÍ la PALABRA RESERVADA HEMATOCRITO")
    return t

def t_PLAQUETAS(t):
    r'"Plaquetas"'      # Patrón: palabra reservada PLAQUETAS
    print("→ ReconocÍ la PALABRA RESERVADA PLAQUETAS")
    return t

def t_NEUTROFILOS(t):
    r'"Neutrófilos"'    # Patrón: palabra reservada NEUTROFILOS
    print("→ ReconocÍ la PALABRA RESERVADA NEUTROFILOS")
    return t

def t_LINFOCITOS(t):
    r'"Linfocitos"'     # Patrón: palabra reservada LINFOCITOS
    print("→ ReconocÍ la PALABRA RESERVADA LINFOCITOS")
    return t

def t_MONOCITOS(t):
    r'"Monocitos"'      # Patrón: palabra reservada MONOCITOS
    print("→ ReconocÍ la PALABRA RESERVADA MONOCITOS")
    return t

def t_NOTA(t):
    r'"nota"'           # Patrón: palabra reservada NOTA
    print("→ ReconocÍ la PALABRA RESERVADA NOTA")
    return t

def t_SIMBOLOS_NOTA(t):
    r'"\*?\**?\+?"'            # Patrón: cadena de texto para símbolos de nota
    print("→ ReconocÍ los SÍMBOLOS DE NOTA")
    return t

def t_FIRMA(t):
    r'"firma"'          # Patrón: palabra reservada FIRMA
    print("→ ReconocÍ la PALABRA RESERVADA FIRMA")
    return t

def t_RESPONSABLE(t):
    r'"responsable"'    # Patrón: palabra reservada RESPONSABLE
    print("→ ReconocÍ la PALABRA RESERVADA RESPONSABLE")
    return t

def t_CEDULA(t):
    r'"cedula"'         # Patrón: palabra reservada CEDULA
    print("→ ReconocÍ la PALABRA RESERVADA CEDULA")
    return t

def t_RESULTADO(t):
    r'"resultado"'      # Patrón: palabra reservada RESULTADO
    print("→ ReconocÍ la PALABRA RESERVADA RESULTADO")
    return t

def t_UNIDAD(t):
    r'"unidad"'         # Patrón: palabra reservada UNIDAD
    print("→ ReconocÍ la PALABRA RESERVADA UNIDAD")
    return t

def t_LIMITE(t):
    r'"limite"'         # Patrón: palabra reservada LIMITE
    print("→ ReconocÍ la PALABRA RESERVADA LIMITE")
    return t

# Símbolos reservados
def t_SIMBOLO_UNIDAD_MCPL(t):
    r'"10\^\d+/[μm]L"'     # Patrón: cadena de texto para símbolo de unidad
    print("→ ReconocÍ un SÍMBOLO DE UNIDAD DE MILIMETROS CUBICOS POR LITRO")
    return t

def t_SIMBOLO_UNIDAD_GPD(t):
    r'"g/dL" '     # Patrón: cadena de texto para símbolo de unidad
    print("→ ReconocÍ un SÍMBOLO DE UNIDAD DE GRAMOS POR DECILITRO")
    return t

def t_SIMBOLO_UNIDAD_PORCENTAJE(t):
    r'"%" '     # Patrón: cadena de texto para símbolo de unidad
    print("→ ReconocÍ un SÍMBOLO DE UNIDAD DE PORCENTAJE")
    return t

def t_LKEY(t):
    r'\{'               # Patrón: símbolo { (escapado)
    print("→ Reconocí una LLAVE IZQ")
    return t

def t_RKEY(t):
    r'\}'               # Patrón: símbolo } (escapado)
    print("→ Reconocí una LLAVE DER")
    return t

def t_LTKEY(t):
    r'\['               # Patrón: símbolo [ (escapado)
    print("→ ReconocÍ un CORCHETE IZQ")
    return t

def t_RTKEY(t):
    r'\]'               # Patrón: símbolo ] (escapado)
    print("→ ReconocÍ un CORCHETE DER")
    return t

def t_COLON(t):
    r':\s'                # Patrón: símbolo : (escapado)
    print("→ Reconocí DOS PUNTOS")
    return t

def t_COMMA(t):
    r',\s'                # Patrón: símbolo , (escapado)
    print("→ ReconocÍ una COMA")
    return t

# Tipos de datos
def t_LIMITE_VALUES(t):
    r'"\[\d{1,3}\.?\d*\s-\s\d{1,3}\.?\d*\]"'   # Patrón: cadena de texto para límite de valores "[num - num]"
    print("→ ReconocÍ un RANGO DE LÍMITES")
    return t

def t_NUM_CEDULA(t):
    r'"\d{8}"'            # Patrón: cadena de dígitos entre comillas
    print("→ ReconocÍ una CÉDULA")
    return t

def t_FECHA(t):
    r'"\d{2}[/]\d{2}[/]\d{4}"'                      # Patrón: dd/mm/yyyy
    print("→ Reconocí una FECHA")
    return t

def t_FECHA_HORA(t):
    r'"\d{2}[/]\d{2}[/]\d{4}\s\d{2}[:]\d{2}[:]\d{2}"'    # Patrón: dd/mm/yyyy hh:mm:ss
    print("→ Reconocí una FECHA Y HORA")
    return t

def t_NUM_FOLIO(t):
    r'\d{8}'                # Patrón: ocho dígitos
    print("→ ReconocÍ un FOLIO")
    return t

def t_NUM_EDAD(t):
    r'\d{1,2}(?!\d|\.)'                # Patrón: uno a tres dígitos y que NO acepta decimales
    print("→ ReconocÍ una EDAD")
    return t

def t_NUM_PLAQUETAS(t):
    r'\d{3}'              # Patrón: uno o más dígitos con opcional punto decimal
    print("→ Reconocí un RESULTADO NUMÉRICO")
    return t

def t_NUM_RESULTADO(t):
    r'\d{1,2}\.?\d*'              # Patrón: uno o más dígitos con opcional punto decimal
    print("→ Reconocí un RESULTADO NUMÉRICO")
    return t

def t_CARACTER(t):
    r'"M" | "F"'        # Patrón: "M" o "F"
    print("→ Reconocí un CARACTER")
    return t

def t_CADENA(t):
    r'".+?"'            # Patrón: cadena de texto
    print("→ Reconocí una CADENA DE TEXTO")
    return t

#4. Se especifican los caracteres que se deben ignorar (espacios, tabuladores y saltos de línea)
t_ignore = ' \t\n'

#5. Se define una función para manejar caracteres ilegales
def t_error(t):
    print(f" ERROR: Carácter '{t.value[0]}' no válido")  # Imprime el carácter ilegal
    t.lexer.skip(1)  # Salta el carácter ilegal

#6. Se construye el analizador léxico utilizando la función lex.lex().
lexer = lex.lex() # Se crea instancia del analizador léxico