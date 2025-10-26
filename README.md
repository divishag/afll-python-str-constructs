# Python String Method Syntax Validator

A Context-Free Grammar (CFG) based syntax validator for Python string methods using PLY (Python Lex-Yacc) tools.

## 📋 Overview

This project implements a lexical analyzer and parser to validate the syntax of Python string method calls. It uses PLY to define a context-free grammar that recognizes valid string method invocations and their parameters.

## ✨ Features

### Supported String Methods

1. **upper()** - Converts string to uppercase
2. **replace(old, new)** - Replaces all occurrences
3. **replace(old, new, count)** - Replaces with maximum count

## 🏗️ Architecture

### Files Structure

```
.
├── lexer.py      # Lexical analyzer (tokenizer)
├── parser.py     # Syntax parser (CFG rules)
├── main.py       # Main program interface
└── README.md     # This file
```

### Components

#### 1. Lexer (`lexer.py`)

- Tokenizes input into lexemes
- Recognizes: identifiers, strings, numbers, operators
- Handles reserved keywords for string methods
- Defines token patterns using regex

**Key Tokens:**

- `ID` - Identifiers (variable names)
- `STRING` - String literals (single or double quotes)
- `NUMBER` - Integer literals
- Punctuation: `.`, `(`, `)`, `,`
- Reserved keywords: `upper`, `replace`

#### 2. Parser (`parser.py`)

- Implements context-free grammar rules
- Validates syntax structure
- Provides detailed error messages
- Matches valid Python string method call patterns

**Grammar Structure:**

```
statement → ID DOT METHOD_NAME LPAREN [args] RPAREN
```

#### 3. Main Program (`main.py`)

- Interactive command-line interface
- Displays usage examples
- Processes user input
- Shows validation results

## 🚀 Usage

### Running the Program

**Interactive Mode:**

```bash
python main.py
```

**Run Automated Tests:**

```bash
python test.py
```

### Example Interactions

**Valid Statements:**

```
myStr.upper()                            [OK] Valid
word.replace("a", "b")                   [OK] Valid
text.replace("old", "new", 3)            [OK] Valid
```

**Invalid Statements:**

```
myStr.upper(                            [ERROR] Syntax error
replace("a", "b")                       [ERROR] Missing dot notation
myStr.uppercase()                       [ERROR] Invalid method
text.lower()                            [ERROR] Invalid method
```

## 🔧 How It Works

### Lexical Analysis

1. Input string is tokenized into atomic elements
2. Each token is classified (identifier, string, operator, etc.)
3. Reserved words are recognized and marked
4. Tokens are passed to the parser

### Syntax Analysis

1. Parser receives token stream
2. Grammar rules are applied recursively
3. Syntax tree is built if input matches valid pattern
4. Validation messages are displayed

### Example Parse Tree

```
Input: myStr.upper()

Parse Tree:
    statement
     /   \
   ID    DOT
  (myStr) (.)
          |
       UPPER
        (upper)
         |
       LPAREN
         |
       RPAREN
```

## 📚 Grammar Rules

### Production Rules

```bnf
start              → statement | start statement
statement          → ID DOT METHOD_NAME LPAREN args RPAREN

METHOD_NAME        → UPPER | REPLACE

args               → ε
                   | STRING COMMA STRING
                   | STRING COMMA STRING COMMA NUMBER
```

## 🎯 Use Cases

- **Educational Purpose**: Learn CFG and compiler design
- **Syntax Validation**: Verify Python string method syntax
- **Parser Development**: Template for building custom parsers
- **Language Processing**: Foundation for language interpreters

## 🛠️ Technologies

- **Python 3.x**
- **PLY (Python Lex-Yacc)** - Lexer and parser generator
- **Regex** - Pattern matching for tokenization

## 📝 Notes

- This validator checks **syntax only**, not semantics
- Variable names are not type-checked
- Does not execute the methods
- Validates method signatures and parameter types
- **Mismatched quotes are detected** (e.g., `"abc'` is invalid)

## 🤝 Contributing

Feel free to extend this project by:

- Adding more string methods
- Supporting more complex expressions
- Adding type checking
- Implementing actual method execution

## 📄 License

This project is for educational purposes.

---

**Created for AFLL (Automata Formal Languages and Logic) Course**
