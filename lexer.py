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
    'REPLACE'
)

# Reserved keywords for string methods
reserved = {
    'upper': 'UPPER',
    'replace': 'REPLACE'
}

# Token regex patterns
t_DOT       = r'\.'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','

def t_ID(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
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
