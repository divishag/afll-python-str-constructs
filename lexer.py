# lexer.py
import ply.lex as lex

# Define all tokens
tokens = (
    'ID',
    'STRING',
    'NUMBER',
    'DOT',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'UPPER',
    'REPLACE',
    # Python reserved keywords
    'IF', 'ELSE', 'WHILE', 'FOR', 'BREAK', 'CONTINUE', 'RETURN', 'DEF', 
    'CLASS', 'IMPORT', 'FROM', 'AS', 'PASS', 'IN', 'NOT', 'AND', 'OR', 
    'TRUE', 'FALSE', 'NONE'
)

# Reserved keywords
reserved = {
    # String method keywords
    'upper': 'UPPER',
    'replace': 'REPLACE',
    # Python reserved keywords
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'def': 'DEF',
    'class': 'CLASS',
    'import': 'IMPORT',
    'from': 'FROM',
    'as': 'AS',
    'pass': 'PASS',
    'in': 'IN',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE'
}

# Token regex patterns
t_DOT       = r'\.'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','

def t_ID(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    # Check if it's a reserved Python keyword
    if t.value in ['if', 'else', 'while', 'for', 'break', 'continue', 'return', 'def', 
                   'class', 'import', 'from', 'as', 'pass', 'in', 'not', 'and', 'or',
                   'True', 'False', 'None']:
        t.type = reserved.get(t.value)
        return t
    # Check if it's a string method keyword
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING_DOUBLE(t):
    r'"([^\\\n"]|(\\.))*?"'
    # Store the actual string content without quotes
    t.value = t.value[1:-1]
    t.type = 'STRING'
    return t

def t_STRING_SINGLE(t):
    r"'([^\\\n']|(\\.))*?'"
    # Store the actual string content without quotes
    t.value = t.value[1:-1]
    t.type = 'STRING'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexer.lexpos}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
