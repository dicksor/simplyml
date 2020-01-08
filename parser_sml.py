import ply.yacc as yacc

from lex import tokens
import AST

precedence = (
    ('left', 'COMP_OP'),
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),  
)

def p_programme_statement(p):
    ''' programme : statement'''
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : assignation 
        | expression
        | structure '''
    p[0] = p[1]

def p_structure_while(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2],p[4]])

def p_structure_for(p):
    ''' structure : FOR IDENTIFIER FROM expression TO expression '{' programme '}' '''
    variable = AST.IdentifierNode(p[2])
    fromNumber = p[4]
    toNumber = p[6]
    assign = AST.AssignNode([variable, fromNumber])

    variable = AST.IdentifierNode(p[2])
    condition = AST.OpNode('<', [variable, toNumber])

    variable = AST.IdentifierNode(p[2])
    increment = AST.OpNode('+', [variable, AST.TokenNode(1)])
    variable = AST.IdentifierNode(p[2])
    increment = AST.AssignNode([variable, increment])

    p[0] = AST.ForNode([assign, condition, increment, p[8]])

def p_structure_if(p):
    ''' structure : IF expression '{' programme '}' '''
    p[0] = AST.IfNode([p[2], p[4]])

def p_structure_bulleted_list(p):
    ''' structure : BULLETEDLIST '{' programme '}' '''
    p[0] = AST.BulletedListNode(p[3])

def p_structure_table(p):
    ''' structure : TABLE '{' programme '}' '''
    p[0] = AST.TableNode(p[3])

def p_structure_table_row(p):
    ''' structure : TABLEROW '{' programme '}' '''
    p[0] = AST.TableRowNode(p[3])

def p_expression_paren(p):
    ''' expression : '(' expression ')' '''
    p[0] = p[2]

def p_expression(p):
    ''' expression : NUMBER 
        | STRING
        | array
        | function '''

    if isinstance(p[1], AST.ArrayNode):
        p[0] = p[1]
    elif isinstance(p[1], AST.FunctionNode):
        p[0] = p[1]
    else:
        p[0] = AST.TokenNode(p[1])

def p_expression_identifier(p):
    ''' expression : IDENTIFIER '''
    p[0] = AST.IdentifierNode(p[1])

def p_expression_op(p):
    ''' expression : expression ADD_OP expression 
        | expression MUL_OP expression 
        | expression COMP_OP expression '''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.IdentifierNode(p[1]),p[3]])

def p_array(p):
    ''' array : '[' parameter ']' '''
    p[0] = AST.ArrayNode(p[2])

def p_function(p):
    ''' function : IDENTIFIER '(' parameter ')' '''
    p[0] = AST.FunctionNode(p[1], p[3])

def p_array_value(p):
    ''' expression : IDENTIFIER '[' IDENTIFIER ']' '''
    array = AST.TokenNode(p[1])
    index = AST.TokenNode(p[3])
    p[0] = AST.ArrayValueNode(array, index)

def p_parameter(p):
    ''' parameter : expression 
        | expression ',' parameter '''
    if len(p) == 4:
        parameters = p[3]
        parameters.insert(0, p[1])
        p[0] = parameters
    elif len(p) == 2:
        parameters = []
        parameters.insert(0, p[1])
        p[0] = parameters

def p_error(p):
    if p:
        print("Syntax error in line %d" % p.lineno)
        parser.errok()
    else:
        print("Sytax error: unexpected end of file!")

def parse(program):
    return yacc.parse(program)

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys 
    import os

    print(os.getcwd())

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    if result:
        print (result)
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name) 
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")