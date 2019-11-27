import AST
from AST import addToClass
from functools import reduce

functions = {
    'title' : lambda content: "<h1>" + content + "</h1>",
    'subTitle' : lambda content: "<h3>" + content + "</h3>",
    'paragraph' : lambda content: "<p>" + content + "</p>"
}

operator = {
    '<' : lambda x, y: x < y,
    '+' : lambda x, y: x + y 
}

variables = {}

@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for child in self.children:
        bytecode += child.compile()
    return bytecode

@addToClass(AST.FunctionNode)
def compile(self):
    childBytecode = self.children[0].compile()
    bytecode = functions[self.name](childBytecode)
    return bytecode

@addToClass(AST.TokenNode)
def compile(self):
    return self.tok

@addToClass(AST.IdentifierNode)
def compile(self):
    return variables[self.tok]

@addToClass(AST.AssignNode)
def compile(self):
    childName = self.children[0].tok
    childValue = self.children[1].compile()
    variables[childName] = childValue
    return ""

@addToClass(AST.OpNode)
def compile(self):
    x = self.children[0].compile()
    y = self.children[1].compile()
    result = operator[self.op](x, y)
    print("%s %s %s = %s" % (x, self.op, y, result))
    return result

@addToClass(AST.WhileNode)
def compile(self):
    cond = self.children[0]
    body = self.children[1]
    bytecode = ""

    while cond.compile():
        bytecode += body.compile()

    return bytecode



if __name__ == "__main__":
    from parser_sml import parse
    import sys, os
    
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()

    name = os.path.splitext(sys.argv[1])[0]+'.html'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()

    print("Wrote output to " , name)