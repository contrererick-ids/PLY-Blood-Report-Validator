# PLY-Blood-Report-Validator

Un analizador léxico y sintáctico para reportes de laboratorio médico, diseñado específicamente para analizar y validar reportes de Biometría Hemática Completa en formato JSON.

## 📋 Descripción General

Este proyecto implementa el frontend de un compilador utilizando PLY (Python Lex-Yacc) para analizar datos médicos de laboratorio estructurados. Realiza tanto análisis léxico (tokenización) como análisis sintáctico (parsing) para validar la estructura y contenido de reportes de hematología.

## 🎯 Propósito

Los principales objetivos de este proyecto son:
- **Validar** la estructura de reportes de laboratorio médico en formato JSON
- **Tokenizar** datos médicos incluyendo información del paciente, parámetros de pruebas y resultados
- **Analizar** estructuras anidadas complejas con reglas gramaticales apropiadas
- **Asegurar la integridad de datos** para sistemas de información de laboratorio clínico

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **PLY (Python Lex-Yacc)**: Biblioteca para análisis léxico y sintáctico
  - `ply.lex`: Generador de analizador léxico
  - `ply.yacc`: Generador de parser (analizador LALR)

## 📁 Estructura del Proyecto
```
├── lexer.py          # Definición del analizador léxico (tokenizador)
├── parser.py         # Definición del analizador sintáctico (reglas gramaticales)
├── main.py           # Archivo de ejecución principal con datos de prueba
└── README.md         # Documentación del proyecto
```

## ⚙️ Cómo Funciona

### 1. Análisis Léxico (`lexer.py`)

El lexer descompone el texto de entrada en tokens. Reconoce:

- **Palabras reservadas**: `folio`, `paciente`, `nombre`, `fecha_nacimiento`, `sexo`, `edad`, etc.
- **Parámetros médicos**: `Leucocitos`, `Eritrocitos`, `Hemoglobina`, `Hematocrito`, `Plaquetas`, `Neutrofilos`, `Linfocitos`, `Monocitos`
- **Tipos de datos**: 
  - Fechas y marcas de tiempo (`dd/mm/yyyy hh:mm:ss`)
  - Valores numéricos (enteros y decimales)
  - Cadenas de texto
  - Símbolos de unidades médicas (`10^3/μL`, `g/dL`, `%`)
  - Rangos de referencia (`[min - max]`)
- **Símbolos estructurales**: Llaves `{}`, corchetes `[]`, dos puntos `:`, comas `,`

**Prioridad de Tokens**: Los tokens se emparejan según el orden de definición de las funciones en el lexer. Los patrones más específicos deben definirse antes que los generales.

### 2. Análisis Sintáctico (`parser.py`)

El parser valida la estructura gramatical utilizando reglas de gramática libre de contexto. Asegura:

- Anidamiento apropiado de estructuras tipo JSON
- Secuencia correcta de campos de información del paciente
- Estructura válida de lista de parámetros con definiciones recursivas
- Notas opcionales para cada parámetro de prueba
- Sección de firma completa con credenciales profesionales

**Estructura Gramatical**:
```
S → { A }
A → folio: NUM_FOLIO, B
B → fecha_forma: FECHA_HORA, C
...
O → O, PARAMETRO | PARAMETRO
PARAMETRO → { NOMBRE: NOMBRE_PRUEBA, resultado: NUM, unidad: UNIDAD, limite: RANGO P }
P → , nota: SIMBOLOS_NOTA | ε
```

### 3. Ejecución Principal (`main.py`)

El archivo principal:
1. Importa tanto el lexer como el parser
2. Alimenta datos de prueba (reporte médico en formato tipo JSON)
3. Realiza análisis léxico e imprime todos los tokens reconocidos
4. Realiza análisis sintáctico y valida la estructura
5. Muestra el resultado del análisis o mensajes de error

## 🚀 Uso

### Ejecutar el Analizador
```bash
python main.py
```

### Formato de Entrada Esperado
```json
{
    "folio": 12345678,
    "fecha_forma": "01/10/2023 14:30:12",
    "fecha_validacion": "02/10/2023 10:00:27",
    "paciente": {
        "nombre": "Juan Pérez",
        "fecha_nacimiento": "15/05/1980",
        "sexo": "M",
        "edad": 43
    },
    "medico_solicitante": "Dra. María López",
    "seccion": "Biometría Hemática",
    "parametros": [
        {
            "nombre": "Leucocitos",
            "resultado": 5.9,
            "unidad": "10^3/μL",
            "limite": "[4.5 - 10.0]"
        },
        {
            "nombre": "Plaquetas",
            "resultado": 210,
            "unidad": "10^3/μL",
            "limite": "[150 - 400]",
            "nota": "+"
        }
    ],
    "firma": {
        "responsable": "Dra. María López",
        "cedula": "12345678"
    }
}
```

## 📊 Ejemplo de Salida

### Salida del Análisis Léxico
```
→ Reconocí una LLAVE IZQ
→ Reconocí la PALABRA RESERVADA FOLIO
→ Reconocí DOS PUNTOS
→ Reconocí una FOLIO
→ Reconocí una COMA
...
```

### Salida del Análisis Sintáctico
```
======== ANÁLISIS SINTÁCTICO ========
Resultado del análisis sintáctico: 
('{', '}')
```

## 🔍 Características Principales

- **Reconocimiento integral de tokens** para terminología médica
- **Manejo flexible de parámetros** con notas opcionales
- **Gramática recursiva** para listas de parámetros de longitud variable
- **Detección de errores** tanto léxicos como sintácticos
- **Validación de unidades médicas** (μL, g/dL, porcentajes)
- **Análisis de rangos de referencia** en formato `[min - max]`

## 📝 Notas

- El parser utiliza el algoritmo de análisis LALR(1) proporcionado por PLY
- La precedencia de tokens está determinada por el orden de definición de funciones en `lexer.py`
- Cada parámetro médico puede incluir opcionalmente un campo de nota
- La gramática impone una estructura estricta de reporte médico

## 🤝 Contribución

Este es un proyecto académico que demuestra principios de diseño de compiladores aplicados al análisis de datos médicos.

## 📄 Licencia

Solo para fines educativos.

## 📚 English version

See this README in english [here.](README.md)

---

**Nota**: Este analizador está diseñado para demostración educativa de conceptos de análisis léxico y sintáctico. No debe utilizarse en sistemas médicos de producción sin la validación adecuada y el cumplimiento de estándares de datos médicos.