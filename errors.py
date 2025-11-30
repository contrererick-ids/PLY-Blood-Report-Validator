
errors = {
    "lexicos": [],
    "sintacticos": [],
    "semanticos": []
}

def add_error(tipo, mensaje):
    errors[tipo].append(mensaje)

def print_errors():
    print("\n======== REPORTE DE ERRORES ========")
    
    if not errors["lexicos"] and not errors["sintacticos"] and not errors["semanticos"]:
        print("✔ No se encontraron errores.")
        return
    
    if errors["lexicos"]:
        print("\n✖ Errores léxicos:")
        for e in errors["lexicos"]:
            print("  -", e)

    if errors["sintacticos"]:
        print("\n✖ Errores sintácticos:")
        for e in errors["sintacticos"]:
            print("  -", e)

    if errors["semanticos"]:
        print("\n✖ Errores semánticos:")
        for e in errors["semanticos"]:
            print("  -", e)
