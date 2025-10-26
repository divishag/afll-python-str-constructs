# parser.py
import ply.yacc as yacc
from lexer import tokens

def p_start(p):
    '''start : statement
             | start statement'''
    pass

def p_statement_upper(p):
    'statement : ID DOT UPPER LPAREN RPAREN'
    print(f"[OK] Valid: {p[1]}.upper() - Converts string to uppercase")

def p_statement_replace(p):
    '''statement : ID DOT REPLACE LPAREN STRING COMMA STRING RPAREN
                 | ID DOT REPLACE LPAREN STRING COMMA STRING COMMA NUMBER RPAREN'''
    if len(p) == 9:
        print(f"[OK] Valid: {p[1]}.replace('{p[4]}', '{p[6]}') - Replaces all occurrences")
    else:
        print(f"[OK] Valid: {p[1]}.replace('{p[4]}', '{p[6]}', {p[8]}) - Replaces with max count")

def p_error(p):
    if p:
        print(f"[ERROR] Syntax Error: Unexpected '{p.value}' at position {p.lexpos}")
        print(f"  Expected: valid Python string method call")
    else:
        print("[ERROR] Syntax Error: Unexpected end of input")
    parser.success = False

# Build the parser
parser = yacc.yacc()
parser.success = True
