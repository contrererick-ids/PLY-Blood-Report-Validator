#1.  Se importa el módulo lex de la biblioteca PLY, que se utiliza para definir el analizador léxico.
import ply.lex as lex

#2.  Se define una lista de tokens que el analizador léxico reconocerá.
tokens = ('FOLIO', 'FECHA_FORMA', 'FECHA_VALIDACION', 'PACIENTE', 'NOMBRE', 'FECHA_NAC', 'SEXO', 'EDAD',
          'NUM', 'FECHA', 'FECHA_HORA', 'CADENA', 'CARACTER', 'LKEY', 'RKEY', 'COLON', 'COMMA')

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

# Símbolos reservados
def t_LKEY(t):
    r'\{'               # Patrón: símbolo { (escapado)
    print("→ Reconocí una LLAVE IZQ")
    return t

def t_RKEY(t):
    r'\}'               # Patrón: símbolo } (escapado)
    print("→ Reconocí una LLAVE DER")
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
def t_NUM(t):
    r'\d+'              # Patrón: uno o más dígitos
    print("→ Reconocí un NÚMERO")
    return t

def t_FECHA(t):
    r'"\d{2}[/]\d{2}[/]\d{4}"'                      # Patrón: dd/mm/yyyy
    print("→ Reconocí una FECHA")
    return t

def t_FECHA_HORA(t):
    r'"\d{2}[/]\d{2}[/]\d{4}\s\d{2}[:]\d{2}[:]\d{2}"'    # Patrón: dd/mm/yyyy hh:mm:ss
    print("→ Reconocí una FECHA Y HORA")
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