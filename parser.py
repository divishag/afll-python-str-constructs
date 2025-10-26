# parser.py
import ply.yacc as yacc
from lexer import tokens

def p_start(p):
    '''start : statement
             | start statement'''
    pass

# Add rules to handle string literals calling methods
def p_statement_string_upper(p):
    'statement : STRING DOT UPPER LPAREN RPAREN'
    print(f"[OK] Valid: \"{p[1]}\".upper() - Converts string to uppercase")

def p_statement_string_replace(p):
    '''statement : STRING DOT REPLACE LPAREN STRING COMMA STRING RPAREN
                 | STRING DOT REPLACE LPAREN STRING COMMA STRING COMMA NUMBER RPAREN'''
    if len(p) == 9:
        print(f"[OK] Valid: \"{p[1]}\".replace('{p[5]}', '{p[7]}') - Replaces all occurrences")
    else:
        print(f"[OK] Valid: \"{p[1]}\".replace('{p[5]}', '{p[7]}', {p[9]}) - Replaces with max count")

def p_statement_upper(p):
    'statement : ID DOT UPPER LPAREN RPAREN'
    # Check if it's a reserved keyword
    if p[1] in ['if', 'else', 'while', 'for', 'break', 'continue', 'return', 'def',
                'class', 'import', 'from', 'as', 'pass', 'in', 'not', 'and', 'or',
                'True', 'False', 'None']:
        print(f"[ERROR] Reserved keyword '{p[1]}' cannot be used as variable name")
        parser.success = False
        return
    print(f"[OK] Valid: {p[1]}.upper() - Converts string to uppercase")

def p_statement_replace(p):
    '''statement : ID DOT REPLACE LPAREN STRING COMMA STRING RPAREN
                 | ID DOT REPLACE LPAREN STRING COMMA STRING COMMA NUMBER RPAREN'''
    # Check if it's a reserved keyword
    if p[1] in ['if', 'else', 'while', 'for', 'break', 'continue', 'return', 'def',
                'class', 'import', 'from', 'as', 'pass', 'in', 'not', 'and', 'or',
                'True', 'False', 'None']:
        print(f"[ERROR] Reserved keyword '{p[1]}' cannot be used as variable name")
        parser.success = False
        return
    if len(p) == 9:
        print(f"[OK] Valid: {p[1]}.replace('{p[5]}', '{p[7]}') - Replaces all occurrences")
    else:
        print(f"[OK] Valid: {p[1]}.replace('{p[5]}', '{p[7]}', {p[9]}) - Replaces with max count")

def p_error(p):
    if p:
        # Check if it's a reserved keyword
        reserved_keywords = ['if', 'else', 'while', 'for', 'break', 'continue', 'return', 'def', 
                           'class', 'import', 'from', 'as', 'pass', 'in', 'not', 'and', 'or',
                           'True', 'False', 'None']
        if p.type in ['IF', 'ELSE', 'WHILE', 'FOR', 'BREAK', 'CONTINUE', 'RETURN', 'DEF',
                      'CLASS', 'IMPORT', 'FROM', 'AS', 'PASS', 'IN', 'NOT', 'AND', 'OR',
                      'TRUE', 'FALSE', 'NONE']:
            print(f"[ERROR] Reserved keyword '{p.value}' cannot be used as an identifier")
            print(f"  Python reserved keywords like '{p.value}' are not allowed as variable names")
        else:
            print(f"[ERROR] Syntax Error: Unexpected '{p.value}' at position {p.lexpos}")
            print(f"  Expected: valid Python string method call")
    else:
        print("[ERROR] Syntax Error: Unexpected end of input")
    parser.success = False

# Build the parser
parser = yacc.yacc()
parser.success = True
