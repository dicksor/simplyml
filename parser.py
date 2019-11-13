import ply.yacc as yacc

from lex import tokens
import AST

def p_programme(p):
    ''' programme : statement 
        | statement EOL programme '''
    if(len(p) == 2):
        p[0] = AST.ProgramNode(p[1])
    else:
        p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : assignation 
        | structure 
        | function '''

def p_structure_while(p):
    ''' structure : WHILE expression '{' programme '}' '''

def p_structure_for(p):
    ''' structure : FOR IDENTIFIER FROM NUMBER TO NUMBER '{' programme '}' '''

def p_structure_if(p):
    ''' structure : IF expression '{' programme '}' '''

def p_structure_bulleted_list(p):
    ''' structure : BULLETEDLIST '{' programme '}' '''

def p_structure_array(p):
    ''' structure : ARRAY '{' programme '}' '''

def p_structure_array_header(p):
    ''' structure : ARRAYHEADER '{' programme '}' '''

def p_structure_array_row(p):
    ''' structure : ARRAYROW '{' programme '}' '''

def p_expression_paren(p):
    ''' expression : '(' expression ')' '''

def p_expression(p):
    ''' expression :  NUMBER 
        | IDENTIFIER 
        | STRING '''

def p_expression_op(p):
    ''' expression : expression ADD_OP expression 
        | expression MUL_OP expression 
        | expression COMP_OP expression '''

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''

def p_parameter(p):
    ''' parameter : expression 
        | expression ',' parameter '''

def p_function(p):
    ''' function : IDENTIFIER '(' parameter ')' '''

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
    	
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=True)
    if result:
        print (result)
            
        import os
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name) 
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")