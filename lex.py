import ply.lex as lex

reserved_words = {
    'for',
    'from',
    'to',
    'while',
    'array',
    'arrayheader',
    'arrayrow',
    'bulletedlist',
    'if'
}

tokens = (
    'NUMBER',
    'STRING',
    'IDENTIFIER',
    'ADD_OP',
    'MUL_OP',
    'COMP_OP',
) + tuple(map(lambda s : s.upper(), reserved_words))

literals = '()"}{,[]=;'

def t_NUMBER(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\"((?!\").)*\"'
    t.value = t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z]+'
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t

def t_ADD_OP(t):
    r'[+-]'
    return t

def t_MUL_OP(t):
    r'[*/]'
    return t

def t_COMP_OP(t):
    r'(==|!=|<|>)'
    return t

def t_EOL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_SPACE(t):
    r'\s'

t_ignore = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    fileContent = open(file).read()
    lex.input(fileContent)
    while 1:
        tok = lex.token()
        if not tok: break
        print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))