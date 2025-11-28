# PLY-Blood-Report-Validator

A lexical and syntactic analyzer for medical laboratory reports, specifically designed to parse and validate Complete Blood Count (CBC) / Hematology reports in JSON format.

## 📋 Overview

This project implements a compiler front-end using PLY (Python Lex-Yacc) to parse structured medical laboratory data. It performs both lexical analysis (tokenization) and syntactic analysis (parsing) to validate the structure and content of hematology reports.

## 🎯 Purpose

The main objectives of this project are:
- **Validate** the structure of medical laboratory reports in JSON format
- **Tokenize** medical data including patient information, test parameters, and results
- **Parse** complex nested structures with proper grammar rules
- **Ensure data integrity** for clinical laboratory information systems

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **PLY (Python Lex-Yacc)**: Lexical and syntactic analysis library
  - `ply.lex`: Lexical analyzer generator
  - `ply.yacc`: Parser generator (LALR parser)

## 📁 Project Structure
```
├── lexer.py          # Lexical analyzer definition (tokenizer)
├── parser.py         # Syntactic analyzer definition (grammar rules)
├── main.py           # Main execution file with test data
└── README.md         # Project documentation
```

## ⚙️ How It Works

### 1. Lexical Analysis (`lexer.py`)

The lexer breaks down the input text into tokens. It recognizes:

- **Reserved keywords**: `folio`, `paciente`, `nombre`, `fecha_nacimiento`, `sexo`, `edad`, etc.
- **Medical parameters**: `Leucocitos`, `Eritrocitos`, `Hemoglobina`, `Hematocrito`, `Plaquetas`, `Neutrofilos`, `Linfocitos`, `Monocitos`
- **Data types**: 
  - Dates and timestamps (`dd/mm/yyyy hh:mm:ss`)
  - Numeric values (integers and decimals)
  - Text strings
  - Medical unit symbols (`10^3/μL`, `g/dL`, `%`)
  - Reference ranges (`[min - max]`)
- **Structural symbols**: Braces `{}`, brackets `[]`, colons `:`, commas `,`

**Token Priority**: Tokens are matched based on the order of function definitions in the lexer. More specific patterns should be defined before general ones.

### 2. Syntactic Analysis (`parser.py`)

The parser validates the grammatical structure using context-free grammar rules. It ensures:

- Proper nesting of JSON-like structures
- Correct sequence of patient information fields
- Valid parameter list structure with recursive definitions
- Optional notes for each test parameter
- Complete signature section with professional credentials

**Grammar Structure**:
```
S → { A }
A → folio: NUM_FOLIO, B
B → fecha_forma: FECHA_HORA, C
...
O → O, PARAMETRO | PARAMETRO
PARAMETRO → { NOMBRE: TEST_NAME, resultado: NUM, unidad: UNIT, limite: RANGE P }
P → , nota: SIMBOLOS_NOTA | ε
```

### 3. Main Execution (`main.py`)

The main file:
1. Imports both lexer and parser
2. Feeds test data (medical report in JSON-like format)
3. Performs lexical analysis and prints all recognized tokens
4. Performs syntactic analysis and validates the structure
5. Outputs the parsing result or error messages

## 🚀 Usage

### Running the Analyzer
```bash
python main.py
```

### Expected Input Format
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

## 📊 Output Example

### Lexical Analysis Output
```
→ Reconocí una LLAVE IZQ
→ Reconocí la PALABRA RESERVADA FOLIO
→ Reconocí DOS PUNTOS
→ Reconocí una FOLIO
→ Reconocí una COMA
...
```

### Syntactic Analysis Output
```
======== ANÁLISIS SINTÁCTICO ========
Resultado del análisis sintáctico: 
('{', '}')
```

## 🔍 Key Features

- **Comprehensive token recognition** for medical terminology
- **Flexible parameter handling** with optional notes
- **Recursive grammar** for variable-length parameter lists
- **Error detection** for both lexical and syntactic errors
- **Medical unit validation** (μL, g/dL, percentages)
- **Reference range parsing** in `[min - max]` format

## 📝 Notes

- The parser uses LALR(1) parsing algorithm provided by PLY
- Token precedence is determined by function definition order in `lexer.py`
- Each medical parameter can optionally include a note field
- The grammar enforces strict medical report structure

## 🤝 Contributing

This is an academic project demonstrating compiler design principles applied to medical data parsing.

## 📄 License

Educational purposes only.

## 📚 Versión en Español

Lea este README en español [aquí.](README.es.md)

---

**Note**: This parser is designed for educational demonstration of lexical and syntactic analysis concepts. It should not be used in production medical systems without proper validation and compliance with medical data standards.