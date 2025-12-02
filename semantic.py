import re
from errors import add_error
from datetime import datetime

# ---------------- VALIDADORES AUXILIARES ----------------

def validar_edad(fecha_nac_str, fecha_forma_str, edad_reportada):
    # --- Parseo de fechas ---
    try:
        fecha_nac = datetime.strptime(fecha_nac_str.replace('"', ''), "%d/%m/%Y")
    except:
        add_error("semanticos", f"Fecha de nacimiento inválida: {fecha_nac_str}")
        return

    try:
        # fecha_forma incluye hora → %d/%m/%Y %H:%M:%S
        fecha_forma = datetime.strptime(fecha_forma_str.replace('"', ''), "%d/%m/%Y %H:%M:%S")
    except:
        add_error("semanticos", f"Fecha de emisión inválida: {fecha_forma_str}")
        return

    # --- Cálculo correcto de edad con referencia a fecha_forma ---
    años = fecha_forma.year - fecha_nac.year

    # Si todavía no ha cumplido años en esa fecha
    if (fecha_forma.month, fecha_forma.day) < (fecha_nac.month, fecha_nac.day):
        años -= 1

    # --- Validación ---
    if años != edad_reportada:
        add_error(
            "semanticos",
            f"Inconsistencia: La edad declarada ({edad_reportada}) "
            f"no coincide con la edad calculada ({años}) según fecha_forma."
        )


# ---------------- CONSTANTES ----------------

PARAM_VALIDOS = {
    "Leucocitos", "Eritrocitos", "Hemoglobina", "Hematocrito",
    "Plaquetas", "Neutrófilos", "Linfocitos", "Monocitos"
}

LIMITE_RE = re.compile(r'\[\d+(\.\d+)?\s-\s\d+(\.\d+)?\]')

SIMBOLOS_NOTA_VALIDOS = {"*", "**", "+"}


# ---------------- ANÁLISIS SEMÁNTICO ----------------

def validar_semantica(arbol):
    if not arbol:
        add_error("semanticos", "No se puede validar semántica: estructura vacía.")
        return

    # ---------------- PARÁMETROS ----------------
    parametros = arbol.get("parametros", [])

    for p in parametros:

        # --- 1. Validación del nombre del parámetro ---
        nombre = p.get("nombre")
        if nombre not in PARAM_VALIDOS:
            add_error("semanticos", f"'{nombre}' no pertenece a la sección 'Biometría Hemática'.")

        # --- 2. Validación del límite ---
        limite = p.get("limite", "")
        limite_limpio = limite.replace('"', '').strip()

        if not LIMITE_RE.fullmatch(limite_limpio):
            add_error("semanticos", f"Límite '{limite}' no cumple el formato '[x - y]'.")

        # --- 3. Validación de nota opcional ---
        nota = p.get("nota")
        if nota and nota not in SIMBOLOS_NOTA_VALIDOS:
            add_error("semanticos", f"Símbolo de nota '{nota}' inválido. Debe ser *, ** o +.")

    # ---------------- CEDULA ----------------
    cedula = arbol.get("cedula", "")

    if not re.fullmatch(r"\d{8}", cedula):
        add_error("semanticos", f"La cédula profesional '{cedula}' debe tener exactamente 8 dígitos.")

    # ---------------- FECHAS ----------------
    fecha_forma = arbol.get("fecha_forma")
    fecha_validacion = arbol.get("fecha_validacion")

    try:
        f1 = datetime.strptime(fecha_forma, "%d/%m/%Y %H:%M:%S")
        f2 = datetime.strptime(fecha_validacion, "%d/%m/%Y %H:%M:%S")

        if f1 > f2:
            add_error("semanticos", "La fecha de toma no puede ser posterior a la fecha de validación.")
    except:
        add_error("semanticos", "Formato de fecha inválido en fecha_forma o fecha_validacion.")

    # ---------------- PACIENTE ----------------
    paciente = arbol.get("paciente", {})

    fecha_nac = paciente.get("fecha_nacimiento")
    fecha_forma = arbol.get("fecha_forma")
    edad = paciente.get("edad")

    if fecha_nac and edad is not None:
        validar_edad(fecha_nac, fecha_forma, edad)
    else:
        add_error("semanticos", "Datos incompletos del paciente (edad o fecha de nacimiento faltantes).")
